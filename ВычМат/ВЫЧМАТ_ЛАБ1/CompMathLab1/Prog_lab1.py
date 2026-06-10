import copy
import numpy as np

def input_n(prompt):
    while True:
        try:
            n = int(input(prompt))
            if not (1 <= n <= 20):
                print("Размерность должна быть 1 <= n <= 20")
                continue
            return n
        except ValueError:
            print("Введите целое число")


def input_matrix_A(n):
    A = []
    print("Введите матрицу коэффициентов (по строкам):")

    for i in range(n):
        while True:
            try:
                row = list(map(float, input(f"Строка №{i + 1}: ").split()))
                if len(row) != n:
                    print(f"Нужно ввести {n} чисел")
                    continue
                A.append(row)
                break
            except ValueError:
                print("Введите корректные числовые значения")

    return A


def input_vector_b(n):
    while True:
        try:
            b = list(map(float, input("Введите вектор свободных членов b: ").split()))
            if len(b) != n:
                print(f"Нужно ввести ровно {n} чисел")
                continue
            return b
        except ValueError:
            print("Введите корректные числовые значения")


def input_from_file():
    while True:
        filename = input("Введите имя файла: ")

        try:
            with open(filename, "r") as f:
                lines = f.readlines()

            if len(lines) < 2:
                print("Файл содержит недостаточно данных")
                continue

            n = int(lines[0].strip())

            if not (1 <= n <= 20):
                print("Некорректная размерность в файле")
                continue

            if len(lines) != n + 2:
                print("Количество строк в файле некорректно")
                continue

            A = []
            for i in range(1, n + 1):
                row = list(map(float, lines[i].split()))
                if len(row) != n:
                    print("Матрица не соответствует заданной размерности")
                    return None, None, None
                A.append(row)

            b = list(map(float, lines[n + 1].split()))
            if len(b) != n:
                print("Вектор свободных членов не соответствует размерности")
                return None, None, None

            return n, A, b

        except FileNotFoundError:
            print("Файл не найден, попробуйте снова")
        except ValueError:
            print("В файле некорректные числовые данные")


def choose_input():
    while True:
        print("\nВыберите способ ввода:")
        print("1 — С клавиатуры")
        print("2 — Из файла")

        choice = input("Ваш выбор: ")

        if choice == "1":
            n = input_n("Введите размерность системы n = ")
            A = input_matrix_A(n)
            b = input_vector_b(n)
            return n, A, b

        elif choice == "2":
            result = input_from_file()
            if result[0] is not None:
                return result

        else:
            print("Некорректный выбор, попробуйте снова")

def straight_runnig(A, b, n):
    swaps = 0

    for k in range(n):
        max_row = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[max_row][k]):
                max_row = i

        if A[max_row][k] == 0:
            print("Матрица вырождена")
            return None, None, None

        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            b[k], b[max_row] = b[max_row], b[k]
            swaps += 1

        for i in range(k + 1, n):
            multiplier = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= multiplier * A[k][j]
            b[i] -= multiplier * b[k]

    return A, b, swaps

def reverse_gear(A, b, n):
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_known = 0
        for j in range(i + 1, n):
            term = A[i][j] * x[j]
            sum_known += term
        numerator = b[i] - sum_known
        denominator = A[i][i]
        x[i] = numerator / denominator
    return x


def determinant(A, swaps, n):
    det = 1
    for i in range(n):
        det *= A[i][i]
    if swaps % 2 != 0:
        det *= -1
    return det


def r_vector(A_orig, b_orig, x, n):
    r = []
    for i in range(n):
        left = 0
        for j in range(n):
            term = A_orig[i][j] * x[j]
            left += term
        r_vec = left - b_orig[i]
        r.append(r_vec)
    return r

def main():

    n, A, b = choose_input()

    print("\nИсходные данные:")
    print("Размерность n =", n)

    print("Матрица A:")
    for row in A:
        print(row)

    print("Вектор b:")
    print(b)

    A_orig = copy.deepcopy(A)
    b_orig = b.copy()

    A_triangular, b_transformed, swaps = straight_runnig(A, b, n)

    if A_triangular is None:
        return

    print("\nТреугольная матрица:")
    for i in range(n):
        for j in range(n):
            print(f"{A_triangular[i][j]:10.5f}", end=" ")
        print("|", f"{b_transformed[i]:10.5f}")

    x = reverse_gear(A_triangular, b_transformed, n)

    print("\nРешение:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")

    det = determinant(A_triangular, swaps, n)
    print("\ndet A = ", det)

    r = r_vector(A_orig, b_orig, x, n)
    print("\nВектор невязки:")
    for i in range(n):
        print(f"r{i+1} = {r[i]:.10f}")

    A_np = np.array(A_orig)
    b_np = np.array(b_orig)

    x_lib = np.linalg.solve(A_np, b_np)
    det_lib = np.linalg.det(A_np)

    print("\nNumPy:")
    print("Решение:")
    for i in range(n):
        print(f"x{i+1} = {x_lib[i]:.6f}")

    print("\ndet A_lib = ", det_lib)

    print("\nСравнение:")
    for i in range(n):
        print(f"|x{i+1} - x_lib{i+1}| = {abs(x[i] - x_lib[i]):.10f}")

    print("Разница определителей =", abs(det - det_lib))


if __name__ == "__main__":
    main()
