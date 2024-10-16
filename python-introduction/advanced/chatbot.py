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