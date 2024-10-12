import context
import io
import unittest
from unittest.mock import patch
from intro import contest


class ContestMathsTestCase(unittest.TestCase):

    def test_question_output_is_ok(self):
        question2 = """
¿Cuál es el resultado de SUMAR estos dos números?
434
493
"""
        self.__verify_question2_output_content("10", question2)

    def test_output_with_correct_and_incorrect_answers(self):
        value1 = 434
        value2 = 493
        correct_value = value1 + value2
        incorrect_value = value1 + value2 + 1
        self.__verify_question2_output_content(str(incorrect_value), "Parece que esa respuesta no es correcta, ¡no te rindas!")
        self.__verify_question2_output_content(str(correct_value), "¡Una mente privilegiada para el cálculo!")

    def test_output_with_invalid_number(self):
        responses = ["hola", "caracola", 500]
        self.__verify_question2_output_content_with_side_effect_input(responses, "¡No has introducido un número válido!")

    def __verify_question2_output_content(self, given_answer, expected_out_content):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            contest.make_question2()
            self.assertTrue(fake_out.getvalue().__contains__(expected_out_content))

    def __verify_question2_output_content_with_side_effect_input(self, side_effect, expected_out_content):
        with patch('builtins.input', side_effect=side_effect), patch('sys.stdout', new=io.StringIO()) as fake_out:
            contest.make_question2()
            self.assertTrue(fake_out.getvalue().__contains__(expected_out_content))


if __name__ == '__main__':
    unittest.main()
