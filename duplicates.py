
class Result(object):
    has_duplicated = None
    steps = None


def greedy_duplicate_values(numbers, result):
    """ Complejidad cuadrática """
    steps = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            steps += 1
            if i != j and numbers[i] == numbers[j]:
                result.has_duplicated = True
                result.steps = steps
                return result
    result.has_duplicated = False
    result.steps = steps
    return result


def duplicate_values(numbers, result):
    """" Complejidad lineal """
    dict_numbers = {}
    steps = 0
    for number in numbers:
        steps += 1
        dict_numbers.update({number: number})
    if len(dict_numbers.keys()) == len(numbers):
        result.has_duplicated = False
    else:
        result.has_duplicated = True
    result.steps = steps
    return result


def main():
    result = Result()
    numbers = [45, 69, 2, 1, 3, 7, 8, 9, 10, 11, 15, 17, 18, 20, 25, 26, 27, 19, 38, 38]
    result = duplicate_values(numbers, result)
    print('N: {}'.format(len(numbers)))
    print('Optimizated - Has duplicate values: {}'.format(result.has_duplicated))
    print('Optimizated - Steps: {}'.format(result.steps))


if __name__ == '__main__':
    main()