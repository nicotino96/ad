import context
import runpy
import unittest


class SumStringAndIntTestCase(unittest.TestCase):

    def test_example2_prints_correct_output(self):
        # Run example2.py as Main
        with self.assertRaises(TypeError):
            runpy.run_module("intro.example2", {}, "__main__")


if __name__ == '__main__':
    unittest.main()
