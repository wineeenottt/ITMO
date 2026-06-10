import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def g1_sys1(x1, x2):
    return 0.5 * math.cos(x2) + 0.5

def g2_sys1(x1, x2):
    return 0.5 * math.sin(x1) + 0.5

def f1_sys1(x1, x2):
    return x1 - 0.5 * math.cos(x2) - 0.5

def f2_sys1(x1, x2):
    return x2 - 0.5 * math.sin(x1) - 0.5

def dg1dx1_sys1(x1, x2):
    return 0

def dg1dx2_sys1(x1, x2):
    return -0.5 * math.sin(x2)

def dg2dx1_sys1(x1, x2):
    return 0.5 * math.cos(x1)

def dg2dx2_sys1(x1, x2):
    return 0

def g1_sys2(x1, x2):
    return math.sin(x2) / 2 + 1

def g2_sys2(x1, x2):
    return math.cos(x1) / 2 + 1

def f1_sys2(x1, x2):
    return x1 - math.sin(x2) / 2 - 1

def f2_sys2(x1, x2): return x2 - math.cos(x1) / 2 - 1

def dg1dx1_sys2(x1, x2):
    return 0

def dg1dx2_sys2(x1, x2):
    return math.cos(x2) / 2

def dg2dx1_sys2(x1, x2):
    return -math.sin(x1) / 2

def dg2dx2_sys2(x1, x2):
    return 0

SYSTEMS = {
    1: {
        'name': 'x1 - 0.5cos(x2) - 0.5 = 0\nx2 - 0.5sin(x1) - 0.5 = 0',
        'g1': g1_sys1, 'g2': g2_sys1,
        'f1': f1_sys1, 'f2': f2_sys1,
        'dg1dx1': dg1dx1_sys1, 'dg1dx2': dg1dx2_sys1,
        'dg2dx1': dg2dx1_sys1, 'dg2dx2': dg2dx2_sys1,
        'plot_range': (-1, 2, -1, 2)
    },
    2: {
        'name': 'x1 - sin(x2)/2 - 1 = 0\nx2 - cos(x1)/2 - 1 = 0',
        'g1': g1_sys2, 'g2': g2_sys2,
        'f1': f1_sys2, 'f2': f2_sys2,
        'dg1dx1': dg1dx1_sys2, 'dg1dx2': dg1dx2_sys2,
        'dg2dx1': dg2dx1_sys2, 'dg2dx2': dg2dx2_sys2,
        'plot_range': (0, 3, 0, 3)
    }
}

def simple_iteration(g1, g2, x1, x2, eps, max_iter=1000):
    iteration = 0
    while iteration < max_iter:
        iteration += 1
        x1_new = g1(x1, x2)
        x2_new = g2(x1, x2)
        if max(abs(x1_new - x1), abs(x2_new - x2)) < eps:
            return {'root': (x1_new, x2_new), 'iterations': iteration}
        x1, x2 = x1_new, x2_new
    raise ValueError("Точность не достигнута за максимальное число итераций")


def check(system, x1, x2):
    row1 = abs(system['dg1dx1'](x1, x2)) + abs(system['dg1dx2'](x1, x2))
    row2 = abs(system['dg2dx1'](x1, x2)) + abs(system['dg2dx2'](x1, x2))
    q = max(row1, row2)
    return q < 1, q


def plot_system(f1, f2, root, plot_range, system_name):
    x1_min, x1_max, x2_min, x2_max = plot_range

    x1_vals = np.linspace(x1_min, x1_max, 400)
    x2_vals = np.linspace(x2_min, x2_max, 400)
    X1, X2 = np.meshgrid(x1_vals, x2_vals)

    F1 = np.vectorize(f1)
    F2 = np.vectorize(f2)

    Z1 = F1(X1, X2)
    Z2 = F2(X1, X2)

    plt.figure(figsize=(10, 8))

    plt.contour(X1, X2, Z1, levels=[0], colors='blue', linewidths=2)
    plt.contour(X1, X2, Z2, levels=[0], colors='green', linewidths=2)

    if root:
        plt.plot(root[0], root[1], 'ro', markersize=10, label=f'Корень: ({root[0]:.4f}, {root[1]:.4f})')


    plt.grid(True, alpha=0.3, linestyle='--')
    plt.xlabel('x₁', fontsize=12)
    plt.ylabel('x₂', fontsize=12)
    plt.title(f'График системы:\n{system_name}', fontsize=11, pad=20)
    plt.legend(fontsize=10)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def save_results_to_file(system_name, root, iterations, x1_0, x2_0, eps, q, is_correct):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"system_results_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("РЕЗУЛЬТАТЫ РЕШЕНИЯ СИСТЕМЫ НЕЛИНЕЙНЫХ УРАВНЕНИЙ\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Система уравнений:\n{system_name}\n\n")
        f.write(f"Начальное приближение: x₁₀ = {x1_0:.6f}, x₂₀ = {x2_0:.6f}\n")
        f.write(f"Точность: ε = {eps}\n")
        f.write(f"Коэффициент сходимости: q = {q:.6f}\n")
        f.write(f"Дата и время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n\n")
        f.write("-" * 60 + "\n")
        f.write("РЕШЕНИЕ:\n")
        f.write("-" * 60 + "\n")
        f.write(f"x₁ = {root[0]:.12f}\n")
        f.write(f"x₂ = {root[1]:.12f}\n")
        f.write(f"Число итераций: {iterations}\n")
        f.write(f"Статус: {'Верно' if is_correct else 'Неточное'}\n")
        f.write("=" * 60 + "\n")

    print(f"\nРезультаты сохранены в файл: {filename}")
    return filename
