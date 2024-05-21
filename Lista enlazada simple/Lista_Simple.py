import os
class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente



class ListaSimple(Nodo):

    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
            return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                if encontrado == True:
                    print("Elemento encontrado")
            else:
                actual = actual.obtenerSiguiente()
                print("Elemento inexistente")

        return encontrado

    def eliminar(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())

L=ListaSimple()
def main():
    while True:
        print("1) Agregar elemento")
        print("2) Buscar elemento")
        print("3) Eliminar elemento de la lista")
        opc = int(input("Selecciona una opcion: "))
        if opc == 1:
            agrega = int(input("Introduce un elemento numerico: "))
            L.agregar(agrega)
            os.system("pause")
            os.system("cls")
        elif opc == 2:
            busca = int(input("Introduce numero a buscar: "))
            L.buscar(busca)
            print("Busqueda exitosa")
            os.system("pause")
            os.system("cls")
        elif opc == 3:
            elimina = int(input("Ingresa numero a eliminar: "))
            L.eliminar(elimina)
            print("Proceso realizado con exito")
            os.system("pause")
            os.system("cls")
        else:
            print("Opcion Invalida")
            break

if __name__ == "__main__":
    main()
