
import unittest

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

class TestIsPrime(unittest.TestCase):
    def test_num_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))

    def test_num_non_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(1))

    def test_num_2(self):
        self.assertTrue(is_prime(2))

    def test_num_le_1(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

if __name__ == '__main__':
    unittest.main()