def numpar(numero):                     #Funciòn para verificar si el numero es par
    if numero%2 == 0:                   #Si el residuo del numero el igual a cero el resultado sera true
        return True
    else:
        return False

numinicio=2
#Mi carnet es 201612200 el limite seria 200
numfinal=200
listaresultado=[]
resultado = 0

while(numfinal>numinicio):
    for i in range (numinicio, numfinal):
        if(numpar(i)):
            resultado = i//2
            listaresultado.append(resultado)
            resultado = 0
        else:
            resultado = (3*i) + 1
            listaresultado.append(resultado)
            resultado = 0
    
    numinicio = numinicio + 1
    print(listaresultado)
    listaresultado = []

"""
while(numfinal>numinicio):
    while(resultado == 1):
        if (numpar(numinicio)):
            resultado = numinicio//2
            listaresultado.append(resultado)
        else:
            resultado = (3*numinicio) + 1 
            listaresultado.append(resultado)  

"""