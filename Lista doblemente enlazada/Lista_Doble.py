import os
class Nodo:
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None



class ListaDoble(Nodo):

    def __init__(self):
        self.cabeza = None


    def AgregarVacia(self, datoInicial):
        if self.cabeza is None:
            NuevoNodo = Nodo(datoInicial)
            self.cabeza = NuevoNodo
        else:
            print("La lista no esta vacia")

    def AgregaInicio(self, datoInicial):
        if self.cabeza is None:
            NuevoNodo = Nodo(datoInicial)
            self.cabeza = NuevoNodo
            print("Nodo agregado")
            return
        NuevoNodo = Nodo(datoInicial)
        NuevoNodo.siguiente = self.cabeza
        self.cabeza.anterior = NuevoNodo
        self.cabeza = NuevoNodo

    def AgregaFinal(self, datoInicial):
        if self.cabeza is None:
            NuevoNodo = Nodo(datoInicial)
            self.cabeza = NuevoNodo
            return
        n = self.cabeza
        while n.siguiente is not None:
            n = n.siguiente
        NuevoNodo = Nodo(datoInicial)
        n.siguiente = NuevoNodo
        NuevoNodo.anterior = n

    def AgregaDespues(self, x, datoInicial):
        if self.cabeza is None:
            print("Lista vacia")
            return
        else:
            n = self.cabeza
            while n is not None:
                if n.dato == x:
                    break
                n = n.siguiente
            if n is None:
                print("Elemento inexistente en la lista")
            else:
                NuevoNodo = Nodo(datoInicial)
                NuevoNodo.anterior = n
                NuevoNodo.siguiente = n.siguiente
                if n.siguiente is not None:
                    n.siguiente.prev = NuevoNodo
                n.siguiente = NuevoNodo

    def AgregaAntes(self, x, datoInicial):
        if self.cabeza is None:
            print("Lista vacia")
            return
        else:
            n = self.cabeza
            while n is not None:
                if n.dato == x:
                    break
                n = n.siguiente
            if n is None:
                print("Elemento inexistente en la lista")
            else:
                NuevoNodo = Nodo(datoInicial)
                NuevoNodo.siguiente = n
                NuevoNodo.anterior = n.anterior
                if n.anterior is not None:
                    n.anterior.siguiente = NuevoNodo
                n.anterior = NuevoNodo

    def Imprimir(self):
        if self.cabeza is None:
            print("Lista vacia")
            return
        else:
            n = self.cabeza
            while n is not None:
                print(n.dato , " ")
                n = n.siguiente

    def EliminaInicio(self):
       if self.cabeza is None:
            print("Lista vacia, no se pueden eliminar elementos")
            return
       if self.cabeza.siguiente is None:
            self.cabeza = None
            return
       self.cabeza = self.cabeza.siguiente
       self.inicioAnterior = None;
       print("Eliminado con exito")

    def EliminaFinal(self):
        if self.cabeza is None:
            print("Lista vacia, no se pueden eliminar elementos")
            return 
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        n = self.cabeza
        while n.siguiente is not None:
            n = n.siguiente
        n.anterior.siguiente = None

    def EliminarValor(self, x):
        if self.cabeza is None:
            print("Lista vacia, no se pueden eliminar elementos")
            return 
        if self.cabeza.siguiente is None:
            if self.cabeza.dato == x:
                self.cabeza = None
            else:
                print("Dato no encontrado")
            return 

        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            return

        n = self.cabeza
        while n.siguiente is not None:
            if n.dato == x:
                break;
            n = n.siguiente
        if n.siguiente is not None:
            n.anterior.siguiente = n.siguiente
            n.siguiente.anterior = n.anterior
        else:
            if n.dato == x:
                n.anterior.siguiente = None
            else:
                print("Elemento no encontrado")

L=ListaDoble()
def main():
    while True:
        print("**-Menu Lista Doblemente Enlazada-**")
        print("1) Agregar elemento en lista vacia")
        print("2) Agregar elemento al inicio de la lista")
        print("3) Agregar elemento al final de la lista")
        print("4) Agregar elemento despues de otro elemento")
        print("5) Agregar elemento antes de otro elemento")
        print("6) Eliminar elemento al inicio de la lista")
        print("7) Eliminar elemento al final de la lista")
        print("8) Eliminar elemento por valor asignado")
        opc = int(input("Selecciona una opcion: "))
        
        if opc == 1:
            agrega_vacia = int(input("Introduce un elemento numerico: "))
            L.AgregarVacia(agrega_vacia)
            print("Elemento agregado: ")
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 2:
            agrega_inicio = int(input("Introduce un elemento numerico: "))
            L.AgregaInicio(agrega_inicio)
            print("Elemento agregado: ")
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 3:
            agrega_final = int(input("Introduce un elemento numerico: "))
            L.AgregaInicio(agrega_final)
            print("Elemento agregado: ")
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 4:
            agrega_despues = int(input("Introduce el numero que quieres agregar: "))
            agrega_despues2 = int(input("Introduce el numero que quieres recorrer: "))
            L.AgregaDespues(agrega_despues2, agrega_despues)
            print("Agregado con exito")
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 5:
            agrega_antes = int(input("Introduce el numero que quieres agregar: "))
            agrega_antes2 = int(input("Introduce el numero que quieres recorrer: "))
            L.AgregaAntes(agrega_antes2, agrega_antes)
            print("Agregado con exito")
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 6:
            print("Se eliminara el elemento del inicio de la lista")
            L.EliminaInicio()
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 7:
            print("Se eliminara el elemento del final de la lista")
            L.EliminaFinal()
            L.Imprimir()
            os.system("pause")
            os.system("cls")
        elif opc == 8:
            elimina = int(input("Ingresa el numero que se quiere eliminar: "))
            L.EliminarValor(elimina)
            L.Imprimir()
            print("Elemento eliminado")
            os.system("pause")
            os.system("cls") 
        else:
            print("Opcion Invalida")
            break

if __name__ == "__main__":
    main()

