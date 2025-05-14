import unittest
from functions import sum, multiply

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, 'should return 6 when summing list')

    def test_multiply(self):
        self.assertEqual(multiply([1,2,3]), 6, 'should return 6 when multiplying list')

if __name__ == '__main__':
    unittest.main()
