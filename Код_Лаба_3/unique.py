from gen_random import gen_random


class Unique(object):

    def __init__(self, items, **kwargs):
        self.items = items
        self.used = set()
        assert len(kwargs) < 2
        if len(kwargs) == 0:
            self.ignore_case = False
        else:
            try:
                self.ignore_case = kwargs['ignore_case']
            except KeyError as k:
                print('Имя именованного итератора должно быть {}'.format(k))
                raise

    def __next__(self):
        it = iter(self.items)
        while True:
            try:
                cur = next(it)
                if self.ignore_case and isinstance(cur, str):
                    curl = cur.lower()
                    if curl not in self.used:
                        self.used.add(curl)
                        return cur
                elif cur not in self.used:
                    self.used.add(cur)
                    return cur
            except StopIteration:
                raise

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print([i for i in Unique(data)])

    data = gen_random(10, 1, 3)
    print([i for i in Unique(data)])

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print([i for i in Unique(data)])
    print([i for i in Unique(data, ignore_case=True)])
