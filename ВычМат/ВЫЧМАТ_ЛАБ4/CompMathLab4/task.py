import math
import sys
import matplotlib.pyplot as plt


def gauss(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]

    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[max_row][col]) < 1e-12:
            return None
        M[col], M[max_row] = M[max_row], M[col]

        pivot = M[col][col]
        M[col] = [v / pivot for v in M[col]]

        for row in range(n):
            if row == col:
                continue
            factor = M[row][col]
            M[row] = [M[row][j] - factor * M[col][j] for j in range(n + 1)]

    return [M[i][n] for i in range(n)]


def sums(xs, ys, max_pow):
    n = len(xs)
    sx = [sum(x ** k for x in xs) for k in range(max_pow + 1)]
    sxy = [sum((x ** k) * y for x, y in zip(xs, ys)) for k in range(max_pow + 1)]
    return n, sx, sxy


def deviation_S(ys, phi):
    return sum((p - y) ** 2 for p, y in zip(phi, ys))


def std_dev(ys, phi):
    return math.sqrt(deviation_S(ys, phi) / len(ys))


def r2_score(ys, phi):
    y_mean = sum(ys) / len(ys)
    ss_res = sum((y - p) ** 2 for y, p in zip(ys, phi))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    if abs(ss_tot) < 1e-15:
        return 1.0
    return 1.0 - ss_res / ss_tot


def pearson_r(xs, ys):
    n = len(xs)
    xm = sum(xs) / n
    ym = sum(ys) / n
    num = sum((x - xm) * (y - ym) for x, y in zip(xs, ys))
    denom = math.sqrt(sum((x - xm) ** 2 for x in xs) *
                      sum((y - ym) ** 2 for y in ys))
    if abs(denom) < 1e-15:
        return 0.0
    return num / denom


def interpret_pearson(r):
    ar = abs(r)
    if ar < 0.3:   return "слабая"
    if ar < 0.5:   return "умеренная"
    if ar < 0.7:   return "заметная"
    if ar < 0.9:   return "высокая"
    if ar < 1.0:   return "весьма высокая"
    return "строгая линейная функциональная"


def interpret_r2(r2):
    if r2 >= 0.95: return "высокая точность аппроксимации (модель хорошо описывает явление)"
    if r2 >= 0.75: return "удовлетворительная аппроксимация (модель в целом адекватно описывает явление)"
    if r2 >= 0.5:  return "слабая аппроксимация (модель слабо описывает явление)"
    return "точность аппроксимации недостаточна, модель требует изменения"


class ApproxResult:
    def __init__(self, name, formula, coeffs, phi, xs, ys):
        self.name = name
        self.formula = formula
        self.coeffs = coeffs
        self.phi = phi
        self.eps = [p - y for p, y in zip(phi, ys)]
        self.S = deviation_S(ys, phi)
        self.delta = std_dev(ys, phi)
        self.R2 = r2_score(ys, phi)
        self.xs = xs
        self.ys = ys


def linear(xs, ys):
    n, sx, sxy = sums(xs, ys, 2)
    A = [[sx[2], sx[1]], [sx[1], n]]
    b = [sxy[1], sxy[0]]
    sol = gauss(A, b)
    if sol is None:
        return None
    a, b_coef = sol
    phi = [a * x + b_coef for x in xs]
    return ApproxResult("Линейная", f"φ(x) = {a:.4f}·x + ({b_coef:.4f})",
                        {"a": a, "b": b_coef}, phi, xs, ys)


def quadratic(xs, ys):
    n, sx, sxy = sums(xs, ys, 4)
    A = [
        [n, sx[1], sx[2]],
        [sx[1], sx[2], sx[3]],
        [sx[2], sx[3], sx[4]],
    ]
    b = [sxy[0], sxy[1], sxy[2]]
    sol = gauss(A, b)
    if sol is None:
        return None
    a0, a1, a2 = sol
    phi = [a0 + a1 * x + a2 * x ** 2 for x in xs]
    return ApproxResult("Квадратичная",
                        f"φ(x) = {a0:.4f} + {a1:.4f}·x + ({a2:.4f})·x²",
                        {"a0": a0, "a1": a1, "a2": a2}, phi, xs, ys)


