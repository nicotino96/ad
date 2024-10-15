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
def find_dino2(dinosaur):
    return dinosaur in ["Triceratops", "Diplodocus", "Pterodáctilo"]
def example_list_size():
    list1 = ["Alice", "Bob"]
    size1 = len(list1)
    print("El tamaño de la primera lista es: " + str(size1))

    list2 = [None, None, None, None, None]
    size2 = len(list2)
    print("El tamaño de la segunda lista es: " + str(size2))

    list3 = [[1, 2], [3, 4]]
    size3 = len(list3)
    print("El tamaño de la tercera lista es: " + str(size3))
def retrieve_value(indice):
    lista=[4,8,-35,"Pepe Depura",12]
    if 0 <= indice <= len(lista):
        return lista[indice]
    else:
        return None

if __name__ == '__main__':
    simple_for()
