entrada = input()
lista1 = entrada.split()
n = int(lista1[0])
m = int(lista1[1])
lista =list()
def transformacion() :
    global cadena
    otro = ""

    for u in cadena:
        if u=='0':
            otro = otro + 'O'
        elif u == '1' :
            otro = otro + 'L'
        elif u=='2':
            otro = otro + 'Z'
        elif u=='3':
            otro = otro + 'E'
        elif u=='5':
            otro = otro + 'S'
        elif u=='6':
            otro = otro + 'B'
        elif u=='7':
            otro = otro + 'T'
        elif u=='8':
            otro = otro + 'B'
        else :
            otro = otro + u

    return otro


while n > 0 :
    str = input()
    lista.append(str)
    n = n -1
inv = False
while m > 0 :
    inv = False
    cadena = input()
    cadena = transformacion()

    for i in lista :
        con = 0
    #    con = cadena.find(i)
        if i in cadena :
            inv = True

    if inv == True :
        print("INVALID")
    else :
        print("VALID")

    m = m - 1
