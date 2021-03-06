# coding=utf-8
import random
import sys
import time
import drawing
import bernoulli
import lobachevsky

# Constants
# Константы
accuracy = 0.1 ** 6

# Coefficients of a polynomial
# Коэффициенты полинома
coefficients0 = [1, -21, 175, -735, 1624, -1764, 720]
coefficients1 = [1, -15, 85, -225, 274, -120]
coefficients2 = [1, -10, 35, -50, 24]
# coefficients2_ = [1, -100, 3500, -50000, 24000]
coefficients3 = [1, -6, 11, -6]
coefficients4 = [1, -3, 2]


# The polynomial at the point
# Полином в точке
def f(point, a=coefficients0):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * point ** (power - n - 1)

    return result


def iter_benchmark(args, time_):
    iterations = args[1]
    iterations_count = 0

    for i in range(len(iterations)):
        iterations_count += iterations[i]

    return time_ / iterations_count


def format_output(args, time_):
    roots = args[0]
    iterations = args[1]

    print("Полином степени {0}:".format(len(roots)))

    for i in range(len(roots)):
        print("Корень {0} найден за {1} итераций".format(roots[i], iterations[i]))
    print("Общее время подсчёта: {:4f}мс".format(time_))

    print()


def format_output_l(args, time_):
    roots = args[0]
    iterations = args[1]

    print("Полином степени {0}:".format(len(roots)))

    for i in range(len(roots)):
        print("Корень {0}".format(roots[i]))

    print("Общее количество итераций: {0}".format(iterations))
    print("Общее время подсчёта: {:4f}мс".format(time_))

    print()


def random_(power):
    return (random.uniform(20, 21) ** power) ** random.uniform(0.4, 0.5)


if __name__ == "__main__":
    sys.setrecursionlimit(5000)

    drawing.build_function(f, coefficients0, "f6(x)", -1, 7, -4, 4)
    drawing.show_plot()

    drawing.build_function(f, coefficients1, "f5(x)", -1, 7, -4, 4)
    drawing.show_plot()

    drawing.build_function(f, coefficients2, "f4(x)", -1, 7, -4, 4)
    drawing.show_plot()

    drawing.build_function(f, coefficients3, "f3(x)", -1, 7, -4, 4)
    drawing.show_plot()

    drawing.build_function(f, coefficients4, "f2(x)", -1, 7, -4, 4)
    drawing.show_plot()

    # Drawing
    # Построение
    drawing.build_function(f, coefficients0, "f6(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients1, "f5(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients2, "f4(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients3, "f3(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients4, "f2(x)", -1, 7, -4, 4)

    drawing.show_plot()

    # Bernoulli benchmark
    bernoulli_time = []
    iter_b = 0

    print("Метод Бернулли")
    print()

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients0, [6, 5, 4, 3, 2, 1], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)
    iter_b += iter_benchmark(ret, result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients1, [6, 5, 4, 3, 2], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)
    iter_b += iter_benchmark(ret, result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients2, [6, 5, 4, 3], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)
    iter_b += iter_benchmark(ret, result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients3, [6, 5, 4], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)
    iter_b += iter_benchmark(ret, result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients4, [6, 5], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)
    iter_b += iter_benchmark(ret, result_time)

    bernoulli_iter_complexity = iter_b / 5 * 1000000
    print("Сложность итерации для метода Бернулли: {:4f}нс".format(bernoulli_iter_complexity))

    drawing.data_plot([2, 3, 4, 5, 6], list(reversed(bernoulli_time)),
                      "Метод Бернулли",
                      "Рост времени рассчёта от роста степени полинома",
                      "Степень",
                      "Время (мс)",
                      [2, 3, 4, 5, 6, 7])

    print()
    print("Метод Лобачевского")
    print()

    lobachevsky_time = []

    start = time.time()
    ret = lobachevsky.lobachevsky_execute(f, coefficients4, accuracy)
    result_time = (time.time() - start) * 1000
    format_output_l(ret, result_time)
    lobachevsky_time.append(result_time)

    start = time.time()
    ret = lobachevsky.lobachevsky_execute(f, coefficients3, accuracy)
    result_time = (time.time() - start) * 1000
    format_output_l(ret, result_time)
    lobachevsky_time.append(result_time)

    lobachevsky_time_sum = lobachevsky_time[0] + lobachevsky_time[1]
    print("Сложность итерации для метода Лобачевского: {:4f}мс".format(lobachevsky_time_sum / 12 * 1000))
    print("Сложность итерации для метода Лобачевского: {:4f}нс".format(lobachevsky_time_sum / 12 * 1000 * 1000000))

    drawing.data_plot([2, 3], lobachevsky_time,
                      "Метод Лобачевского",
                      "Рост времени рассчёта от роста степени полинома",
                      "Степень",
                      "Время (мс)",
                      [2, 3, 4, 5, 6, 7])

    ttt = [1.1801719665527344, 0.38596649169921875, 0.15735626220703125, 0.10728836059570312, 0.08344650268554688]

    drawing.data_plot([2, 3, 4, 5, 6], list(reversed(ttt)),
                      "Метод Лобачевского (Искусственный)",
                      "Рост времени рассчёта от роста степени полинома",
                      "Степень",
                      "Время (мс)",
                      [2, 3, 4, 5, 6, 7])

    drawing.show_plot()
