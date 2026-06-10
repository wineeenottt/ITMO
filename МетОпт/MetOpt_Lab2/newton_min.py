import math

def f(x):
    return 2 * math.sin(x) - 1.5 * math.cos(2 * x) + math.sin(3 * x) - 0.5 * math.cos(4 * x)

def df(x):
    return 2 * math.cos(x) + 3 * math.sin(2 * x) + 3 * math.cos(3 * x) + 2 * math.sin(4 * x)

def d2f(x):
    return -2 * math.sin(x) + 6 * math.cos(2 * x) - 9 * math.sin(3 * x) + 8 * math.cos(4 * x)

x0 = -0.3
eps = 10**-8

x = x0
iterations = 0

while True:
    iterations += 1

    f_prime = df(x)
    f_double_prime = d2f(x)

    if abs(f_double_prime) < 1e-12:
        break

    x_new = x - f_prime / f_double_prime

    if abs(x_new - x) < eps:
        x = x_new
        break

    x = x_new

    if iterations > 1000:
        break

x_min = x
f_min = f(x_min)
df_val = df(x_min)

print(f"Найденная точка минимум (x) {x_min:.4f}")
print(f"Значение функции (f)       {f_min:.4f}")
print(f"{'Первая производная (df)':<25}  {df_val}")
print(f"Количество итераций (N)    {iterations}")