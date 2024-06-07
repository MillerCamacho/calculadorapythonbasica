#Calculadora Desarrollada por Miller Steven Camacho

while True:
     
    print("""Bienvenido
    Opciones
    Ingrese '+' para sumar dos numeros
    Ingrese '-' para restar dos numeros
    Ingrese '*' para multiplicar dos numeros
    Ingrese '/' para dividir dos numeros
    Ingrese 'salir' para finalizar""")

    teclado=input(":")
    if teclado=="salir" or teclado=="Salir":
        break
    elif teclado=="+":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1+num2)
        print("Respuesta: "+result)
    elif teclado=="-":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1-num2)
        print("Respuesta: "+result)
    elif teclado=="*":
        num1=float(input("Ingrese un numero:"))
