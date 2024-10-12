import context
import io
import runpy
import unittest
from contextlib import redirect_stdout


class SumTwoNumbersTestCase(unittest.TestCase):

    def test_maths_behaves_as_expected(self):
        # Run maths.py as Main
        with redirect_stdout(io.StringIO()) as f1:
            runpy.run_module("intro.maths", {}, "__main__")
        console_output1 = f1.getvalue()
        value1 = 3
        value2 = 48
        value_sum = int(console_output1)
        self.assertEqual(value_sum, value1 + value2)

        # Import maths.py
        with redirect_stdout(io.StringIO()) as f2:
            from intro import maths
        console_output2 = f2.getvalue()
        self.assertEqual(len(console_output2), 0)
        self.assertEqual(maths.sum_two_numbers(11, -5), 6)

    def test_evaluate_student_behaves_as_expected(self):
        # Run evaluate_student.py as __main__
        with redirect_stdout(io.StringIO()) as f3:
            runpy.run_module("intro.evaluate_student", {}, "__main__")
        console_output3 = f3.getvalue()
        p_note = 4
        t_note = 3
        self.assertTrue(console_output3.__contains__("La nota de prácticas es:"))
        self.assertTrue(console_output3.__contains__(str(p_note)))
        self.assertTrue(console_output3.__contains__("La nota de teoría es:"))
        self.assertTrue(console_output3.__contains__(str(t_note)))
        self.assertTrue(console_output3.__contains__("Nota final:"))
        self.assertTrue(console_output3.__contains__(str(p_note + t_note)))

        # Import evaluate_student.py
        with redirect_stdout(io.StringIO()) as f2:
            from intro import evaluate_student
        console_output2 = f2.getvalue()
        self.assertEqual(len(console_output2), 0)


if __name__ == '__main__':
    unittest.main()
