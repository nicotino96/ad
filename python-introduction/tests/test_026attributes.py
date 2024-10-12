import context
import unittest
from advanced import chatbot


class ChatBotSimpleConstructorTestCase(unittest.TestCase):

    def test_constructor_name_exists(self):
        t = chatbot.ChatBot()
        self.assertEqual(t.name, "Atlas")


if __name__ == '__main__':
    unittest.main()

