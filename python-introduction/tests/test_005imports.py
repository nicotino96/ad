import context
import io
import unittest
from contextlib import redirect_stdout
from intro import functions


class ImportsTestCase(unittest.TestCase):

    def test_function_exists_and_simple_program_is_correct(self):
        value = functions.get_color()
        self.assertEqual(value, "Verde")

        with redirect_stdout(io.StringIO()) as f:
            from intro import simple_program
        console_output = f.getvalue()

        self.assertTrue(console_output.__contains__("El color es:"))
        self.assertTrue(console_output.__contains__("Verde"))


if __name__ == '__main__':
    unittest.main()
