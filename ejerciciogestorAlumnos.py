import random 


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
        prom=calcularPromedio(notaEP,notaTF,notaEF)
        alumno=[nombre,edad,notaEP,notaTF,notaEF,prom]
        return alumno
    except ValueError:
        print("Error al ingresar los datos")
        return []
    
def validarPosicion():
    while True:
        try:
            pos=int(input(f"Ingrese una posicion desde 0 hasta {len(listaAlumnos)-1}: "))
            if pos>=0 and pos<len(listaAlumnos):
                break
            else:
                print("Error posición fuera del rango permitido")
        except ValueError:
            print("Debe ingresar un valor numérico")
    return pos

def insertarEnPosicion(listaAlumnos):
    posicion=validarPosicion()
    #Agregamos un nuevo registro en la posición
    alumno=validarDatos()
    if alumno!=[]:
        listaAlumnos.insert(posicion,alumno)
        print(f"ALUMNOS REGISTRADO en posicion {posicion}\n")
    else:
        print("ALUMNO NO REGISTRADO!!!!")

def eliminarAlumno(listaAlumnos):
    try:
        while True:
            opcion=int(input("Desea eliminar [1] Por nombre o [2] Por indice: "))
            if opcion==1 or opcion==2:
                break
            else:
                print("Debe ingresar una opción valida")
        if opcion==1:
            nombreEliminar=input("Ingrese el nombre del registro que sea eliminar: ")
            for alumno in listaAlumnos:
                if alumno[0].lower()==nombreEliminar.lower():
                    print("Encontraro... eliminando registro\n")
                    listaAlumnos.pop(listaAlumnos.index(alumno))
        else:
            pos=validarPosicion()
            listaAlumnos.pop(pos)
            print("Encontraro... eliminando registro\n")
    except ValueError:
        print("Debe ingresar un valor numérico")


def agregarAlumno(listaAlumnos):
    alumno=validarDatos()
    if alumno!=[]:
        #Agregamos al alumnos la lista principal
        listaAlumnos.append(alumno)
        print("ALUMNO REGISTRADO OK\n")
    else:
        print("ALUMNO NO REGISTRADO!!!!")
     
def mostrarAlumnos(listaAlumnos):
    print("ID\t\tNombre\t\tEdad\t\tNotaEP\t\tnotaTF\t\tnotaEF\t\tPromedio")
    for i,alumno in enumerate(listaAlumnos):
        print(f"{i+1}\t\t{alumno[0]}\t\t{alumno[1]}\t\t{alumno[2]}\t\t{alumno[3]}\t\t{alumno[4]}\t\t{alumno[5]}")
    

def buscarAlumno(listaAlumnos):
    try:
        while True:
            opcion=int(input("Desea buscar [1] Por nombre o [2] Por indice: "))
            if opcion==1 or opcion==2:
                break
            else:
                print("Debe ingresar una opción valida")
        if opcion==1:
            nombreEliminar=input("Ingrese el nombre del registro a buscar: ")
            for alumno in listaAlumnos:
                if alumno[0].lower()==nombreEliminar.lower():
                    print(f"Encontrado... en posición {listaAlumnos.index(alumno)}\n")        
        else:
            pos=validarPosicion()
            print(f"Registro Encontrado su nombre es: {listaAlumnos[pos][0]}")
    except ValueError:
        print("Debe ingresar un valor numérico")

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

def actualizarNombre(pos):
    while True:
        try:
            op=int(input("Desea modificar el nombre [1]SI o [2]NO: "))
            if op==1:
                nuevoNombre=input("Ingrese el nombre a actualizar: ")
            else:
                nuevoNombre=listaAlumnos[pos][0]
            if nuevoNombre!="":
                return nuevoNombre
        except ValueError:
            print("Debe ingresar un valor numérico")

def actualizarEdad(pos):
     while True:
        try:
            op=int(input("Desea modificar la edad [1]SI o [2]NO: "))
            if op==1:
                nuevaEdad=int(input("Ingrese la edad a actualizar: "))
                if nuevaEdad>0:
                    return nuevaEdad
                else:
                    print("Edad fuera del rango")
            else:
                nuevaEdad=listaAlumnos[pos][1]
            if nuevaEdad!="":
                return nuevaEdad
        except ValueError:
            print("Debe ingresar un valor numérico")

def actualizarNota(pos,mensaje,j):
     while True:
        try:
            op=int(input(f"Desea modificar la nota {mensaje} [1]SI o [2]NO: "))
            if op==1:
                nuevaNota=float(input("Ingrese la edad a actualizar: "))
                if nuevaNota>=0 and nuevaNota<=20:
                    return nuevaNota
                else:
                    print("Debe ingresar una nota valida")
            else:
                nuevaNota=listaAlumnos[pos][j]
            if nuevaNota!="":
                return nuevaNota
        except ValueError:
            print("Debe ingresar un valor numérico")

def calcularPromedio(notaEP,notaTF,notaEF):
    return round((notaEP*0.30+notaTF*0.2+notaEF*0.50),2)

def actualizarDatos(listaAlumnos):
    pos=validarPosicion()
    nombre=actualizarNombre(pos)
    edad=actualizarEdad(pos)
    notaEP=actualizarNota(pos,"EP",2)
    notaTF=actualizarNota(pos,"TF",3)
    notaEF=actualizarNota(pos,"EF",4)
    prom=calcularPromedio(notaEP,notaTF,notaEF)
    alumno=[nombre,edad,notaEP,notaTF,notaEF,prom]
    #eliminamos el registro de la posicion
    listaAlumnos.pop(pos)
    #Insertar el nuevo registro en la posicion
    listaAlumnos.insert(pos,alumno)
    print("LISTA ACTUALIZADA")


def generarEstadisticas(listaAlumnos):
    sumaPromedio=0
    notaMinEP=21
    for i,alumno in enumerate(listaAlumnos):
        #Alternativa 1
        sumaPromedio+=alumno[5]
        #Alternativa 1
        if alumno[2]<notaMinEP:
            notaMinEP=alumno[2]

    print(f"El promedio de notas alternativa 1: {sumaPromedio/len(listaAlumnos)}")
    print(f"La nota minima del examen Parcial es: {notaMinEP}")
    
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


