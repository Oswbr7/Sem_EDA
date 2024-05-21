class Complejo:
    #Atributos de la clase
    Preal = 0
    Pimaginaria = 0

    #Constructor de la clase
    def __init__(self, real, imaginaria):
        self.Preal = real
        self.Pimaginaria = imaginaria

    def __add__(self,N3):
        return Complejo(self.Preal + N3.Preal, self.Pimaginaria + N3.Pimaginaria)

    def __sub__(self,N4):
        return Complejo(self.Preal - N4.Preal, self.Pimaginaria - N4.Pimaginaria)

    def __mul__(self,N5):
        return Complejo(self.Preal * N5.Preal, self.Pimaginaria * N5.Pimaginaria)

    def __truediv__(self,N6):
        return Complejo(self.Preal / N6.Preal, self.Pimaginaria / N6.Pimaginaria)

    #Metodo de la clase (imprimir el numero complejo)
    def imprimirC(self):
        print(str(self.Preal) + " + " + str(self.Pimaginaria) + "i")

    def imprimirC1(self):
        print(str(self.Preal) + " - " + str(self.Pimaginaria) + "i")


Numero1 = Complejo(2, 5)
Numero2 = Complejo(3, 6)

print("Los numeros son: ")
Numero1.imprimirC()
Numero2.imprimirC()

print("Suma")
Numero = Numero1 + Numero2
Numero.imprimirC()

print("Resta")
Numero = Numero1 - Numero2
Numero.imprimirC1()

print("Multiplicacion")
Numero = Numero1 * Numero2
Numero.imprimirC()

print("Division")
Numero = Numero1 / Numero2
Numero.imprimirC()
