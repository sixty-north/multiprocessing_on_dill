import unittest
from mp2.pool import Pool

def square(x):
    return x*x

class TestCallables(unittest.TestCase):

    def test_function(self):
        p = Pool(12)
        result = p.map(square, range(10000), chunksize=1)
        self.assertListEqual(result, [x*x for x in range(10000)])

    def test_lambda(self):
        p = Pool(12)
        result = p.map(lambda x: x*x, range(10000), chunksize=1)
        self.assertListEqual(result, [x*x for x in range(10000)])

if __name__ == '__main__':
    unittest.main()
