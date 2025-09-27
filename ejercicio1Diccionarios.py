def generarDatos():
    dicFrutas={
        "platano":1.35,
        "manzana":0.80,
        "pera":0.85,
        "naranja":0.70
    }
    return dicFrutas

def ingresarPedido():
    while True:
        try:
            fruta=input("Ingrese la fruta a comprar: ")
            cantidad=int(input("Ingrese el número de kilos a comprar: "))
            if cantidad>0:
                break
            else:
                print("Debe ingresar una cantidad valida")        
        except ValueError:
            print("Debe ingresar un valor numérico")
    return fruta,cantidad

def calcularPrecioVenta(dicFrutas,fruta,cantidad):
    fruta=fruta.lower()
    if fruta in dicFrutas:
        return dicFrutas[fruta]*cantidad
    else:
        return -1

def ingresarOtrasFrutas():
    while True:
        try:

            nuevaFruta=input("Ingrese una nueva fruta al stock: ")
            precio=float(input("Ingrese el precio de la nueva fruta: "))
            if precio>0:
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
    #Validar que la fruta no exista en el diccionario para poderla agregar
    if nuevaFruta in dicFrutas:
        print(f" La {nuevaFruta} ya existe en la lista")
    else:
        dicFrutas[nuevaFruta]=precio
    return dicFrutas


if __name__=="__main__":
    #Creamos un dicionario vacio como variable global
    dicFrutas={}
    dicFrutas=generarDatos()
    fruta,cantidad=ingresarPedido()
    precioVenta=calcularPrecioVenta(dicFrutas,fruta,cantidad)
    if precioVenta!=-1:
        print(f"El precio de {cantidad} kilos de {fruta} es {precioVenta:.2f}")
    else:
        print("No existe la fruta en el stock")
    ## ingrese un nuevo valor al stock
    dicFrutas=ingresarOtrasFrutas()
    print(dicFrutas)



