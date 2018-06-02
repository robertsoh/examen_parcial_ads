

def es_mayor_edad(edad):
    if edad >= 18:
        es_mayor_edad = True
    else:
        es_mayor_edad = False
    return es_mayor_edad


def main():
    print('Es mayor: {}'.format(es_mayor_edad(17)))

if __name__ == '__main__':
    main()