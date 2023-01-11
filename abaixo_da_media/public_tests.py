import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_abaixo_media
        undertest = __import__(module)
        remove_abaixo_media = getattr(undertest, 'remove_abaixo_media', None)

    def test_exemplo1(self):
        l1 = [1, 1, 1, 1]
        remove_abaixo_media(l1)
        assert l1 == [1, 1, 1, 1]

    def test_exemplo2(self):
        l1 = [1, 1, 1, -1, 1]
        remove_abaixo_media(l1)
        assert l1 == [1, 1, 1, 1]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
