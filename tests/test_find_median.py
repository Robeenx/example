
import unittest

import get_base_dir
from find_median import find_median


class TestFindMedian(unittest.TestCase):
    """Тестирование функции поиска медианы или среднего значения
    центральных элементов списка, в зависимости от их колличества"""

    def test_1(self):
        """Проверка списка: [1, 5, 2, 3, 6], искомое значение: 3"""
        self.assertEqual(find_median([1, 5, 2, 3, 6]), 3)

    def test_2(self):
        """Проверка списка: [100, 5, 2, 4, 3, 6], искомое значение: 4.5"""
        self.assertEqual(find_median([100, 5, 2, 4, 3, 6]), 4.5)


if __name__ =='__main__':
    unittest.main()
