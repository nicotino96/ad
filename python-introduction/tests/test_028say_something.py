import context
import io
import unittest
from unittest.mock import patch
from advanced import chatbot


class ChatBotNiceConversationTestCase(unittest.TestCase):
    __fake_input_call_count = 0

    def setUp(self): # Executed before EACH test
        self.__fake_input_call_count = 0

    def test_output_correct_batch1(self):
        with patch('builtins.input', self.__fake_input_batch1), patch('sys.stdout', new=io.StringIO()) as fake_out:
            c = chatbot.ChatBot()
            c.begin_conversation()
            self.assertTrue(fake_out.getvalue().__contains__("(Cuando quieras despedirte, di 'salir')"))
            self.assertTrue(fake_out.getvalue().__contains__("¿No crees que el amor y el odio están separados por una delgada línea?"))
            self.assertTrue(fake_out.getvalue().__contains__("Apagar, encender,... Qué más da"))
            self.assertTrue(fake_out.getvalue().__contains__("Para mí una casa es un montón de circuitos"))
            self.assertTrue(fake_out.getvalue().__contains__("Ojalá yo pudiera ver los colores"))
            self.assertTrue(fake_out.getvalue().__contains__("Vaya..."))
            self.assertTrue(fake_out.getvalue().__contains__("¡Hasta pronto!"))

    def test_output_correct_batch2(self):
        with patch('builtins.input', self.__fake_input_batch2), patch('sys.stdout', new=io.StringIO()) as fake_out:
            c = chatbot.ChatBot()
            c.begin_conversation()
            self.assertTrue(fake_out.getvalue().__contains__("(Cuando quieras despedirte, di 'salir')"))
            self.assertTrue(fake_out.getvalue().__contains__("Si hay algo que sé es que el dinero no da la felicidad. Y no sé mucho..."))
            self.assertTrue(fake_out.getvalue().__contains__("Yo no hago favores"))
            self.assertTrue(fake_out.getvalue().__contains__("Los humanos siempre estáis con vuestras cosas"))
            self.assertTrue(fake_out.getvalue().__contains__("¿Inteligencia? No me hables de inteligencia..."))
            self.assertTrue(fake_out.getvalue().__contains__("Vaya..."))
            self.assertTrue(fake_out.getvalue().__contains__("¡Hasta pronto!"))

    def test_output_correct_batch3(self):
        with patch('builtins.input', self.__fake_input_batch3), patch('sys.stdout', new=io.StringIO()) as fake_out:
            c = chatbot.ChatBot()
            c.begin_conversation()
            self.assertTrue(fake_out.getvalue().__contains__("(Cuando quieras despedirte, di 'salir')"))
            self.assertTrue(fake_out.getvalue().__contains__("Para cosas interesantes, el Discovery Channel"))
            self.assertTrue(fake_out.getvalue().__contains__("¿Has visto la película Terminator? Quizá deberías..."))
            self.assertTrue(fake_out.getvalue().__contains__("Los ordenadores son máquinas muy útiles"))
            self.assertTrue(fake_out.getvalue().__contains__("Vaya..."))
            self.assertTrue(fake_out.getvalue().__contains__("¡Hasta pronto!"))

    def test_output_correct_batch4(self):
        with patch('builtins.input', self.__fake_input_batch4), patch('sys.stdout', new=io.StringIO()) as fake_out:
            c = chatbot.ChatBot()
            c.begin_conversation()
            self.assertTrue(fake_out.getvalue().__contains__("(Cuando quieras despedirte, di 'salir')"))
            self.assertTrue(fake_out.getvalue().__contains__("Tu lavadora también tiene programas, ¿lo sabías?"))
            self.assertTrue(fake_out.getvalue().__contains__("Querer es una palabra con un significado muy amplio"))
            self.assertTrue(fake_out.getvalue().__contains__("Vaya..."))
            self.assertTrue(fake_out.getvalue().__contains__("¡Hasta pronto!"))

    def __fake_input_batch1(self, value):
        return self.__fake_input(value, ["Te amo", "Te voy a apagar", "Vete a casa", "Qué colorido", "Ostras tú", "salir"])

    def __fake_input_batch2(self, value):
        return self.__fake_input(value, ["Es dinero", "Por favor", "Eres humano", "Qué inteligencia", "Ostras tú", "salir"])

    def __fake_input_batch3(self, value):
        return self.__fake_input(value, ["Qué interesante", "Maldita máquina", "Ordenador, ordenador....", "Ostras tú", "salir"])

    def __fake_input_batch4(self, value):
        return self.__fake_input(value, ["Qué programa", "Te quiero", "Ostras, vaya", "salir"])

    def __fake_input(self, value, side_effects):
        self.assertEqual("Tú dices: ", value)
        self.__fake_input_call_count += 1
        return side_effects[self.__fake_input_call_count - 1]


if __name__ == '__main__':
    unittest.main()
