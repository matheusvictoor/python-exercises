import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global precede_impares
        undertest = __import__(module)
        precede_impares = getattr(undertest, 'precede_impares', None)

    def test_exemplo(self):
        assert precede_impares([15, 2, 4, 3, 8, 7, 6]) == [4, 8]
        assert precede_impares([4, 3, 2, 2, 4, 5]) == [4]
        assert precede_impares([1, 5, 4, 3, 8, 7]) == [4, 8]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
