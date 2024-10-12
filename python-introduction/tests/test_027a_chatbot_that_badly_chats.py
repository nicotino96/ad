import context
import io
import unittest
from unittest.mock import patch
from advanced import chatbot


class ChatBotStupidConversationTestCase(unittest.TestCase):
    __fake_input_call_count = 0

    def test_output_with_invalid_incorrect_and_correct(self):
        with patch('builtins.input', self.__fake_input), patch('sys.stdout', new=io.StringIO()) as fake_out:
            c = chatbot.ChatBot()
            c.begin_conversation()
            self.assertTrue(fake_out.getvalue().__contains__("dice:"))
            self.assertTrue(fake_out.getvalue().__contains__("¿De qué quieres hablar?"))
            self.assertTrue(fake_out.getvalue().__contains__("(Cuando quieras despedirte, di 'salir')"))
            self.assertTrue(fake_out.getvalue().__contains__("Vaya..."))
            self.assertTrue(fake_out.getvalue().__contains__("¡Hasta pronto!"))

    def __fake_input(self, value):
        self.assertEqual("Tú dices: ", value)
        self.__fake_input_call_count += 1
        if self.__fake_input_call_count > 1:
            return "salir"
        else:
            return "Hola"


if __name__ == '__main__':
    unittest.main()
