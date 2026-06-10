import math

def f1(x):
    return x ** 2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(x)

def f4(x):
    return 1 / x ** 2

def f5(x):
    return math.log(x)

functions = [f1, f2, f3, f4, f5]

def rectangle(func, a, b, n, mode="middle"):
    h = (b - a) / n
    result = 0
    if mode == "left":
        for i in range(n):
            result += func(a + i * h)
    elif mode == "right":
        for i in range(1, n + 1):
            result += func(a + i * h)
    else:
        for i in range(n):
            result += func(a + (i + 0.5) * h)
    result *= h
    return result

def trapezoid(func, a, b, n):
    h = (b - a) / n
    result = (func(a) + func(b)) / 2
    for i in range(1, n):
        result += func(a + i * h)
    result *= h
    return result

def simpson(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n):
        coef = 3 + (-1) ** (i + 1)
        result += coef * func(a + i * h)
    result *= h / 3
    return result

methods = {
    "Метод левых прямоугольников": lambda f, a, b, n: rectangle(f, a, b, n, mode="left"),
    "Метод правых прямоугольников": lambda f, a, b, n: rectangle(f, a, b, n, mode="right"),
    "Метод средних прямоугольников": rectangle,
    "Метод трапеций": trapezoid,
    "Метод Симпсона": simpson
}

def compute_integral(func, a, b, epsilon, method):
    n = 4
    runge_coef = {
        "Метод левых прямоугольников": 1,
        "Метод правых прямоугольников": 1,
        "Метод средних прямоугольников": 3,
        "Метод трапеций": 3,
        "Метод Симпсона": 15
    }
    coef = runge_coef[method]
    result = methods[method](func, a, b, n)
    r = math.inf
    while r > epsilon:
        n *= 2
        new_result = methods[method](func, a, b, n)
        r = abs(new_result - result) / coef
        result = new_result
    return result, n

def check_discontinuity_point(func, x):
    try:
        func(x)
        return False
    except (ZeroDivisionError, ValueError, OverflowError):
        return True

def check_convergence(func, a, b):
    if func == f4:
        if a == 0 or b == 0 or (a < 0 < b):
            return False
        return True
    elif func == f5:
        if a <= 0:
            return False
        return True
    else:
        return True

def check_discontinuity(func, a, b):
    if check_discontinuity_point(func, a) or check_discontinuity_point(func, b):
        return True
    if func == f4 and a < 0 < b:
        return True
    return False

def compute_improper_integral(func, a, b, epsilon, method):
    delta = 1e-8
    if check_discontinuity_point(func, a):
        a += delta
    if check_discontinuity_point(func, b):
        b -= delta
    return compute_integral(func, a, b, epsilon, method)

def get_int_in_range(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Ошибка: введите целое число от {min_val} до {max_val}")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число")

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print("Ошибка: точность должна быть строго больше нуля")
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число")

def get_integration_limits():
    while True:
        try:
            a = float(input("Начальный предел (a): "))
            b = float(input("Конечный предел (b): "))
            if a < b:
                return a, b
            print("Ошибка: начальный предел 'a' должен быть строго меньше конечного предела 'b'. Попробуйте снова")
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные числа")

def main():
    print("\nВыберите функцию:")
    print("1. x^2")
    print("2. sin(x)")
    print("3. e^x")
    print("4. 1/x^2")
    print("5. log(x)")

    func_choice = get_int_in_range("Ваш выбор (1-5): ", 1, 5)
    func = functions[func_choice - 1]

    print("\nВведите пределы интегрирования:")
    a, b = get_integration_limits()

    print("\nВыберите метод интегрирования:")
    for i, method_name in enumerate(methods, 1):
        print(f"{i}. {method_name}")

    method_choice = get_int_in_range("Ваш выбор (1-5): ", 1, 5)
    method = list(methods.keys())[method_choice - 1]

    epsilon = get_positive_float("\nВведите требуемую точность вычислений (>0): ")

    if not check_convergence(func, a, b) or check_discontinuity(func, a, b):
        print("\nИнтеграл не существует (расходится или разрыв на границе)")
    else:
        result, n = compute_improper_integral(func, a, b, epsilon, method)
        print("\nРезультат:")
        print(f"Значение интеграла: {result}")
        print(f"Число разбиений для достижения точности: {n}")

if __name__ == "__main__":
    main()