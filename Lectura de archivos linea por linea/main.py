import os
if os.path.exists("Archivo.txt"):
    archivo = open("Archivo.txt", "r")

    for linea in archivo:
        print(linea)

    archivo.close()
else:
    print("El archivo no existe")
