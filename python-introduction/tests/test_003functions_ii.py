import context
import io
import unittest
from contextlib import redirect_stdout
from intro import functions


class MoreFunctionsTestCase(unittest.TestCase):

    def test_more_functions(self):
        with redirect_stdout(io.StringIO()) as f:
            functions.small_print()
        console_output = f.getvalue()

        self.assertTrue(console_output.__contains__("James Watt patentó en 1769 la máquina de vapor"))
        self.assertEqual(functions.lucky_number(), 63)


if __name__ == '__main__':
    unittest.main()
