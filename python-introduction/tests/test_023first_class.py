import context
import io
import runpy
import unittest
from unittest.mock import patch


class ChatBotSimpleMethodTestCase(unittest.TestCase):

    def test_method_exists_and_is_invoked_in_run_example(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            runpy.run_module("advanced.run_class_example", {}, "__main__")
            self.assertTrue(fake_out.getvalue().__contains__("¡Hola!"))

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            from advanced import chatbot
            chatbot.ChatBot().test_hello()
            self.assertTrue(fake_out.getvalue().__contains__("¡Hola!"))


if __name__ == '__main__':
    unittest.main()

