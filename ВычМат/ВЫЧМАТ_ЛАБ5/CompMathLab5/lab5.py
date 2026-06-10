import math
import matplotlib.pyplot as plt
import numpy as np

def print_separator(char="═", width=70):
    print(char * width)

def print_header(title):
    print(f"  {title}")
    print_separator()

def print_table(xs, ys, title="Таблица узлов"):
    print(f"\n{'─'*40}")
    print(f"  {title}")
    print(f"{'─'*40}")
    print(f"{'i':>4} | {'x':>12} | {'y':>14}")
    print(f"{'─'*4}-+-{'─'*12}-+-{'─'*14}")
    for i, (x, y) in enumerate(zip(xs, ys)):
        print(f"{i:>4} | {x:>12.6f} | {y:>14.6f}")
    print(f"{'─'*40}")


def build_finite_differences(ys):
    n = len(ys)
    delta = [list(ys)]
    for k in range(1, n):
        prev = delta[k - 1]
        row = [prev[i + 1] - prev[i] for i in range(len(prev) - 1)]
        if not row:
            break
        delta.append(row)
    return delta

def print_finite_diff_table(xs, delta):
    n = len(xs)
    max_order = len(delta) - 1
    print(f"\n{'─'*10}  Таблица конечных разностей  {'─'*10}")
    header = f"{'i':>3}  {'x':>10}  {'y':>12}"
    for k in range(1, max_order + 1):
        header += f"  {'Δ^'+str(k)+'y':>12}"
    print(header)
    print("─" * (40 + 14 * max_order))
    for i in range(n):
        row = f"{i:>3}  {xs[i]:>10.5f}  {delta[0][i]:>12.6f}"
        for k in range(1, max_order + 1):
            if i < len(delta[k]):
                row += f"  {delta[k][i]:>12.6f}"
            else:
                row += f"  {'':>12}"
        print(row)
    print()

def lagrange(xs, ys, x):
    n = len(xs)
    result = 0.0
    for i in range(n):
        li = 1.0
        for j in range(n):
            if j != i:
                li *= (x - xs[j]) / (xs[i] - xs[j])
        result += ys[i] * li
    return result


def newton_forward(xs, delta, x):
    h = xs[1] - xs[0]
    t = (x - xs[0]) / h
    n = len(xs) - 1
    result = delta[0][0]
    t_product = 1.0
    factorial = 1
    for k in range(1, n + 1):
        t_product *= (t - (k - 1))
        factorial *= k
        if k < len(delta) and delta[k]:
            result += t_product / factorial * delta[k][0]
    return result

def newton_backward(xs, delta, x):
    h = xs[1] - xs[0]
    n = len(xs) - 1
    t = (x - xs[n]) / h
    result = delta[0][n]
    t_product = 1.0
    factorial = 1
    for k in range(1, n + 1):
        t_product *= (t + (k - 1))
        factorial *= k
        if k < len(delta) and len(delta[k]) > n - k:
            result += t_product / factorial * delta[k][n - k]
    return result

def newton_finite_verbose(xs, delta, x):
    h = xs[1] - xs[0]
    x_mid = (xs[0] + xs[-1]) / 2

    if x <= x_mid:
        t = (x - xs[0]) / h
        print(f"\n  Ньютон (вперёд): t = {t:.4f}")
        result = newton_forward(xs, delta, x)
    else:
        n = len(xs) - 1
        t = (x - xs[n]) / h
        print(f"\n  Ньютон (назад): t = {t:.4f}")
        result = newton_backward(xs, delta, x)

    print(f"  N(x) = {result:.6f}")
    return result

def _find_center(xs, x):
    idx = 0
    min_dist = abs(x - xs[0])
    for i in range(1, len(xs)):
        d = abs(x - xs[i])
        if d < min_dist:
            min_dist = d
            idx = i
    return idx

