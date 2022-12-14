
import sys
import unittest
from os.path import dirname, realpath

sys.path.append(dirname(dirname(realpath(__file__))))
from lucky_tickets import count_tickets


class TestLuckyTickets(unittest.TestCase):
    """Тестирование функции определения счастливого билета."""

    def test_num_sub_zero(self):
        """Тестирование значения меньше нуля."""
        self.assertEqual(count_tickets(-5), 0)

    def test_num_zero(self):
        """Тестирование значения равного нулю."""
        self.assertEqual(count_tickets(0), 0)

    def test_num_one(self):
        """Тестирование значения равного единице."""
        self.assertEqual(count_tickets(1), 0)

    def test_num_two(self):
        """Тестирование значения равного двойке."""
        self.assertEqual(count_tickets(2), 10)

    def test_num_three(self):
        """Тестирование значения равного тройке."""
        self.assertEqual(count_tickets(3), 10)


if __name__ == '__main__':
    unittest.main()
