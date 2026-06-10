import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def f1(x):
    return -1.5 * x ** 3 + 2.3 * x ** 2 + 4.1 * x - 3.7


def df1(x):
    return -4.5 * x ** 2 + 4.6 * x + 4.1


def d2f1(x):
    return -9.0 * x + 4.6


def f2(x):
    return x ** 3 - 2.15 * x ** 2 - 1.8 * x + 2.4


def df2(x):
    return 3 * x ** 2 - 4.3 * x - 1.8


def d2f2(x):
    return 6 * x - 4.3


def f3(x):
    return math.exp(x) - 2.5 * x - 1.2


def df3(x):
    return math.exp(x) - 2.5


def d2f3(x):
    return math.exp(x)


def f4(x):
    return math.sin(x) + 0.5 * x - 1.3


def df4(x):
    return math.cos(x) + 0.5


def d2f4(x):
    return -math.sin(x)


EQUATIONS = {
    1: {'name': '-1.5x³ + 2.3x² + 4.1x - 3.7', 'f': f1, 'df': df1, 'd2f': d2f1},
    2: {'name': 'x³ - 2.15x² - 1.8x + 2.4', 'f': f2, 'df': df2, 'd2f': d2f2},
    3: {'name': 'eˣ - 2.5x - 1.2', 'f': f3, 'df': df3, 'd2f': d2f3},
    4: {'name': 'sin(x) + 0.5x - 1.3', 'f': f4, 'df': df4, 'd2f': d2f4}
}


def half_division_method(func, a, b, epsilon, max_iterations=1000):
    fa = func(a)
    fb = func(b)

    if fa * fb > 0:
        raise ValueError(f"На интервале [{a}, {b}] нет корня (знаки на концах одинаковы)")

    iteration = 0
    while (b - a) > epsilon and iteration < max_iterations:
        iteration += 1
        x = (a + b) / 2
        fx = func(x)

        if abs(fx) < epsilon:
            return {'root': x, 'f_root': fx, 'iterations': iteration}

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    x_final = (a + b) / 2
    return {'root': x_final, 'f_root': func(x_final), 'iterations': iteration}


def newton_method(func, deriv_func, x0, epsilon, max_iterations=1000):
    x = x0
    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        fx = func(x)
        dfx = deriv_func(x)

        if abs(dfx) < 1e-12:
            raise ValueError(f"Производная близка к нулю (f'({x:.4f})={dfx:.4e}). Метод не сходится")

        x_new = x - fx / dfx

        if abs(x_new - x) < epsilon:
            return {'root': x_new, 'f_root': func(x_new), 'iterations': iteration}

        x = x_new

    raise ValueError(f"Не достигнута точность за {max_iterations} итераций. Последнее x={x}")


def simple_iteration_method(func, deriv_func, a, b, epsilon, x0, max_iterations=1000):
    n_samples = 1000
    x_samples = np.linspace(a, b, n_samples)

    deriv_values = [deriv_func(x) for x in x_samples]
    abs_deriv_values = [abs(d) for d in deriv_values]

    M = max(abs_deriv_values)

    if M == 0:
        raise ValueError("Производная равна нулю на интервале. Метод неприменим")

    signs = [1 if d >= 0 else -1 for d in deriv_values]
    if len(set(signs)) > 1:
        raise ValueError("Производная меняет знак на интервале")
    sign_df = signs[0]
    lambda_val = -sign_df / M

    phi_deriv_values = [abs(1 + lambda_val * d) for d in deriv_values]
    q = max(phi_deriv_values)

    if q >= 1:
        raise ValueError(f"\nДостаточное условие сходимости не выполняется (q = {q:.4f} >= 1)")

    x = x0
    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        x_new = x + lambda_val * func(x)

        if abs(x_new - x) < epsilon:
            return {'root': x_new, 'f_root': func(x_new), 'iterations': iteration}

        x = x_new

    raise ValueError(f"Не достигнута точность за {max_iterations} итераций. Последнее x={x}")

def choose_newton_start(func, second_deriv_func, a, b):

    fa = func(a)
    fb = func(b)
    d2fa = second_deriv_func(a)
    d2fb = second_deriv_func(b)

    if fa * d2fa > 0:
        return a
    elif fb * d2fb > 0:
        return b
    else:
        return (a + b) / 2


def choose_iteration_start(func, a, b):
    if abs(func(a)) < abs(func(b)):
        return a
    else:
        return b


def check_root(func, a, b, num_points=100):
    x_values = np.linspace(a, b, num_points)
    y_values = [func(x) for x in x_values]

    sign_changes = 0
    for i in range(len(y_values) - 1):
        if y_values[i] * y_values[i + 1] < 0:
            sign_changes += 1
        elif abs(y_values[i]) < 1e-10:
            sign_changes += 1

    if sign_changes == 0:
        return False, 0, "Корней на интервале не обнаружено"
    elif sign_changes > 1:
        return False, sign_changes, f"На интервале обнаружено {sign_changes} корней (рекомендуется сузить интервал)"
    else:
        return True, sign_changes, "Обнаружен 1 корень"


