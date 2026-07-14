import timeit

import numpy as np


def somme_for(data):
    total = 0.0
    for x in data:
        total += x
    return total


def somme_numpy(data):
    return data.sum()


def main():
    arr = np.random.rand(1_000_000)
    lst = arr.tolist()

    print(f"sum(list) : {timeit.timeit(lambda: sum(lst), number=50):.6f}s")
    print(f"arr.sum()  : {timeit.timeit(lambda: arr.sum(), number=50):.6f}s")

    print("for   :", somme_for(lst))
    print("numpy :", somme_numpy(arr))
    print()

    n = 10
    t_for = timeit.timeit(lambda: somme_for(lst), number=n) / n
    t_numpy = timeit.timeit(lambda: somme_numpy(arr), number=n) / n

    print(f"for pur Python : {t_for * 1000:8.3f} ms")
    print(f"np.sum()       : {t_numpy * 1000:8.3f} ms")
    print(f"→ NumPy ~{t_for / t_numpy:.0f}x plus rapide")


if __name__ == "__main__":
    main()
