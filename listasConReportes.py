
# VALIDACIONES DE ENTRADA DE DATOS
def ingresarMedioTransporte():
    while True:
        medioT=input("Medio de transporte (A/T/P o X para terminar): ").upper()
        if medioT=='A' or medioT=='T' or medioT=='P' or medioT=='X':
            break
    return medioT

def  ingresarTiempo():
    while True:
        try:
            t=int(input("Tiempo de duración del viaje: "))
            if t>0:
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
    return t
def ingresarMomentoDia():
    while True:
        try:
            momento=int(input("Momento del día (1:7-9, 2:12-14, 3:17-19, 4:>=22): "))
            if momento>=1 and momento<=4:
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
    return momento

def ingresarRuta():
    while True:
        ruta=input("Ruta elegida (A/B/C/O): ").upper()
        if ruta=='A' or ruta=='B' or ruta=='C' or ruta=='O':
            break
    return ruta

def generarReporte(listaDatos):
    #Contadores para los medios de transporte
    contA=0
    contT=0
    contP=0
    #Sumadores para los tiempos por 
    sumaTiempoA=0
    sumaTiempoB=0
    sumaTiempoC=0
    sumaTiempoO=0
    contRutaA=0
    contRutaB=0
    contRutaC=0
    contRutaO=0
    #contador de momentos del dia
    cont1=0
    cont2=0
    cont3=0
    cont4=0
    for dato in listaDatos:
        #dato[0]->medio de transporte
        match(dato[0]):
            case 'A': contA+=1
            case 'T': contT+=1
            case 'P': contP+=1
        match(dato[3]):
            case 'A':
                contRutaA+=1
                sumaTiempoA+=dato[1]
            case 'B':
                contRutaB+=1
                sumaTiempoB+=dato[1]
            case 'C':
                contRutaC+=1
                sumaTiempoC+=dato[1]
            case '0':
                contRutaO+=1
                sumaTiempoO+=dato[1]
        if dato[2]==1:
            cont1+=1
        else:
            if dato[2]==2:
                cont2+=1
            else:
                if dato[2]==3:
                    cont3+=1
                else:
                    cont4+=1
    #fin del for
    print("=== Cantidad de usarios por medio de transportes")
    print(f"\tAuto propio       : {contA}")
    print(f"\tAuto privado      : {contT}")
    print(f"\tTransporte público: {contP}")
    print("=== Tiempo promedio de viaje por ruta")
    print(f"\tAv. Arequipa          : {sumaTiempoA/contRutaA}")
    print(f"\tAv. Brasil            : {sumaTiempoB/contRutaB}")
    print(f"\tPaseo de la república : {sumaTiempoC/contRutaC}")
    if contRutaO!=0:
        print(f"\tOtra ruta             : {sumaTiempoO/contRutaO}")
    else:
        print(f"\tOtra ruta             : 0")
    print("=== Momento con mayor cantidad de viajes")
    contadores=[cont1,cont2,cont3,cont4]
    maximo=max(contadores)
    for i,contador in enumerate(contadores):
        if contador==maximo:
            print(i+1,end=", ")
    
if __name__=="__main__":
    listaDatos=[]
    while True:
        medioT=ingresarMedioTransporte() #A, T, P y X -> convertir a mayuscula con upper()
        if medioT=='X':
            break
        tiempo=ingresarTiempo() #valor entero positivo
        momentoDia=ingresarMomentoDia() # De 1 al 4
        ruta=ingresarRuta() #A,B,C,O
        listaDatos.append([medioT,tiempo,momentoDia,ruta])
    generarReporte(listaDatos)


