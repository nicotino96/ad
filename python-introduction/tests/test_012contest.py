import context
import io
import unittest
from unittest.mock import patch
from intro import contest


class ContestBasicTestCase(unittest.TestCase):

    def test_question_output_is_ok(self):
        question = """
¿Cuál es la universidad más antigua de Europa, fundada en 1088, que sigue en funcionamiento actualmente?

a) Universidad de París
b) Universidad de Bolonia
c) Universidad de Oxford    
"""
        self.__verify_question1_output_content("c", question)

    def test_output_with_correct_and_incorrect_answers(self):
        self.__verify_question1_output_content("a", "¡Fallaste! Pero no pasa nada, ¡sigue intentándolo!")
        self.__verify_question1_output_content("b", "¡ENHORABUENA! ¡HAS ACERTADO! Ganaste 159 puntos")

    def __verify_question1_output_content(self, given_answer, expected_out_content):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            contest.make_question()
            self.assertTrue(fake_out.getvalue().__contains__(expected_out_content))


if __name__ == '__main__':
    unittest.main()
