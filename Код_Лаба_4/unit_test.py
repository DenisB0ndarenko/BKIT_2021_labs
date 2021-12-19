import unittest
from pattern import *


class MyTest(unittest.TestCase):

    def setUp(self):
        self.rcaramel = RightCaramel()
        self.lcaramel = LeftCaramel()
        self.rbiscuit = RightBiscuit()
        self.lbiscuit = LeftBiscuit()
        self.rstick = RightStick()
        self.lstick = LeftStick()

    def test_same(self):
        self.assertEqual(self.lcaramel.on_the_biscuit(self.lbiscuit),
                         "Left caramel on the Left biscuit. We are the same.")

    def test_not_same_lcrb(self):
        self.assertEqual(self.lcaramel.on_the_biscuit(self.rbiscuit),
                         "We are not the same.")

    def test_not_same_rclb(self):
        self.assertEqual(self.rcaramel.on_the_biscuit(self.lbiscuit),
                         "We are not the same.")

    def test_rstick(self):
        self.assertEqual(self.rstick.made_of(), "I'm Right stick. I'm made of Right caramel on the Right biscuit."
                                                " We are the same.")

    def test_lstick(self):
        self.assertEqual(self.lstick.made_of(), "I'm Left stick. I'm made of Left caramel on the Left biscuit."
                                                " We are the same.")


if __name__ == '__main__':
    unittest.main()
