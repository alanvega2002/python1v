encendido=True
opcion=0


def suma(num_1:int,num_2:int):

while encendido:
    print("seleccionar una opcion")
    print("1.-sumar 2 numeros")
    print("2.-restar 2 numeros")
    print("3.-multiplicar 2 numeros")
    print("4.-dividir 2 numeros")
    print("5.-salir")
    opcion=int(input("seleccione una opcion: "))
    if opcion == 1:
        print("seleccionó :",opcion)
        num_1=int(input("ingrese 1er numero: "))
        num_2=int(input("ingrese 2do numero: "))
        print(f" {num_1} + {num2} = {num_1+num_2} ")
    if opcion == 2:
        print("seleccionó :",opcion)
        num_1=int(input("ingrese 1er numero: "))
        num_2=int(input("ingrese 2do numero: "))
        print(f" {num_1} - {num2} = {num_1+num_2} ")
    if opcion == 3:
        print("seleccionó :",opcion)
        num_1=int(input("ingrese 1er numero: "))
        num_2=int(input("ingrese 2do numero: "))
        print(f" {num_1} * {num2} = {num_1+num_2} ")
    if opcion == 4:
        print("seleccionó :",opcion)
        num_1=int(input("ingrese 1er numero: "))
        num_2=int(input("ingrese 2do numero: "))
        print(f" {num_1} / {num2} = {num_1+num_2} ")
    if opcion == 5:
        print("seleccionó :",opcion)
        encendido=falso
