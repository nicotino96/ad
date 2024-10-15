def make_question():
    question = """
¿Cuál es la universidad más antigua de Europa, fundada en 1088, que sigue en funcionamiento actualmente?

a) Universidad de París
b) Universidad de Bolonia
c) Universidad de Oxford    
"""
    print(question)
    choice = input("Escoge tu respuesta (a, b ó c): ")
    if choice == 'b':
        print("¡ENHORABUENA! ¡HAS ACERTADO! Ganaste 159 puntos")
    else:
        print("¡Fallaste! Pero no pasa nada, ¡sigue intentándolo!")

if __name__ == '__main__':
    make_question()
