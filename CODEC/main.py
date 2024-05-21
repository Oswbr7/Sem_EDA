import os

def main():
        #nombre = input("Ingrese el nombre del archivo: ")+".txt"
        while True:
                print("\n1)Codificar texto")
                print("2)Decodificar texto")
                opc = int(input("Selecciona una opcion: "))
                if opc == 1:
                        archivo = open("prueba",'r')
                        caracter = archivo.read(1)
                        while caracter != "":
                                if caracter.isalpha():
                                    if caracter.islower():
                                        if caracter == 'z':
                                            caracter = 'a'
                                        else:
                                            caracter = chr(ord(caracter) + 1)
                                print(caracter,end="")
                                caracter = archivo.read(1)
                        archivo.close()
                        os.system("pause")
                        os.system("cls")
                elif opc == 2:
                        if os.path.exists("Codificado.txt"):
                                archivo2 = open("Codificado", "r")
                                caracter = archivo2.read(1)
                                while caracter != "":
                                        if caracter.isalpha():
                                            if caracter.islower():
                                                caracter = chr(ord(caracter) - 1)
                                                #if caracter == 'z':
                                                    #caracter = 'a'
                                                #    caracter = chr(ord(caracter) - 1)
                                                #else:
                                                #    caracter = chr(ord(caracter) - 1)
                                        print(caracter,end="")
                                        caracter = archivo2.read(1)
                                archivo2.close()
                                os.system("pause")
                                os.system("cls")

                else:
                    os.system("cls")
                    print("Opcion invalida")
                    os.system("pause")
                    os.system("cls")
                    break
        
if __name__ == "__main__":
    main()
