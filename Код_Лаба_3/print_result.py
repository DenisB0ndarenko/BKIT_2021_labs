def print_result(function):
    def wrapper(*args, **kwargs):
        print(function.__name__)
        result = function(*args, **kwargs)
        if isinstance(result, dict):
            for k, v in result.items():
                print('{} = {}'.format(k, v))
        elif isinstance(result, list):
            for i in result:
                print(i)
        else:
            print(result)
        return result
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