def cubic(xs, ys):
    n, sx, sxy = sums(xs, ys, 6)
    A = [
        [n, sx[1], sx[2], sx[3]],
        [sx[1], sx[2], sx[3], sx[4]],
        [sx[2], sx[3], sx[4], sx[5]],
        [sx[3], sx[4], sx[5], sx[6]],
    ]
    b = [sxy[0], sxy[1], sxy[2], sxy[3]]
    sol = gauss(A, b)
    if sol is None:
        return None
    a0, a1, a2, a3 = sol
    phi = [a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 for x in xs]
    return ApproxResult("Кубическая",
                        f"φ(x) = {a0:.4f} + {a1:.4f}·x + ({a2:.4f})·x² + ({a3:.4f})·x³",
                        {"a0": a0, "a1": a1, "a2": a2, "a3": a3}, phi, xs, ys)


def exponential(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if y > 0]
    if len(pairs) < 2:
        return None
    xs2 = [p[0] for p in pairs]
    # Y = ln(y)
    lny = [math.log(p[1]) for p in pairs]
    #ln(y) = b·x + ln(a)
    res = linear(xs2, lny)
    if res is None:
        return None
    b_coef = res.coeffs["a"]
    a = math.exp(res.coeffs["b"])
    #φ(x) = a·e^(b·x)
    phi = [a * math.exp(b_coef * x) for x in xs]
    return ApproxResult("Экспоненциальная",
                        f"φ(x) = {a:.4f}·e^({b_coef:.4f}·x)",
                        {"a": a, "b": b_coef}, phi, xs, ys)


def logarithmic(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x > 0]
    if len(pairs) < 2:
        return None
    # X = ln(x)
    lnx = [math.log(p[0]) for p in pairs]
    #y по ln(x)
    ys2 = [p[1] for p in pairs]
    res = linear(lnx, ys2)
    if res is None:
        return None
    a = res.coeffs["a"]
    b_coef = res.coeffs["b"]
    #φ(x) = a·ln(x) + b
    phi = []
    for x in xs:
        if x > 0:
            phi.append(a * math.log(x) + b_coef)
        else:
            phi.append(float("nan"))
    valid = [(p, y) for p, y in zip(phi, ys) if not math.isnan(p)]
    if not valid:
        return None
    phi_v = [v[0] for v in valid]
    ys_v = [v[1] for v in valid]
    eps = [p - y for p, y in zip(phi_v, ys_v)]
    S = sum(e ** 2 for e in eps)
    delta = math.sqrt(S / len(ys_v))
    R2 = r2_score(ys_v, phi_v)

    r = ApproxResult("Логарифмическая",
                     f"φ(x) = {a:.4f}·ln(x) + ({b_coef:.4f})",
                     {"a": a, "b": b_coef}, phi, xs, ys)

    r.eps = [p - y for p, y in zip(phi, ys)]
    r.S = S
    r.delta = delta
    r.R2 = R2
    return r


def power(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x > 0 and y > 0]
    if len(pairs) < 2:
        return None
    # X = ln(x)
    lnx = [math.log(p[0]) for p in pairs]
    # Y = ln(y)
    lny = [math.log(p[1]) for p in pairs]
    #ln(y) = b·ln(x) + ln(a)
    res = linear(lnx, lny)
    if res is None:
        return None
    b_coef = res.coeffs["a"]
    a = math.exp(res.coeffs["b"])
    #φ(x) = a·x ^ b
    phi = []
    for x in xs:
        if x > 0:
            phi.append(a * (x ** b_coef))
        else:
            phi.append(float("nan"))
    valid = [(p, y) for p, y in zip(phi, ys) if not math.isnan(p)]
    if not valid:
        return None
    phi_v = [v[0] for v in valid]
    ys_v = [v[1] for v in valid]
    S = sum((p - y) ** 2 for p, y in zip(phi_v, ys_v))
    delta = math.sqrt(S / len(ys_v))
    R2 = r2_score(ys_v, phi_v)

    r = ApproxResult("Степенная",
                     f"φ(x) = {a:.4f}·x^({b_coef:.4f})",
                     {"a": a, "b": b_coef}, phi, xs, ys)
    r.S = S
    r.delta = delta
    r.R2 = R2
    return r


