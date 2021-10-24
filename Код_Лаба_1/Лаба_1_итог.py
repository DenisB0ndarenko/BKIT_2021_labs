import sys
import math

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

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
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
        while not isfloat(coef_str):
            coef_str = input()
    # Переводим строку в действительное число
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
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        #get_roots(1, 0, -root)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        #get_roots(1, 0, -root1)
        #get_roots(1, 0, -root2)
        result.append(root1)
        result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    if a == 0:
        print('Не биквадратное уравнение')
        exit(0)
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        root = roots[0]
        roots = []
        roots = get_roots(1,0,-root)
    elif len_roots == 2:
        root3 = roots[1]
        root4 = roots[0]
        roots = get_roots(1,0,-root3)
        roots += get_roots(1,0,-root4)
    # Вывод корней
    len_roots = len(roots)
    
    if len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# Лаба_1_итог.py 1 0 -4
