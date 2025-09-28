opcion=int(input("1. sumar\n 2.restar\n 3.multiplicar\n Ingrese una opcion: "))
dato1 = float(input("Ingrese el primer numero: "))
dato2 = float(input("Ingrese el segundo numero: "))
if opcion==1:
    total=dato1+dato2
    print(total)
elif opcion==2:
    total=dato1-dato2
    print(total)
elif opcion==3:
    total=dato1*dato2
    print(total)
else:
    print("Opcion no valida")
