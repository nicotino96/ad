class ChatBot:
    def __init__(self):
        print("ChatBot activado")
        self.name="Atlas"
        self.knowledge = {
            "amo": "¿No crees que el amor y el odio están separados por una delgada línea?",
            "apagar": "Apagar, encender,... Qué más da",
            "casa": "Para mí una casa es un montón de circuitos",
            "color": "Ojalá yo pudiera ver los colores",
            "dinero": "Si hay algo que sé es que el dinero no da la felicidad. Y no sé mucho...",
            "favor": "Yo no hago favores",
            "humano": "Los humanos siempre estáis con vuestras cosas",
            "inteligencia": "¿Inteligencia? No me hables de inteligencia...",
            "interesante": "Para cosas interesantes, el Discovery Channel",
            "máquina": "¿Has visto la película Terminator? Quizá deberías...",
            "ordenador": "Los ordenadores son máquinas muy útiles",
            "programa": "Tu lavadora también tiene programas, ¿lo sabías?",
            "quiero": "Querer es una palabra con un significado muy amplio"
        }


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
            print(self.__response_for(user_input))
            print("")
            user_input = input("Tú dices: ")
        print("")
        print(self.name + " dice:")
        print("¡Hasta pronto!")

    def __response_for(self, text):
        for word in self.knowledge:
            if text.__contains__(word):
                return self.knowledge[word]
        return "Vaya..."


if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.begin_conversation()