def display_system():
    print("\nДОСТУПНЫЕ СИСТЕМЫ:")
    for key, value in SYSTEMS.items():
        print(f"\n{key}.")
        for line in value['name'].split('\n'):
            print(f"{line}")

def get_input_source():
    print("\nВыберите источник ввода данных:")
    print("1. С клавиатуры")
    print("2. Из файла")
    while True:
        try:
            choice = int(input("Ваш выбор (1-2): ").strip())
            if choice in [1, 2]:
                return str(choice)
            print("Выберите 1 или 2")
        except ValueError:
            print("Введите число")
            
            
def get_output_destination():
    while True:
        print("\nКуда вывести результаты?")
        print("1. На экран")
        print("2. В файл")
        choice = input("Ваш выбор (1-2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("Некорректный ввод")
        

def display_results(system_name, root, iterations, q):
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ РЕШЕНИЯ")
    print("=" * 60)
    print(f"Система:\n{system_name}")
    print(f"Коэффициент сходимости: q = {q:.6f}")
    print(f"\nНайденный корень:")
    print(f"x₁ = {root[0]:.12f}")
    print(f"x₂ = {root[1]:.12f}")
    print(f"Число итераций: {iterations}")
    print("=" * 60)

def read_from_keyboard():
    print("\nВведите начальное приближение и точность:")
    x1 = float(input("x1₀ = "))
    x2 = float(input("x2₀ = "))
    eps = float(input("ε = "))
    return x1, x2, eps


def read_from_file():
    filename = input("Введите имя файла: ").strip()
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if len(lines) < 3:
        raise ValueError("Недостаточно строк в файле")
    x1 = float(lines[0].strip())
    x2 = float(lines[1].strip())
    eps = float(lines[2].strip())
    return x1, x2, eps


def verify_solution(f1, f2, root, eps):
    x1, x2 = root

    res1 = abs(f1(x1, x2))
    res2 = abs(f2(x1, x2))

    is_correct = (res1 < 10 * eps) and (res2 < 10 * eps)

    return is_correct, (res1, res2)

def main():
    display_system()
    while True:
        try:
            choice = int(input("\nВыберите систему (1-2): "))
            if choice in SYSTEMS:
                break
            print("Введите число от 1 до 3")
        except ValueError:
            print("Введите корректное число")

    system = SYSTEMS[choice]

    input_source = get_input_source()

    if input_source == '1':
        x1_0, x2_0, eps = read_from_keyboard()
    else:
        x1_0, x2_0, eps = read_from_file()

    print("\nПроверка условия сходимости")
    converges, q = check(system, x1_0, x2_0)
    print(f"   q = {q:.4f}")

    if not converges:
        print("Условие сходимости не выполнено")
        return

    try:
        results = simple_iteration(
            system['g1'], system['g2'],
            x1_0, x2_0, eps
        )
        root = results['root']
        iterations = results['iterations']
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    print("Проверка правильности решения")
    is_correct, residuals = verify_solution(
        system['f1'],
        system['f2'],
        root,
        eps
    )

    if is_correct:
        print("Решение верное")
    else:
        print("Решение неточное")

    output_dest = get_output_destination()

    if output_dest in '1':
        display_results(system['name'], root, iterations, q)
    if output_dest in '2':
        save_results_to_file(
            system['name'], root, iterations,
            x1_0, x2_0, eps, q, is_correct
        )

    show_graph = input("\nПоказать график функции? (y/n): ").lower()
    if show_graph in 'y':
        try:
            plot_range = system.get('plot_range')
            plot_system(
                system['f1'], system['f2'],
                root, plot_range, system['name']
            )
        except Exception as e:
            print(f"Ошибка при построении графика: {e}")

    again = input("Продолжить работу с программой? (y/n): ").lower().strip()
    if again in 'y':
        main()
    else:
        print("\nПрограмма завершена\n")


if __name__ == "__main__":
    main()