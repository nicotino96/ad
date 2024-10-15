def simple_for():
    for i in range(69):
        print(i)
def simple_for_begin():
    for i in range(60, 109):
        print(i)
def simple_for_increment():
    for i in range(60, 109, 3):
        print(i)
def multiples():
    for i in range(31,57):
        if i%3==0:
            print(i)
def multiplication_table(numero):
    for i in range(1,11):
        print(numero*i)
def find_dino(dinosaurioBusq):
    dinosaurios=["Triceratops", "Tiranosaurio", "Diplodocus", "Pterodáctilo", "Cuellilargo"]
    for dinosaurio in dinosaurios:
        if dinosaurio == dinosaurioBusq:
            return True
    return False
if __name__ == '__main__':
    simple_for()
