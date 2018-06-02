#!/usr/bin/python3


def count_greedy_combinations(n, level):
    if n < 0:
        return 0
    if n == 0 and level == 0:
        return 0
    if n == 0 and level > 0:
        return 1
    return (count_greedy_combinations(n-1, level+1)
            + count_greedy_combinations(n-2, level+1)
            + count_greedy_combinations(n-3, level+1))


def count_combinations(n, level):
    if n < 0:
        return 0
    if n == 0 and level == 0:
        return 0
    if n == 0 and level > 0:
        return 1

    return n


combination_results = []


def main():
    n = int(input('Ingrese número de pasos: '))
    print('Número de combinaciones: {}'.format(count_greedy_combinations(n, 0)))


if __name__ == '__main__':
    main()