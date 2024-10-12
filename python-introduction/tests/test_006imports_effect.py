import context
import io
import runpy
import unittest
from contextlib import redirect_stdout


class GreeterTestCase(unittest.TestCase):

    def test_greeter_wont_autoprint_and_outputs_expected(self):
        # Run greeter.py as Main
        with redirect_stdout(io.StringIO()) as f1:
            runpy.run_module("intro.greeter", {}, "__main__")
        console_output1 = f1.getvalue()
        self.assertTrue(console_output1.__contains__("Good morning! I hope you enjoy your day!"))

        # Import greeter.py
        with redirect_stdout(io.StringIO()) as f2:
            from intro import greeter
        console_output2 = f2.getvalue()
        self.assertEqual(len(console_output2), 0)
        self.assertEqual(greeter.good_morning(), "Good morning! I hope you enjoy your day!")

        # Run other_program.py as __main__
        with redirect_stdout(io.StringIO()) as f3:
            runpy.run_module("intro.other_program", {}, "__main__")
        console_output3 = f3.getvalue()
        self.assertTrue(console_output3.__contains__("I wish I could say good morning..."))
        self.assertTrue(console_output3.__contains__("Wait, I can!"))
        self.assertTrue(console_output3.__contains__("Good morning! I hope you enjoy your day!"))


if __name__ == '__main__':
    unittest.main()

