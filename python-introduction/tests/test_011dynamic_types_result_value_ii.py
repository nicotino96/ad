import context
import io
import runpy
import unittest
from contextlib import redirect_stdout


class PrintDentalInsuranceYearlyCostTestCase(unittest.TestCase):

    def test_output_in_example3(self):
        # Run example3.py as Main
        with redirect_stdout(io.StringIO()) as f1:
            runpy.run_module("intro.example3", {}, "__main__")
        console_output1 = f1.getvalue()
        self.assertTrue(console_output1.__contains__("Si contratas la compañía Dientes Baratos S.L., el coste anual será 360 euros"))
        self.assertTrue(console_output1.__contains__("Si contratas la compañía Ratoncito Pérez S.L., el coste anual será 480 euros"))

        from intro import example3
        self.assertEqual(example3.show_annual_cost("Whatever"), None)
        
        # It'd be nice if these two belonged to previous test, but
        # once intro.example3 is imported; runpy.run_module will complain
        # So we assert these two here to prevent line 13 of this file
        # from showing a warning:
        self.assertEqual(example3.dental_insurance_cost("Whatever"), 30)
        self.assertEqual(example3.dental_insurance_cost("Ratoncito Pérez S.L."), "40")


if __name__ == '__main__':
    unittest.main()

