class Estudiante:
    def __init__(self, nombre, codigo, carrera):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
    def toSTR(self):
        return str(self.codigo+'\t'+self.nombre+'\t'+self.carrera+'\n')
def main():
    nombre = input("Introduce el nombre del archivo: ")+".txt"
    while True:
        print("1- Mostrar todos los estudiantes")
        print("2- Agregar estudiantes")
        opc = int(input("Selecciona una opcion: "))
        if opc == 1:
            print("1- Mostrar")
            print("2- Buscar")
            op = int(input("Selecciona una opcion: "))
            if op == 1:
                archivo = open(nombre,'r')
                for linea in archivo:
                    print(linea)
                archivo.close()
            elif op == 2:
                archivo = open(nombre,'r')
                linea = archivo.readline()
                codigo = input("Inserte el codigo a buscar: ")
                busca = False
                while linea != "":
                    if linea.find(codigo) != -1:
                        print(linea)
                        busca = True
                    else:
                        continue
                    linea = archivo.readline()
                if not busca:
                    print("Alumno buscado inexistente")
            else:
                print("Opcion invalida")

        elif opc == 2:
            archivo = open(nombre,'a')
            nomAlumno = input("Introduce el nombre del alumno: ")
            codAlumno = input("Introduce el código del alumno: ")
            carAlumno = input("introduce la carrera del alumno: ")
            archivo.write(Estudiante(nomAlumno,codAlumno,carAlumno).toSTR())
            archivo.close()


        else:
            print("Opcion invalida")
            break
        
if __name__ == "__main__":
    main()
