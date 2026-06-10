import math


def f(x):
    return 2 * math.sin(x) - 1.5 * math.cos(2 * x) + math.sin(3 * x) - 0.5 * math.cos(4 * x)

a0, b0 = -2.0, 2.0
a, b = a0, b0
eps = 10**-8
tau = (math.sqrt(5) - 1) / 2

x1 = a + (b - a) * (1 - tau)
x2 = a + (b - a) * tau
f1, f2 = f(x1), f(x2)
iterations = 0

while (b - a) > eps:
    iterations += 1
    if f1 <= f2:
        b = x2
        x2 = x1
        f2 = f1
        x1 = a + (b - a) * (1 - tau)
        f1 = f(x1)
    else:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + (b - a) * tau
        f2 = f(x2)

x_min = (a + b) / 2
f_min_val = f(x_min)

Nt_raw = math.log((b0 - a0) / eps) / math.log(1 / tau)
Nt = math.ceil(Nt_raw)

print(f"Найденная точка минимума (x): {x_min:.4f}")
print(f"Значение функции в минимуме (f): {f_min_val:.4f}")
print(f"Количество итераций: {iterations}")
print(f"Nt = {Nt}")