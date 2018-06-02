

def es_mayor_edad(edad):
    if edad <= 0:
        raise "La edad debe ser mayor a 0"
    return edad >= 18


def main():
    print('Es mayor: {}'.format(es_mayor_edad(-1)))


if __name__ == '__main__':
    main()