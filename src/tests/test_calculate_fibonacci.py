
import unittest

def calculate_fibonacci(n):
    if n < 0:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

class TestCalculateFibonacci(unittest.TestCase):
    def test_n_0(self):
        self.assertEqual(calculate_fibonacci(0), [])

    def test_n_1(self):
        self.assertEqual(calculate_fibonacci(1), [0])

    def test_n_2(self):
        self.assertEqual(calculate_fibonacci(2), [0, 1])

    def test_n_positive(self):
        self.assertEqual(calculate_fibonacci(5), [0, 1, 1, 2, 3])

    def test_n_negative(self):
        self.assertEqual(calculate_fibonacci(-1), [])

if __name__ == '__main__':
    unittest.main()