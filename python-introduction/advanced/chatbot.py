class ChatBot:
    def __init__(self):
        print("ChatBot activado")
        self.name="Atlas"



    def test_hello(self):
        print("¡Hola!")

    def test_one_param(self, number):
        print("Tu número es: " + str(number))

    def substract_numbers(self,number1,number2):
        print(number1-number2)

    def begin_conversation(self):
        print(self.name + " dice:")
        print("¡Hola! Soy " + self.name + ". ¿De qué quieres hablar?")
        print("(Cuando quieras despedirte, di 'salir')")
        print("")
        user_input = input("Tú dices: ")
        while user_input != "salir":
            print("")
            print(self.name + " dice:")
            print("Vaya...")
            print("")
            user_input = input("Tú dices: ")
        print("")
        print(self.name + " dice:")
        print("¡Hasta pronto!")

if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.begin_conversation()
