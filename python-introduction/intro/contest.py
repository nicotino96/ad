def make_question():
    question = """
¿Cuál es la universidad más antigua de Europa, fundada en 1088, que sigue en funcionamiento actualmente?

a) Universidad de París
b) Universidad de Bolonia
c) Universidad de Oxford    
"""
    print(question)
    choice=""
    while choice not in ['a', 'b', 'c']:
        choice = input("Escoge tu respuesta (a, b ó c): ")
        if choice == 'b':
            print("¡ENHORABUENA! ¡HAS ACERTADO! Ganaste 159 puntos")
        else:
            print("¡Fallaste! Pero no pasa nada, ¡sigue intentándolo!")

def make_question2():
    question2 = """
¿Cuál es el resultado de SUMAR estos dos números?
434
493
"""
    print(question2)
    answer = None
    while answer is None:  # Se prefiere 'is' a '==' para comparar con None
        try:
            answer = int(input("Dime tu respuesta: "))
        except ValueError:
            print("¡No has introducido un número válido!")
    if answer == (434+493):
        print("¡Una mente privilegiada para el cálculo!")
    else:
        print("Parece que esa respuesta no es correcta, ¡no te rindas!")



if __name__ == '__main__':
    make_question()
    make_question2()