def plot_function(func, a, b, root=None):
    x = np.linspace(a, b, 1000)
    y = [func(xi) for xi in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

    if root is not None:
        plt.plot(root, func(root), 'ro', markersize=10, label=f'Корень: {root:.6f}')

    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции')
    plt.legend()
    plt.show()


def display_equations():
    print("\n" + "=" * 60)
    print("ДОСТУПНЫЕ УРАВНЕНИЯ:")
    print("=" * 60)
    for key, value in EQUATIONS.items():
        print(f"{key}. f(x) = {value['name']}")
    print("=" * 60)


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


def read_from_keyboard():
    while True:
        try:
            print("a < b")
            a = float(input("Введите левую границу интервала a: "))
            b = float(input("Введите правую границу интервала b: "))
            if a >= b:
                print("a должно быть меньше b")
                continue
            epsilon = float(input("Введите точность ε (например, 0.001): "))
            if epsilon <= 0:
                print("Точность должна быть положительной")
                continue
            return a, b, epsilon
        except ValueError:
            print("Введите корректные числовые значения")


def read_from_file():
    while True:
        filename = input("Введите имя файла: ").strip()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) < 3:
                    raise IndexError("Недостаточно строк в файле")
                a = float(lines[0].strip())
                b = float(lines[1].strip())
                epsilon = float(lines[2].strip())
                if a >= b or epsilon <= 0:
                    print("В файле некорректные данные")
                    continue
                return a, b, epsilon
        except FileNotFoundError:
            print("Файл не найден")
        except (ValueError, IndexError):
            print("Ожидается 3 строки: a, b, epsilon")


def get_output_destination():
    while True:
        print("\nКуда вывести результаты?")
        print("1. На экран")
        print("2. В файл")
        choice = input("Ваш выбор (1-2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("Некорректный ввод")


def save_results_to_file(results, equation_name, method_name, a, b, epsilon):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("РЕЗУЛЬТАТЫ РЕШЕНИЯ НЕЛИНЕЙНОГО УРАВНЕНИЯ\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Уравнение: {equation_name}\n")
        f.write(f"Метод: {method_name}\n")
        f.write(f"Интервал изоляции: [{a}, {b}]\n")
        f.write(f"Точность: ε = {epsilon}\n")
        f.write(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n\n")
        f.write("-" * 60 + "\n")
        f.write("РЕШЕНИЕ:\n")
        f.write("-" * 60 + "\n")
        f.write(f"Найденный корень: x = {results['root']:.10f}\n")
        f.write(f"Значение функции: f(x) = {results['f_root']:.10e}\n")
        f.write(f"Число итераций: {results['iterations']}\n")
    print(f"\nРезультаты сохранены в файл: {filename}")


def display_results(results, equation_name, method_name):
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ РЕШЕНИЯ")
    print("=" * 60)
    print(f"Уравнение: {equation_name}")
    print(f"Метод: {method_name}")
    print(f"Найденный корень: x = {results['root']:.10f}")
    print(f"Значение функции: f(x) = {results['f_root']:.10f}")
    print(f"Число итераций: {results['iterations']}")


def main():
    display_equations()
    while True:
        try:
            eq_choice = int(input("\nВыберите номер уравнения (1-4): "))
            if eq_choice in EQUATIONS:
                break
            print("Выберите число от 1 до 4")
        except ValueError:
            print("Введите число")

    selected_eq = EQUATIONS[eq_choice]

    print("\nВыберите метод решения:")
    print("1. Метод половинного деления")
    print("2. Метод Ньютона")
    print("3. Метод простых итераций")
    while True:
        try:
            method_choice = int(input("Ваш выбор (1-3): "))
            if method_choice in [1, 2, 3]:
                break
            print("Выберите 1, 2 или 3")
        except ValueError:
            print("Введите число")

    input_source = get_input_source()
    if input_source == '1':
        a, b, epsilon = read_from_keyboard()
    else:
        a, b, epsilon = read_from_file()

    print("=" * 60)
    print("ИСХОДНЫЕ ДАННЫЕ")
    print("=" * 60)
    print(f"Выбрано: f(x) = {selected_eq['name']}")
    print(f"Интервал изоляции: [{a}, {b}]")
    print(f"Точность: ε = {epsilon}")
    print("=" * 60)

    print("\nПроверка наличия корня на интервале")
    exists, count, message = check_root(selected_eq['f'], a, b)
    print(message)

    if not exists:
        print("\nПрограмма завершена. Введите корректный интервал")
        return

    x0 = None
    method_name = ""
    results = None

    try:
        if method_choice == 1:
            results = half_division_method(selected_eq['f'], a, b, epsilon)
            method_name = "Метод половинного деления"

        elif method_choice == 2:
            x0 = choose_newton_start(selected_eq['f'], selected_eq['d2f'], a, b)
            print(f"Автоматически выбрано начальное приближение: x0 = {x0:.4f}")
            results = newton_method(selected_eq['f'], selected_eq['df'], x0, epsilon)
            method_name = "Метод Ньютона"

        elif method_choice == 3:
            x0 = choose_iteration_start(selected_eq['f'], a, b)
            print(f"Автоматически выбрано начальное приближение: x0 = {x0:.4f}")

            print("Проверка условия сходимости метода простой итерации")
            results = simple_iteration_method(selected_eq['f'], selected_eq['df'], a, b, epsilon, x0)
            method_name = "Метод простых итераций"

        output_dest = get_output_destination()
        if output_dest == '1':
            display_results(results, selected_eq['name'], method_name)
        else:
            save_results_to_file(results, selected_eq['name'], method_name, a, b, epsilon)

        show_graph = input("\nПоказать график функции? (y/n): ").lower()
        if show_graph in 'y':
            plot_function(selected_eq['f'], a, b, results['root'])

    except ValueError as e:
        print(f"\nОшибка при решении: {e}")
    except RuntimeError as e:
        print(f"\nОшибка выполнения: {e}")

    again = input("\nПродолжить работу с программой? (y/n): ").lower()
    if again in 'y':
        main()
    else:
        print("\nПрограмма завершена")


if __name__ == "__main__":
    main()