import os
class Estudiante:
    def __init__(self, nombre, codigo, carrera):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
    def toSTR(self):
        return str(self.codigo+'\t'+self.nombre+'\t'+self.carrera+'\n')
def main():
    #nombre = input("Introduce el nombre del archivo: ")+".txt"
    while True:
        print("1- Mostrar todos los estudiantes")
        print("2- Agregar estudiantes")
        opc = int(input("Selecciona una opcion: "))
        if opc == 1:
            #archivo = open(nombre, 'r')
            archivo = open("agenda", "r")
            for linea in archivo:
                print(linea)
            archivo.close()
            os.system("pause")
            os.system("cls")

        elif opc == 2:
            archivo = open("agenda",'a')
            #archivo = open("agenda", "r")
            nomAlumno = input("Introduce el nombre del alumno: ")
            codAlumno = input("Introduce el código del alumno: ")
            carAlumno = input("introduce la carrera del alumno: ")
            archivo.write(Estudiante(nomAlumno,codAlumno,carAlumno).toSTR())
            archivo.close()
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
