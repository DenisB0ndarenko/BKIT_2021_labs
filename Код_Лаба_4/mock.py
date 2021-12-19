from pattern import *
from unittest import TestCase
from unittest.mock import patch


class MockTest(TestCase):
    @patch('pattern.LeftStick.made_of', return_value="I'm Left stick. I'm made of Left caramel on the Left biscuit."
                                                     " We are the same.")
    def test_made_of(self, made_of):
        self.stick = LeftStick()
        self.assertEqual(self.stick.made_of(), "I'm Left stick. I'm made of Left caramel on the Left biscuit."
                                               " We are the same.")

    @patch('pattern.RightStick.i_stick', return_value="Right stick.")
    def test_made_of2(self, i_stick):
        self.stick = RightStick()
        self.assertEqual(self.stick.made_of(), "I'm Right stick. I'm made of Right caramel on the Right biscuit."
                                               " We are the same.")


if __name__ == '__main__':
    unittest.main()
