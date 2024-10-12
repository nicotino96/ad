import context
import io
import unittest
from contextlib import redirect_stdout


class HelloWorldTestCase(unittest.TestCase):

    def test_print(self):
        with redirect_stdout(io.StringIO()) as f:
            from intro import helloworld
        console_output = f.getvalue()

        self.assertTrue(console_output.__contains__("Hello, world!"))


if __name__ == '__main__':
    unittest.main()
