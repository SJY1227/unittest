import unittest
from unittest.mock import patch
from KHU_Festival import KHU_Festival

class KHU_Festival_Test(unittest.TestCase):
    def test_get_name(self):
        festival = KHU_Festival("Adelante", 130000000, [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]])
        self.assertEqual(festival.get_name(), "Adelante")

    def test_get_balance(self):
        festival = KHU_Festival("Adelante", 130000000, [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]])
        self.assertEqual(festival.get_balance(), 130000000)

    def test_get_lineup(self):
        festival = KHU_Festival("Adelante", 130000000, [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]])
        self.assertEqual(festival.get_lineup(), [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]])

    def test_set_name(self):
        festival = KHU_Festival()
        festival.set_name("Adelante")
        self.assertEqual(festival.get_name(), "Adelante")

    def test_set_balance(self):
        festival = KHU_Festival()
        festival.set_balance(130000000)
        self.assertEqual(festival.get_balance(), 130000000)

    def test_set_lineup(self):
        festival = KHU_Festival()
        new_lineup = [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]]
        festival.set_lineup(new_lineup)
        self.assertEqual(festival.get_lineup(), new_lineup)

    @patch('builtins.print')
    def test_print_lineup(self, mock_print):
        festival = KHU_Festival("Adelante", 130000000, [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]])
        festival.print_lineup()

        expected_output = "1일차 라인업\nLacuna\nSTAYC\n하이라이트\n\n2일차 라인업\n창모\nYB\n\n"
        mock_print.assert_called_with(expected_output)

if __name__ == '__main__':
    unittest.main()