try :
    x = int(input("Ingrese la cantidad de datos \n"))
except :
    x = 1
prom = 0
cantidad = x

def mipro() :
    global x, cantidad, prom
    while  x > 0 :
        dato = int(input("Ingrese el dato \n"))
        prom = prom + dato
        x = x - 1


mipro()
prom = prom / cantidad
print(cantidad)
print(prom,"\n")
