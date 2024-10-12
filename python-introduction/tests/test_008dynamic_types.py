import context
import io
import runpy
import unittest
from contextlib import redirect_stdout


class SumTwoStringsTestCase(unittest.TestCase):

    def test_example_prints_correct_output(self):
        # Run example.py as Main
        with redirect_stdout(io.StringIO()) as f1:
            runpy.run_module("intro.example", {}, "__main__")
        console_output1 = f1.getvalue()
        value1 = "Hiper"
        value2 = "Rayo"
        self.assertTrue(console_output1.__contains__(value1 + value2))


if __name__ == '__main__':
    unittest.main()