def input_from_console():
    while True:
        try:
            n = int(input("Введите количество точек (8–12): "))
            if 8 <= n <= 12:
                break
            print("Ошибка: допустимо от 8 до 12 точек")
        except ValueError:
            print("Ошибка: введите целое число")

    xs, ys = [], []
    print("Введите значения x и y через пробел (по одной паре в строке):")
    for i in range(n):
        while True:
            try:
                line = input(f"  Точка {i + 1}: ").split()
                xs.append(float(line[0].replace(",", ".")))
                ys.append(float(line[1].replace(",", ".")))
                break
            except (ValueError, IndexError):
                print("  Ошибка. Введите два числа через пробел")
    return xs, ys


def input_from_file(path):
    xs, ys = [], []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.replace(",", ".").split()
            if len(parts) == 2:
                xs.append(float(parts[0]))
                ys.append(float(parts[1]))
    n = len(xs)
    if not (8 <= n <= 12):
        raise ValueError(f"Файл содержит {n} точек — допустимо от 8 до 12")
    return xs, ys


def validate_data(xs, ys):
    n = len(xs)
    if n != len(ys):
        raise ValueError("Количество x и y не совпадает")
    if not (8 <= n <= 12):
        raise ValueError(f"Допустимо от 8 до 12 точек, получено {n}")
    if len(set(xs)) != n:
        raise ValueError("Значения x должны быть уникальными")



def print_table(res: ApproxResult):
    header = f"{'i':>3} | {'xi':>8} | {'yi':>10} | {'φ(xi)':>10} | {'εi':>10}"
    print(header)
    print("─" * len(header))
    for i, (x, y, p, e) in enumerate(zip(res.xs, res.ys, res.phi, res.eps), 1):
        p_str = f"{p:10.6f}" if not math.isnan(p) else f"{'н/д':>10}"
        e_str = f"{e:10.6f}" if not math.isnan(e) else f"{'н/д':>10}"
        print(f"{i:>3} | {x:8.4f} | {y:10.6f} | {p_str} | {e_str}")


def print_result(res: ApproxResult, xs, ys, print_pearson=False):
    print(f"\n{'═' * 80}")
    print(f"  {res.name.upper()} АППРОКСИМАЦИЯ")
    print(f"  Формула: {res.formula}")
    print()
    print("  Коэффициенты:")
    for k, v in res.coeffs.items():
        print(f"    {k} = {v:.6f}")
    print()
    print_table(res)
    print()
    print(f"  S  (мера отклонения)         = {res.S:.6f}")
    print(f"  δ  (среднеквадратичное откл.) = {res.delta:.6f}")
    print(f"  R² (коэффициент детерминации) = {res.R2:.6f}")
    print(f"  Интерпретация R²: {interpret_r2(res.R2)}")

    if print_pearson:
        r = pearson_r(xs, ys)
        print()
        print(f"  Коэффициент корреляции Пирсона r = {r:.6f}")
        print(f"  Интерпретация: связь {interpret_pearson(r)}")


def plot_results(results, xs, ys, best):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    x_min = min(xs)
    x_max = max(xs)
    x_range = x_max - x_min
    x_min_plot = x_min - 0.05 * x_range
    x_max_plot = x_max + 0.05 * x_range

    ax.scatter(xs, ys, color='black', s=60, zorder=5, label='Исходные данные',
               edgecolors='white', linewidth=1.5)

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    for idx, res in enumerate(results):
        x_plot = [x_min_plot + i * (x_max_plot - x_min_plot) / 199 for i in range(200)]
        y_plot = []
        for x in x_plot:
            try:
                y_val = _eval_approx(res, x)
                y_plot.append(y_val if y_val is not None and not math.isnan(y_val) else None)
            except:
                y_plot.append(None)

        ax.plot(x_plot, y_plot, color=colors[idx % len(colors)],
                linewidth=2, label=res.name, zorder=3)

    ax.set_xlim(x_min_plot, x_max_plot)

    ax.margins(y=0.1)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title('Аппроксимация функции методом наименьших квадратов',
                 fontsize=13, fontweight='bold', pad=15)

    ax.legend(loc='best', fontsize=9)
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.show()


