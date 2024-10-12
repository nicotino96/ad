import context
import io
import unittest
from contextlib import redirect_stdout
from intro import functions


class FirstFunctionsTestCase(unittest.TestCase):

    def test_functions(self):
        with redirect_stdout(io.StringIO()) as f:
            functions.do_nothing()
            functions.do_something()
            functions.return_something()
        console_output = f.getvalue()

        self.assertTrue(console_output.__contains__("I'm doing something"))
        self.assertEqual(functions.do_nothing(), None)
        self.assertEqual(functions.do_something(), None)
        self.assertEqual(functions.return_something(), 47)


if __name__ == '__main__':
    unittest.main()
