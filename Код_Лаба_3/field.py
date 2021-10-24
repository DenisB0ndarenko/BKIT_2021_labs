def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            try:
                if i[args[0]] is not None:
                    yield i[args[0]]
            except KeyError:
                pass
    else:
        for i in items:
            new_dict = {}
            for key in args:
                try:
                    if i[key] is not None:
                        new_dict.update({key: i[key]})
                except KeyError:
                    pass
            if not len(new_dict) == 0:
                yield new_dict


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print(', '.join(field(goods, 'title')))

    for k in field(goods, 'title', 'price'):
        print(k, end=' ')
    pass
