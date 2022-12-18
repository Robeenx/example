
import unittest

import get_base_dir
from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """Тестирование функции fizz_buzz"""

    def test_multiples_3(self):
        """Замена кратных 3-м на 'Fizz'"""
        for index, value in enumerate(fizz_buzz(), 1):
            if not index % 3 and index % 5:
                self.assertEqual(value, 'Fizz')

    def test_multiples_5(self):
        """Замена кратных 5-и на 'Buzz'"""
        for index, value in enumerate(fizz_buzz(), 1):
            if not index % 5 and index % 3:
                self.assertEqual(value, 'Buzz')

    def test_multiples_3_and_5(self):
        """Замена кратных 3-м и 5-и на 'FizzBuzz'"""
        for index, value in enumerate(fizz_buzz(), 1):
            if not index % 3 and not index % 5:
                self.assertEqual(value, 'FizzBuzz')
    
    def test_not_multiples_3_and_5(self):
        """Числа не кратные 3-м и 5-и не заменены'"""
        for index, value in enumerate(fizz_buzz(), 1):
            if index % 3 and index % 5:
                self.assertEqual(value, index)


if __name__ == '__main__':
    unittest.main()
