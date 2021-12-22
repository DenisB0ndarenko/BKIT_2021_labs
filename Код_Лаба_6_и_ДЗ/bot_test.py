import unittest
from bot2 import *


class MyTest(unittest.TestCase):

    def setUp(self):
        self.love_comp = [[True, False, False, False],
                          [False, True, False, True],
                          [False, False, False, True],
                          [False, True, False, False]]

        self.work_comp = [[True, False, True, False],
                          [True, True, True, False],
                          [False, False, True, True],
                          [True, False, False, False]]

    def test_conclusion_true_love(self):
        s1 = '2'
        s2 = '3'
        rltn = 'Любовь'
        self.assertEqual(config.conclusion(s1, s2, rltn), True)

    def test_conclusion_false_work(self):
        s1 = '0'
        s2 = '1'
        rltn = 'Работа'
        self.assertEqual(config.conclusion(s1, s2, rltn), False)


if __name__ == '__main__':
    unittest.main()
