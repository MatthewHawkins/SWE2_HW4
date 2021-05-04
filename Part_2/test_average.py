import average_calculation
import unittest


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [-1, -17, 4, 16, 8]
list3 = []

class test_avg(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(average_calculation.calculate_average(list1, len(list1)), 5.5)
    def test_avg_neg(self):
        self.assertEqual(average_calculation.calculate_average(list2, len(list2)), 2)
    def test_divide_by_zero_exception(self):
        with self.assertRaises(ZeroDivisionError):
            average_calculation.calculate_average(list3, len(list3))


if __name__ == "__main__":
    unittest.main()