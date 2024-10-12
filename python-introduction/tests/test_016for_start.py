import context
import io
import unittest
from unittest.mock import patch
from advanced import loops


class StartForTestCase(unittest.TestCase):

    def test_simple_for_output_is_ok(self):
        expected_output = ""
        range_start = 60
        i = 0
        for i in range(range_start, 109):
            expected_output += str(i) + "\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            loops.simple_for_begin()
            self.assertTrue(fake_out.getvalue().__contains__(expected_output))
            self.assertFalse(fake_out.getvalue().__contains__(str(i+1)))
            self.assertFalse(fake_out.getvalue().__contains__(str(range_start-1)))


if __name__ == '__main__':
    unittest.main()
