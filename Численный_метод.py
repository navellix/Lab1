import math
import time
import numpy as np


def f_n(x, n):
    m = 2.0 ** n
    return np.floor(m / (x + 1.0)) / m

# вычисляет интеграл Лебега функции f_n на [a, b]
def integrate_lebesgue_fn(n, a=0.0, b=4.0, steps=200000):
    xs = np.linspace(a, b, steps + 1)
    ys = f_n(xs, n)
    return np.trapezoid(ys, xs)

# вычисляет интеграл Лебега-Стилтьеса от f_n на [a, b]
def integrate_stieltjes_fn(n, a=0.0, b=4.0, steps=200000):
    xs = np.linspace(a, b, steps + 1)
    ys = 4.0 * xs * f_n(xs, n)
    return np.trapezoid(ys, xs)

# значение интеграла Лебега, вычисленное аналитически
def analytical_lebesgue():
    return math.log(5.0)

# значение интеграла Лебега-Стилтьеса, вычисленное аналитически
def analytical_stieltjes():
    return 16.0 - 4.0 * math.log(5.0)


def main():
    ns = [10, 100, 1000]
    steps = 200000

    exact_lebesgue = analytical_lebesgue()
    exact_stieltjes = analytical_stieltjes()

    print(f"Отрезок интегрирования: E = [0, 4]")
    print(f"Используемые значения n: {ns}")
    print()

    print("Задание 2.2. Интеграл Лебега от f_n по E")
    print(f"Аналитическое значение интеграла Лебега = ln(5) = {exact_lebesgue:.12f}")
    print()

    for n in ns:
        start = time.perf_counter()
        value = integrate_lebesgue_fn(n, steps=steps)
        elapsed = time.perf_counter() - start
        error = abs(value - exact_lebesgue)

        print(f"n = {n}")
        print(f"Численное значение:     {value:.12f}")
        print(f"Аналитическое значение: {exact_lebesgue:.12f}")
        print(f"Погрешность:            {error:.12e}")
        print(f"Время работы:           {elapsed:.6f} c")
        print()

    print("Задание 2.3. Интеграл Лебега–Стилтьеса от f_n по E")
    print(f"Аналитическое значение интеграла Лебега-Стилтьеса = 16 - 4 ln(5) = {exact_stieltjes:.12f}")
    print()

    for n in ns:
        start = time.perf_counter()
        value = integrate_stieltjes_fn(n, steps=steps)
        elapsed = time.perf_counter() - start
        error = abs(value - exact_stieltjes)

        print(f"n = {n}")
        print(f"Численное значение:     {value:.12f}")
        print(f"Аналитическое значение: {exact_stieltjes:.12f}")
        print(f"Погрешность:            {error:.12e}")
        print(f"Время работы:           {elapsed:.6f} c")
        print()


if __name__ == "__main__":
    main()