def gauss_forward(xs, delta, x):
    n = len(xs) - 1
    h = xs[1] - xs[0]
    c = _find_center(xs, x)
    if c > n // 2:
        c = n // 2
    t = (x - xs[c]) / h
    result = delta[0][c]
    product = 1.0
    factorial = 1
    for k in range(1, len(delta)):
        product *= t if k == 1 else (t - k // 2) if k % 2 == 0 else (t + k // 2)
        factorial *= k
        idx = c - k // 2
        if 0 <= idx < len(delta[k]):
            result += product / factorial * delta[k][idx]
    return result

def gauss_backward(xs, delta, x):
    n = len(xs) - 1
    h = xs[1] - xs[0]
    c = _find_center(xs, x)
    if c < (n + 1) // 2:
        c = (n + 1) // 2
    if c > n:
        c = n
    t = (x - xs[c]) / h
    result = delta[0][c]
    product = 1.0
    factorial = 1
    for k in range(1, len(delta)):
        product *= t if k == 1 else (t + k // 2) if k % 2 == 0 else (t - k // 2)
        factorial *= k
        idx = c - (k + 1) // 2
        if 0 <= idx < len(delta[k]):
            result += product / factorial * delta[k][idx]
    return result

def gauss_verbose(xs, delta, x):
    n = len(xs) - 1
    h = xs[1] - xs[0]
    c = n // 2
    t = (x - xs[c]) / h
    print(f"\n  Многочлен Гаусса для x = {x}")
    print(f"  Центральный узел: x0 = {xs[c]:.5f}, t = {t:.4f}")

    if t >= 0:
        print("  Формула: 1-я (t ≥ 0)")
        result = gauss_forward(xs, delta, x)
    else:
        print("  Формула: 2-я (t < 0)")
        result = gauss_backward(xs, delta, x)

    print(f"  G(x) = {result:.6f}")
    return result

def _avg_diff(delta, k, idx_lo, idx_hi):
    lo = delta[k][idx_lo] if 0 <= idx_lo < len(delta[k]) else None
    hi = delta[k][idx_hi] if 0 <= idx_hi < len(delta[k]) else None
    if lo is not None and hi is not None:
        return (lo + hi) / 2
    return lo if lo is not None else (hi if hi is not None else 0.0)

def stirling(xs, delta, x):

    h = xs[1] - xs[0]
    c = (len(xs) - 1) // 2
    t = (x - xs[c]) / h
    t2 = t * t

    result = delta[0][c]
    odd_num = t
    denom = 1

    for m in range(1, len(delta)):
        k_odd, k_even = 2 * m - 1, 2 * m

        if k_odd < len(delta):
            result += odd_num / denom * _avg_diff(delta, k_odd, c - m, c - m + 1)

        if k_even < len(delta):
            idx = c - m
            if 0 <= idx < len(delta[k_even]):
                result += (odd_num * t) / (denom * k_even) * delta[k_even][idx]

        odd_num *= (t2 - m * m)
        denom *= k_even * (k_even + 1)

    return result

def bessel(xs, delta, x):
    h = xs[1] - xs[0]
    c = (len(xs) - 1) // 2
    t = (x - xs[c]) / h

    y1 = delta[0][c + 1] if c + 1 < len(delta[0]) else delta[0][c]
    result = (delta[0][c] + y1) / 2

    odd_num = (t - 0.5)
    denom = 1

    for m in range(1, len(delta)):
        k_odd, k_even = 2 * m - 1, 2 * m

        if k_odd < len(delta):
            idx = c - m + 1
            if 0 <= idx < len(delta[k_odd]):
                result += odd_num / denom * delta[k_odd][idx]

        if k_even < len(delta):
            result += (odd_num * t) / (denom * k_even) * _avg_diff(delta, k_even, c - m, c - m + 1)

        odd_num *= (t - m) * (t + m - 1)
        denom *= k_even * (k_even + 1)

    return result

PRESET_FUNCTIONS = {
    "1": ("sin(x)", math.sin),
    "2": ("cos(x)", math.cos),
    "3": ("exp(x)", math.exp),
    "4": ("ln(x)",  math.log),
    "5": ("x^2",   lambda x: x ** 2),
}


def input_manual():
    while True:
        try:
            print("\n Введите количество узлов:")
            n_str = input("  n = ").strip()
            if not n_str:
                print("Ввод не может быть пустым")
                continue
            n = int(n_str)
            if n < 2:
                print("Количество узлов должно быть ≥ 2")
                continue
            break
        except ValueError:
            print("Введите целое число")

    xs, ys = [], []
    print("  Введите пары (x y) через пробел:")

    for i in range(n):
        while True:
            try:
                raw = input(f"  Узел {i}: ").strip()
                if not raw:
                    print("Ввод не может быть пустым")
                    continue

                parts = raw.split()
                if len(parts) != 2:
                    print("Введите ровно два значения через пробел (x y)")
                    continue

                x_val = float(parts[0])
                y_val = float(parts[1])

                xs.append(x_val)
                ys.append(y_val)
                break

            except ValueError:
                print("Значения должны быть корректными числами (целыми или дробными)")

    return xs, ys


def input_from_file():
    while True:
        path = input("  Путь к файлу: ").strip()
        if not path:
            print("Путь не может быть пустым")
            continue

        xs, ys = [], []
        parse_error = False

        try:
            with open(path, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue

                    parts = line.split()
                    if len(parts) != 2:
                        print(f"Строка {line_num}: нужно ровно 2 значения (x y), найдено {len(parts)}")
                        parse_error = True
                        break

                    xs.append(float(parts[0]))
                    ys.append(float(parts[1]))

        except FileNotFoundError:
            print("Файл не найден. Проверьте путь и имя файла")
            continue
        except PermissionError:
            print("Нет прав на чтение файла")
            continue
        except ValueError:
            print(f"Строка {line_num}: значения должны быть корректными числами (например, 1.5 или 2.3e-4)")
            continue
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            continue

        if parse_error:
            continue

        if len(xs) < 2:
            print("В файле должно быть минимум 2 строки с данными (не считая комментариев)")
            continue

        print(f"Успешно загружено {len(xs)} узлов из файла")
        return xs, ys

def input_from_function():
    while True:
        print("\n  Выберите функцию:")
        for k, (name, _) in PRESET_FUNCTIONS.items():
            print(f"    {k}. {name}")
        choice = input("  Функция: ").strip()
        if choice in PRESET_FUNCTIONS:
            fname, func = PRESET_FUNCTIONS[choice]
            break
        print("Некорректный выбор. Доступные варианты:", ", ".join(PRESET_FUNCTIONS.keys()))

    while True:
        try:
            a = float(input("  Начало отрезка a: ").strip())
            b = float(input("  Конец отрезка b: ").strip())
            if a >= b:
                print("a должно быть строго меньше b (иначе шаг сетки ≤ 0)")
                continue
            break
        except ValueError:
            print("Введите корректные числа для a и b")

    while True:
        try:
            n_str = input("Количество узлов (≥ 2): ").strip()
            if not n_str:
                print("Ввод не может быть пустым.")
                continue
            n = int(n_str)
            if n < 2:
                print("Количество узлов должно быть ≥ 2")
                continue
            break
        except ValueError:
            print("Введите целое число")

    h = (b - a) / (n - 1)
    xs = [a + i * h for i in range(n)]
    ys = [func(x) for x in xs]
    print(f"\n Сгенерированы узлы для f(x) = {fname}")
    return xs, ys, func, fname

def validate_data(xs, ys):
    if len(xs) != len(ys):
        raise ValueError("Количество x и y должно совпадать")
    for i in range(len(xs) - 1):
        if xs[i] >= xs[i + 1]:
            raise ValueError("Значения x должны строго возрастать")
    h0 = xs[1] - xs[0]
    for i in range(1, len(xs) - 1):
        if abs((xs[i + 1] - xs[i]) - h0) > 1e-9:
            raise ValueError("Для Ньютона (конечные разности) и Гаусса "
                             "требуется равномерная сетка узлов")
    return True

def print_comparison(results, x):
    print(f"\n{'─'*45}")
    print(f"  Сравнение методов для x = {x}")
    print(f"{'─'*45}")
    ref = next(iter(results.values()))
    for method, val in results.items():
        print(f"  {method:<20}: {val:>12.6f}  (|Δ|={abs(val - ref):.2e})")
    print(f"{'─'*45}")

def plot_interpolation(xs, ys, delta, x_queries=None, true_func=None, true_fname=None):
    n_nodes = len(xs)
    h = xs[1] - xs[0]
    x_mid = (xs[0] + xs[-1]) / 2

    x_dense = np.linspace(xs[0], xs[-1], 400)

    newton_vals = []
    gauss_vals  = []
    for xv in x_dense:
        if xv <= x_mid:
            newton_vals.append(newton_forward(xs, delta, xv))
        else:
            newton_vals.append(newton_backward(xs, delta, xv))

        c = n_nodes // 2
        t = (xv - xs[c]) / h
        if t >= 0:
            gauss_vals.append(gauss_forward(xs, delta, xv))
        else:
            gauss_vals.append(gauss_backward(xs, delta, xv))

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#F7F9FC")
    ax.set_facecolor("#F7F9FC")

    ax.plot(x_dense, newton_vals,
            color="#1B6CA8", linewidth=2.2, linestyle="-",
            label="Многочлен Ньютона", zorder=3)

    ax.plot(x_dense, gauss_vals,
            color="#E07B2A", linewidth=2.2, linestyle="--",
            label="Многочлен Гаусса", zorder=4)

    if true_func is not None:
        true_vals = [true_func(xv) for xv in x_dense]
        label_true = f"Истинная функция f(x) = {true_fname}" if true_fname else "Истинная функция"
        ax.plot(x_dense, true_vals,
                color="#2CA02C", linewidth=2.5, linestyle=(0, (4, 2)),
                label=label_true, zorder=5)

    ax.scatter(xs, ys,
               color="#1B6CA8", edgecolors="#0D3B6E",
               s=80, zorder=5, label="Узлы интерполяции")

    if x_queries:
        for xq in x_queries:
            if xs[0] <= xq <= xs[-1]:
                yq = lagrange(xs, ys, xq)
                ax.scatter([xq], [yq],
                           marker="*", s=220,
                           color="#D62839", edgecolors="#8B0000",
                           zorder=6, label=f"x* = {xq}")
                ax.axvline(xq, color="#D62839", linewidth=0.8,
                           linestyle=":", alpha=0.6)

    ax.set_xlabel("x", fontsize=13, labelpad=8)
    ax.set_ylabel("y", fontsize=13, labelpad=8)
    title_suffix = f"f(x) = {true_fname}" if true_fname else "табличные данные"
    ax.set_title(f"Интерполяция функции ({title_suffix})",
                 fontsize=14, fontweight="bold", pad=14)

    handles, labels = ax.get_legend_handles_labels()
    seen = {}
    uniq_h, uniq_l = [], []
    for h_, l_ in zip(handles, labels):
        if l_ not in seen:
            seen[l_] = True
            uniq_h.append(h_)
            uniq_l.append(l_)
    ax.legend(uniq_h, uniq_l, fontsize=10, framealpha=0.9, loc="best")

    ax.tick_params(labelsize=10)
    plt.tight_layout()
    plt.show()

def get_data_source():
    valid_choices = ["1", "2", "3"]
    choice_descriptions = {
        "1": "Ввод с клавиатуры",
        "2": "Загрузка из файла",
        "3": "Встроенная функция"
    }

    while True:
        print("\n  Источник данных:")
        for key in valid_choices:
            print(f"    {key}. {choice_descriptions[key]}")

        choice = input("  Выбор: ").strip()

        if not choice:
            print("Ввод не может быть пустым. Попробуйте ещё раз")
            continue

        if choice in valid_choices:
            if choice == "1":
                xs, ys = input_manual()
                return xs, ys, None, None
            elif choice == "2":
                xs, ys = input_from_file()
                return xs, ys, None, None
            elif choice == "3":
                xs, ys, func, fname = input_from_function()
                return xs, ys, func, fname
        else:
            print("Некорректный выбор. Доступные варианты: 1,2,3")

def main():
    print_header("Интерполяция функции")
    print("Методы: Лагранж | Ньютон (конечные разности) | Гаусс")
    print("Дополнительно: Стирлинг | Бессель")

    while True:
        try:
            xs, ys, true_func, true_fname = get_data_source()
            validate_data(xs, ys)
            break
        except Exception as e:
            print(f"\n Неожиданная ошибка: {e}")
            print("  Попробуйте ещё раз\n")

    print_table(xs, ys, "Исходные данные")

    delta = build_finite_differences(ys)
    print_finite_diff_table(xs, delta)

    print("\n  Введите точку интерполяции x* (или несколько через пробел):")
    while True:
        try:
            raw = input("  x* = ").strip()
            if not raw:
                print("Ввод не может быть пустым")
                continue
            points = [float(v) for v in raw.split()]
            break
        except ValueError:
            print("Введите корректные числа через пробел")

    for x_star in points:
        print_separator("─", 70)
        print(f"\n Интерполяция в точке x* = {x_star}")
        print_separator("─", 70)

        if x_star < xs[0] or x_star > xs[-1]:
            print("x* вне диапазона узлов — экстраполяция")

        h = xs[1] - xs[0]
        c = (len(xs) - 1) // 2
        t = (x_star - xs[c]) / h
        x_mid = (xs[0] + xs[-1]) / 2
        results = {}

        print("\n  ── Метод Лагранжа")
        results["Лагранж"] = lagrange(xs, ys, x_star)
        print(f"  L(x) = {results['Лагранж']:.6f}")

        print("\n  ── Метод Ньютона (конечные разности)")
        newton_key = "Ньютон (вперёд)" if x_star <= x_mid else "Ньютон (назад)"
        results[newton_key] = newton_finite_verbose(xs, delta, x_star)

        print("\n  ── Метод Гаусса")
        gauss_key = "Гаусс (1-я)" if t >= 0 else "Гаусс (2-я)"
        results[gauss_key] = gauss_verbose(xs, delta, x_star)

        if abs(t) <= 0.25:
            print("\n  ── Формула Стирлинга (|t| ≤ 0.25)")
            results["Стирлинг"] = stirling(xs, delta, x_star)
            print(f"  S(x) = {results['Стирлинг']:.6f}")
        else:
            print(f"\n  [Стирлинг пропущен: |t|={abs(t):.3f} > 0.25]")

        if 0.25 <= abs(t) <= 0.75:
            print("\n  ── Формула Бесселя (0.25 ≤ |t| ≤ 0.75)")
            results["Бессель"] = bessel(xs, delta, x_star)
            print(f"  B(x) = {results['Бессель']:.6f}")
        else:
            print(f"  [Бессель пропущен: |t|={abs(t):.3f} вне (0.25, 0.75)]")

        print_comparison(results, x_star)

    plot_interpolation(xs, ys, delta, x_queries=points, true_func=true_func, true_fname=true_fname)

    print("  Работа завершена")

if __name__ == "__main__":
    main()