def _eval_approx(res: ApproxResult, x):
    c = res.coeffs
    name = res.name
    if name == "Линейная":
        return c["a"] * x + c["b"]
    if name == "Квадратичная":
        return c["a0"] + c["a1"] * x + c["a2"] * x ** 2
    if name == "Кубическая":
        return c["a0"] + c["a1"] * x + c["a2"] * x ** 2 + c["a3"] * x ** 3
    if name == "Экспоненциальная":
        return c["a"] * math.exp(c["b"] * x)
    if name == "Логарифмическая":
        if x <= 0:
            return None
        return c["a"] * math.log(x) + c["b"]
    if name == "Степенная":
        if x <= 0:
            return None
        return c["a"] * (x ** c["b"])
    return None


def save_to_file(path, results, xs, ys, best):
    import io, sys
    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf

    print("Аппроксимация функции методом наименьших квадратов")
    for res in results:
        print_result(res, xs, ys, print_pearson=(res.name == "Линейная"))

    print(f"\n{'═' * 80}")
    print(f"  НАИЛУЧШАЯ АППРОКСИМАЦИЯ: {best.name.upper()}")
    print(f"     Формула : {best.formula}")
    print(f"     δ (min) = {best.delta:.6f}")
    print(f"     R²      = {best.R2:.6f}  →  {interpret_r2(best.R2)}")

    sys.stdout = old_stdout
    with open(path, "w", encoding="utf-8") as f:
        f.write(buf.getvalue())
    print(f"\n  Результаты сохранены в файл: {path}")


def main():
    print("АППРОКСИМАЦИЯ МНК")
    while True:
        choice = input("\n1 - ввод с консоли\n2 -  ввод с файла\nВаш выбор: ").strip()
        if choice == "1":
            xs, ys = input_from_console()
            break
        elif choice == "2":
            path = input("Путь к файлу: ").strip()
            try:
                xs, ys = input_from_file(path)
                break
            except (FileNotFoundError, ValueError) as e:
                print(f"Ошибка: {e}")
                sys.exit(1)
        else:
            print("Неверный выбор. Введите 1/2")

    try:
        validate_data(xs, ys)
    except ValueError as e:
        print(f"\nОшибка в данных: {e}")
        sys.exit(1)

    print(f"\n  Загружено {len(xs)} точек")
    print(f"  x: {[round(v, 4) for v in xs]}")
    print(f"  y: {[round(v, 6) for v in ys]}")

    funcs = [
        ("Линейная", linear),
        ("Квадратичная", quadratic),
        ("Кубическая", cubic),
        ("Экспоненциальная", exponential),
        ("Логарифмическая", logarithmic),
        ("Степенная", power),
    ]

    results = []
    for name, func in funcs:
        try:
            res = func(xs, ys)
            if res is None:
                print(f"\n  [{name}] — не удалось")
            else:
                results.append(res)
        except Exception as e:
            print(f"\n  [{name}] — ошибка: {e}")

    if not results:
        print("Ни одна аппроксимация не была успешно построена")
        sys.exit(1)

    for res in results:
        print_result(res, xs, ys, print_pearson=(res.name == "Линейная"))

    best = min(results, key=lambda r: r.delta)
    print(f"\n{'═' * 80}")
    print(f"  НАИЛУЧШАЯ АППРОКСИМАЦИЯ: {best.name.upper()}")
    print(f"     Формула : {best.formula}")
    print(f"     δ (min) = {best.delta:.6f}")
    print(f"     R²      = {best.R2:.6f}  →  {interpret_r2(best.R2)}")

    plot_results(results, xs, ys, best)

    try:
        save_ans = input("\nСохранить результаты в файл? [y/n]: ").strip().lower()
        if save_ans == "y":
            out_path = input("Путь к файлу (Enter = results.txt): ").strip() or "results.txt"
            save_to_file(out_path, results, xs, ys, best)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
