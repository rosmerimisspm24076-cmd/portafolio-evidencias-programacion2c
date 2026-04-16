#funciones basicas
def suma (a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b
def div(a,b):
    return a / b
#menu de obciones
opcion =0
while(opcion != 5):
    print("___menu de opciones___")
    print("1.sumar 2 valores")
    print("2. restar 2 valores")
    print("3.multiplicar 2 valores ")
    print("dividir 2 valores")
    print("terminar programa")
    opcion =int(input("/nselecciona la opcion deseada (1-5):"))

    if opcion == 1:
        #suma de dos numeros
        n1 =float(input("/ingresa el primer numero a sumar:"))
        n2 =float(input("/ingresa el segundo valor a sumar"))
        print(f"cociente resultante:{suma(n1,n2) }")
    elif  opcion ==2:
        #resta de dos numeros 
        n1 =float(input("/ingresa el minuendo:"))
        n2 =float(input("/ingresa el sustraendo"))
        print(f"diferencia resultante:{resta(n1,n2) }")

    elif opcion ==3:
        #multiplicacion de dos numeros    
        n1 =float(input("/ingresa el primer factor:"))
        n2 =float(input("/ingresa el segundo factor"))
        print(f"producto resultante:{multi(n1,n2) }")

    elif opcion ==4:
        #divicion de dos numeros
        n1 =float(input("/ingresa el dividendo:"))
        n2 =float(input("/ingresa el divisor"))
        print(f"cociente resultante:{div(n1,n2) }")
    elif opcion ==5:
        #finalizacion del programa
        print("programa finalizado...") 
    else:
        #mensaje de error por obcion no valida
        print("opcion seleccionda no valida,intenta nuevamente!")