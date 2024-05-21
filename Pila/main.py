import os
class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def eliminar(self):
        return self.items.pop(0)

    def inspeccionar(self):
        return self.items[0]
    
    def tamanio(self):
        return len(self.items)

p = Pila()

def main():
    while True:
        print("1) Agregar a la pila")
        print("2) Eliminar ultimo elemento")
        opc = int(input("Selecciona una opcion: "))
        if opc == 1:
            agrega = int(input("Introduce un numero a la pila: "))
            p.agregar(agrega)
            print("Elementos agregados:")
            print(p.tamanio())
            os.system("pause")
            os.system("cls")
        elif opc == 2:
            p.eliminar()
            os.system("cls")
        else:
            print("Opcion Invalida")
            break

if __name__ == "__main__":
    main()
