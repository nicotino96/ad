import context
import io
import random
import runpy
import unittest
from unittest.mock import patch


class ChatBotExampleMethodsTestCase(unittest.TestCase):

    def test_method_one_param_exists_and_is_invoked_in_run_example(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            runpy.run_module("advanced.run_class_example", {}, "__main__")
            self.assertTrue(fake_out.getvalue().__contains__("Tu número es: " + str(45)))

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            from advanced import chatbot
            chatbot.ChatBot().test_one_param(0)
            self.assertTrue(fake_out.getvalue().__contains__("Tu número es: 0"))

    def test_method_two_params_exists_and_is_invoked_in_run_example(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            from advanced import chatbot
            random1 = random.randint(1, 50)
            random2 = random.randint(1, 50)
            chatbot.ChatBot().substract_numbers(random1, random2)
            self.assertTrue(fake_out.getvalue().__contains__(str(random2 - random1)))


if __name__ == '__main__':
    unittest.main()
