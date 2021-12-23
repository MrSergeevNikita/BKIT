import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        print(prompt, end=' ')
        coef_str = input()
    while True:
        try:
            float(coef_str)
        except ValueError:
            coef_str = input(prompt + ' ')
        else:
            break
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    if a==0 and b==0 and c==0:
        result = 'infinity'
    elif a==0 or b==0:
        if c > 0:
            result = list()
        elif c == 0:
            result = [0, ]
        else:
            if a == 0:
                result = [-math.sqrt(-c/b), math.sqrt(-c/b)]
            else:
                result = [-math.sqrt(math.sqrt(-c/a)), math.sqrt(math.sqrt(-c/a))]
    elif c == 0:
        if a > 0 and b > 0:
            result = [0, ]
        else:
            result = [-math.sqrt(abs(b/a)), 0, math.sqrt(abs(b/a))]
    else:
        result = list()
        D = b * b - 4 * a * c
        if D == 0.0:
            root = -b / (2.0 * a)
            result.append(root)
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0 * a)
            root2 = (-b - sqD) / (2.0 * a)
            if root1 >= 0:
                result.append(-math.sqrt(root1))
                result.append(math.sqrt(root1))
            if root2 >= 0:
                result.append(-math.sqrt(root2))
                result.append(math.sqrt(root2))
    return result


def main():
    '''
    Основная функция
    '''

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней

    # Вывод корней
    roots = get_roots(a, b, c)
    if isinstance(roots, str):
        len_roots = 1
    else:
        len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1 and not isinstance(roots, str):
        print("Один корень: {}".format(roots[0]))
    elif len_roots == 2:
        print("Два корня: {} и {}".format(roots[0], roots[1]))
    elif len_roots == 3:
        print("Три корня: {}, {} и {}".format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print("Четыре корня: {}, {}, {} и {}".format(roots[0], roots[1], roots[2], roots[3]))
    else:
        print("Бесконечное количество корней")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()