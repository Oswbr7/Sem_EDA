import os
class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def eliminar(self):
        return self.items.pop()

    def tamanio(self):
        return len(self.items)

c=Cola()

def main():
    while True:
        print("1) Agregar a la cola")
        print("2) Eliminar ultimo elemento")
        opc = int(input("Selecciona una opcion: "))
        if opc == 1:
            agrega = int(input("Introduce un numero a la cola: "))
            c.agregar(agrega)
            print("Elementos agregados:")
            print(c.tamanio())
            os.system("pause")
            os.system("cls")
        elif opc == 2:
            c.eliminar()
            os.system("cls")
        else:
            print("Opcion Invalida")
            break

if __name__ == "__main__":
    main()
