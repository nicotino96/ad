import context
import io
import random
import unittest
from unittest.mock import patch
from advanced import loops


class MultiplicationTableTestCase(unittest.TestCase):

    def test_correct_output_for_random_value1_no_exceeding_bounds(self):
        self.__test_case(random.randint(1, 50))

    def test_correct_output_for_random_value2_no_exceeding_bounds(self):
        self.__test_case(random.randint(1, 10))

    def test_correct_output_for_random_value3_no_exceeding_bounds(self):
        self.__test_case(random.randint(1000, 5000))

    def __test_case(self, n):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            loops.multiplication_table(n)
            self.assertTrue(fake_out.getvalue().__contains__(self.__expected_out(n)))
            self.assertFalse(fake_out.getvalue().startswith("0"))
            self.assertFalse(fake_out.getvalue().__contains__(str(n*11)+"\n"))
            self.assertFalse(fake_out.getvalue().__contains__(str((n*10)+1)+"+\n"))

    def __expected_out(self, n):
        expected_out = ""
        for i in range(1, 11):
            expected_out += str(i * n) + "\n"
        return expected_out


if __name__ == '__main__':
    unittest.main()

