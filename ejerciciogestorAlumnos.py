import random 
import math

def validarDatos():
    try:
        nombre=input("Ingrese el nombre del estudiante: ")
        while True:
            edad=int(input("Ingrese la edad: "))
            if edad>0:
                break
            else:
                print("Debe ingresar una edad positiva")
        notaEP=random.randint(0,201)/10
        notaTF=round(random.uniform(0,20.1),2)
        notaEF=random.randint(0,201)/10
        prom=(notaEP*0.30+notaTF*0.2+notaEF*0.50)
        alumno=[nombre,edad,notaEP,notaTF,notaEF,prom]
        return alumno
    except ValueError:
        print("Error al ingresar los datos")
        return []
    

def agregarAlumno(listaAlumnos):
    alumno=validarDatos()
    if alumno!=[]:
        #Agregamos al alumnos la lista principal
        listaAlumnos.append(alumno)
        print("ALUMNOS REGISTRADO OK\n")
    else:
        print("ALUMNO NO REGISTRADO!!!!")
     
def mostrarAlumnos(listaAlumnos):
    print("ID\t\tNombre\t\tEdad\t\tNotaEP\t\tnotaTF\t\tnotaEF\t\tPromedio")
    for i,alumno in enumerate(listaAlumnos):
        print(f"{i+1}\t\t{alumno[0]}\t\t{alumno[1]}\t\t{alumno[2]}\t\t{alumno[3]}\t\t{alumno[4]}\t\t{alumno[5]}")
    



def menu():
     print("\n--------------------------------------")
     print("==== REGISTRO DE ALUMNOS ====")
     print("[1] Agregar Alumno")
     print("[2] Insertar en posición")
     print("[3] Eliminar por nombre o indice")
     print("[4] Buscar alumno")
     print("[5] Actualizar registro")
     print("[6] Listar alumnos")
     print("[7] Generar estadísticas")
     print("[8] Salir")
     op=int(input("Seleccione una opçión---> "))
     print()
     return op



if __name__=="__main__":
    listaAlumnos=[] #lista global
    while True:
        try:
            op=menu()
            match(op):
                case 1: agregarAlumno(listaAlumnos)
                case 2: insertarEnPosicion(listaAlumnos)
                case 3: eliminarAlumno(listaAlumnos)
                case 4: buscarAlumno(listaAlumnos)
                case 5: actualizarDatos(listaAlumnos)
                case 6: mostrarAlumnos(listaAlumnos)
                case 7: generarEstadisticas(listaAlumnos)
                case 8: 
                        print("------- FIN DEL PROGRAMA -------")
                        break
                case _:
                        print("Debe ingresar una opción valida")
        except ValueError:
            print("Debe ingresar un valor numérico")


