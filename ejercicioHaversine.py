

import math
def ingresarValor(mensaje):
    while True:
        try:
            valor=float(input(f"Ingrese la {mensaje} (grados): "))
            if valor>=0:
                break
            else:
                print("Debe ingresar valores positivos")
        
        except ValueError:
            print("Debe ingresar un valor numérico")
    return valor


if __name__=="__main__":
    #ingreso de datos
    lat1=ingresarValor("latitud 1")
    lat2=ingresarValor("latitud 2")
    long1=ingresarValor("longitud 1")
    long2=ingresarValor("longitud 2")
    #Proceso: step 1: Conversion a radianes
    rad_lat1=lat1*(math.pi/180)
    rad_lat2=lat2*(math.pi/180)
    rad_long1=long1*(math.pi/180)
    rad_long2=long2*(math.pi/180)
    #process: step 2: Diferencia angular
    dAngularLatitudes=(rad_lat2-rad_lat1)
    dAngularLongitudes=(rad_long2-rad_long1)
    #proceso: step 3:fórmula de Haversine
    a=(math.pow(math.sin(dAngularLatitudes/2),2)+ math.cos(rad_lat1)*math.cos(rad_lat2)*
       math.pow(math.sin(dAngularLongitudes/2),2))
    radioTerreste=6371000
    distancia=2*radioTerreste*math.asin(math.sqrt(a))
    print(f"La distancia segun la formula de Haversine es: {distancia:.2f}")

