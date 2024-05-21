nombre = input("Dame el nombre del archivo a procesar: ")+".txt"
archivo = open("Archivo.txt", 'r')
contador = 0
caracter = archivo.read(1)

while(caracter != ''):
    contador += 1
    caracter = archivo.read(1)

archivo.close()
print("El numero de caracteres es: ")
print(contador)
