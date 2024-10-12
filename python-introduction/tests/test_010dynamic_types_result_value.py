import context
import io
import runpy
import unittest
from contextlib import redirect_stdout


class PrintDentalInsuranceTestCase(unittest.TestCase):

    def test_output_in_example3(self):
        # Run example3.py as Main
        with redirect_stdout(io.StringIO()) as f1:
            runpy.run_module("intro.example3", {}, "__main__")
        console_output1 = f1.getvalue()
        c_name = "Dientes Sanos S.L."
        self.assertTrue(console_output1.__contains__("Tu seguro dental con la compañía " + c_name + " cuesta 30 euros al mes"))


if __name__ == '__main__':
    unittest.main()
