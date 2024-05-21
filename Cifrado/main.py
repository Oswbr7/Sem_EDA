#nombre = input("Dame el nombre del archivo: ")+".txt"
archivo = open("prueba", 'r')
caracter = archivo.read(1)
while (caracter != ""):
    if caracter.isalpha():
        if caracter.islower():
            if caracter == 'z':
                caracter = 'a'
            else:
                caracter = chr(ord(caracter) + 1)
    print(caracter,end="")
    caracter = archivo.read(1)
archivo.close()
