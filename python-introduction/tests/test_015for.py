import context
import io
import unittest
from unittest.mock import patch
from advanced import loops


class SimpleForTestCase(unittest.TestCase):

    def test_simple_for_output_is_ok(self):
        expected_output = ""
        for i in range(68):
            expected_output += str(i) + "\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            loops.simple_for()
            self.assertTrue(fake_out.getvalue().__contains__(expected_output))
            self.assertFalse(fake_out.getvalue().__contains__(str(i+2)))


if __name__ == '__main__':
    unittest.main()

