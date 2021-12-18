from School2 import *
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.clss = [
                    Cls(1, '11А'),
                    Cls(2, '7Б'),
                    Cls(3, '5В'),

                    Cls(11, '11Б'),
                    Cls(22, '7В'),
                    Cls(33, '5А'),
                    ]
        self.pups = [
                    Pup(1, 'Абуховский', 5000, 1),
                    Pup(2, 'Рыжкова', 0, 2),
                    Pup(3, 'Зелинский', 10000, 2),
                    Pup(4, 'Бондаренко', 10000, 3),
                    Pup(5, 'Смыслов', 30000, 3),
                    ]
        self.pups_clss = [
                         PupCls(1, 1),
                         PupCls(2, 2),
                         PupCls(2, 3),
                         PupCls(3, 4),
                         PupCls(3, 5),

                         PupCls(11, 1),
                         PupCls(22, 2),
                         PupCls(22, 3),
                         PupCls(33, 4),
                         PupCls(33, 5),
                         ]

        self.one_to_many = [(p.fio, p.dbt, c.name)
                            for c in clss
                            for p in pups
                            if p.cls_id == c.id]

        self.many_to_many_temp = [(c.name, pc.cls_id, pc.pup_id)
                                  for c in clss
                                  for pc in pups_clss
                                  if c.id == pc.cls_id]

        self.many_to_many = [(p.fio, p.dbt, cls_name)
                             for cls_name, cls_id, pup_id in self.many_to_many_temp
                             for p in pups if p.id == pup_id]

    def test_task_a1(self):
        prediction = [('Абуховский', 5000, '11А'), ('Бондаренко', 10000, '5В'), ('Смыслов', 30000, '5В'),
                      ('Рыжкова', 0, '7Б'), ('Зелинский', 10000, '7Б')]
        self.assertEqual(task_a1(self.one_to_many), prediction)

    def test_task_a2(self):
        prediction = [('5В', 40000), ('7Б', 10000), ('11А', 5000)]
        self.assertEqual(task_a2(self.one_to_many), prediction)

    def test_task_a3(self):
        prediction = {'7Б': ['Рыжкова', 'Зелинский'], '11Б': ['Абуховский']}
        self.assertEqual(task_a3(self.many_to_many), prediction)


if __name__ == '__main__':
    unittest.main()
