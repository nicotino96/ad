import context
import unittest
from unittest.mock import patch
from intro import contest


class ContestInputWhileTestCase(unittest.TestCase):
    __fake_input_call_count = 0

    def test_output_with_invalid_incorrect_and_correct(self):
        with patch('builtins.input', self.__fake_input):
            contest.make_question()

    def __fake_input(self, value):
        if self.__fake_input_call_count == 0:
            self.assertTrue(value.__contains__("Escoge tu respuesta (a, b ó c)"))
        else:
            self.assertTrue(value.__contains__("Disculpa, escoge una respuesta válida (a, b ó c)"))

        self.__fake_input_call_count += 1
        if self.__fake_input_call_count == 0:
            return "B"
        else:
            return "b"


if __name__ == '__main__':
    unittest.main()
