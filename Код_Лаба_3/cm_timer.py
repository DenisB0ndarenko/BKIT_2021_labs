from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.t0 = 0

    def __enter__(self):
        self.t0 = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, exc_val, exc_tb)
        else:
            print('time: {}'.format(time()-self.t0))


@contextmanager
def cm_timer_2():
    t0 = time()
    yield
    print('time: {}'.format(time() - t0))


if __name__ == '__main__':
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)
