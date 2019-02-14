import math
import filecmp
import unittest
import sys
import time
import platform


def ceil(number):
    return math.ceil(number)


def factorial(number):
    return math.factorial(number)


def pow(x, y):
    return math.pow(x, y)


def file_compare(file1, file2):
    return filecmp.cmp(file1, file2)


def time_clock():
    return time.clock()


class MathTest(unittest.TestCase):
    def test_ceil(self):
        self.assertEqual(ceil(100.000000000001), 101)
        self.assertEqual(ceil(999999.9), 1000000)
        self.assertEqual(ceil(1.000000000001), 2)
        self.assertEqual(ceil(float(sys.maxsize)+0.01), sys.maxsize+1)
        self.assertEqual(ceil(-100.1), -100)
        self.assertEqual(ceil(-0.1), 0)
        self.assertEqual(ceil(0.0000000001), 1)
        # ???
        # self.assertEqual(ceil((float(sys.maxsize)*-1)),
        #                 (sys.maxsize*-1))
        with self.assertRaises(OverflowError):
            ceil(float("inf"))
        with self.assertRaises(TypeError):
            ceil(None)
        with self.assertRaises(TypeError):
            ceil('test')

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(10), 3628800)
        self.assertGreater(factorial(100), 10000000)
        self.assertEqual(factorial(10), 1*2*3*4*5*6*7*8*9*10)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(3.1416)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(None)
        start_time = time.perf_counter()
        factorial(100000)
        duration = time.perf_counter() - start_time
        self.assertLess(duration, 1)
        # just checking it doesnt crash
        self.assertGreater(factorial(1000000), 1000)

    def test_pow(self):
        self.assertEqual(pow(2, 2), 4)
        self.assertEqual(pow(9, 9), 387420489)
        self.assertEqual(pow(0, 0), 1)
        self.assertEqual(pow(0, 1), 0)
        self.assertEqual(pow(1, 0), 1)
        self.assertEqual(pow(0, 1), 0)
        self.assertEqual(pow(1, -11), 1)
        self.assertEqual(pow(2, -11), 0.00048828125)
        self.assertEqual(pow(10, 0.5), 3.1622776601683795)
        self.assertEqual(pow(0.5, 10), 0.0009765625)
        self.assertEqual(pow(27, 3), 27*27*27)
        self.assertEqual(pow(99, -4), 1/(99*99*99*99))
        self.assertEqual(pow(55, 1/2), math.sqrt(55))
        with self.assertRaises(TypeError):
            pow(10, 'a')
        with self.assertRaises(TypeError):
            pow('a', 10)

    def test_filecmp(self):
        txt1 = open('unitTestTxt1.txt', 'w')
        txt1.write("123456789")
        txt2 = open('unitTestTxt2.txt', 'w')
        txt2.write("0000123456789\n")
        txt3 = open('unitTestTxt3.txt', 'w')
        txt3.write("123456789")

        txt1.close()
        txt2.close()
        txt3.close()
        self.assertTrue(file_compare(
            "filecmp_test1.txt", "filecmp_test1.txt"))
        self.assertFalse(file_compare(
            "filecmp_test1.txt", "filecmp_test2.txt"))
        self.assertTrue(file_compare(
            "filecmp_test2.txt", "filecmp_test2.txt"))
        self.assertFalse(file_compare(
            "filecmp_test2.txt", "filecmp_test5.pdf"))
        self.assertTrue(file_compare(
            "filecmp_test5.pdf", "filecmp_test5.pdf"))
        self.assertFalse(file_compare(
            "filecmp_test3.txt", "filecmp_test5.pdf"))
        self.assertFalse(file_compare(
            "filecmp_test3.txt", "filecmp_test4.app"))
        self.assertFalse(file_compare(
            False, "filecmp_test3.txt"))
        # ??
        # self.assertTrue(file_compare(
        #    "filecmp_test4.app", "filecmp_test4.app"))
        with self.assertRaises(TypeError):
            file_compare(None, "filecmp_test3.txt")
        with self.assertRaises(OSError):
            file_compare(-10, "filecmp_test3.txt")
        self.assertFalse(file_compare(
            "unitTestTxt1.txt", "unitTestTxt2.txt"))
        self.assertTrue(file_compare(
            "unitTestTxt1.txt", "unitTestTxt1.txt"))
        self.assertTrue(file_compare(
            "unitTestTxt1.txt", "unitTestTxt3.txt"))
        self.assertTrue(file_compare(
            "unitTestTxt1.txt", "unitTestTxt3.txt"))
        self.assertFalse(file_compare(True, True))
        self.assertFalse(file_compare(True, False))
        self.assertFalse(file_compare(False, False))
        with self.assertRaises(FileNotFoundError):
            file_compare("unitTestTxt1.txt", "unitTestTxt4.txt")
        with self.assertRaises(OSError):
            file_compare(3, 3)

    def test_time_clock(self):
        time1 = time_clock()
        time.sleep(0.1)
        time2 = time_clock()
        self.assertGreater(time2, time1)

        # clock function works different in windows and unix based systems
        if (platform.system() == "Windows"):
            start = time_clock()
            time.sleep(1)
            duration = time_clock() - start
            self.assertAlmostEqual(duration, 1)

        time1 = time_clock()
        time2 = time_clock()
        self.assertAlmostEqual(time1, time2, 3)

        time1 = time.time()
        clock1 = time_clock()
        factorial(50000)
        diff_time = time.time() - time1
        diff_clock = time_clock() - clock1
        self.assertAlmostEqual(diff_clock, diff_time, 2)


if __name__ == '__main__':
    unittest.main()
