import volume_calculation as volume
import unittest


#For some reason, I only got one test to run when it was in one method. Had to split it
#into three methods to get all three to run.
class test_volume(unittest.TestCase):
    def test_vol(self):
        self.assertEqual(volume.volume_of_cube(2,3,4), 24)
    def test_vol_neg(self):
        self.assertEqual(volume.volume_of_cube(-2,-3,-4), -24)
    def test_vol_decimal(self):
        self.assertEqual(volume.volume_of_cube(-10,-10.5,1), 105)


if __name__ == "__main__":
    unittest.main()