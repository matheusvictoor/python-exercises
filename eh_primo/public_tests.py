# coding: utf-8

import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
eh_primo = getattr(undertest, 'eh_primo', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        assert eh_primo(3) == True

    def test_exemplo_2(self):
        assert eh_primo(5) == True

    def test_exemplo_3(self):
        assert eh_primo(10) == False

    def test_exemplo_4(self):
        assert eh_primo(11) == True

    def test_exemplo_5(self):
        assert eh_primo(15) == False
        

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
