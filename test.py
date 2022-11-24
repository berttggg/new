import unittest

from library import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
        
    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(" aaa5", l[1][1])
        
    def test_read3(self):
        try:
            printer = CSVPrinter("sample2.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except (FileNotFoundError, IOError) as e:
            print('No such as a file')
        