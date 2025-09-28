print('sistema hospital, opciones: ')
opciones=int(input('1. registrar paciente \n2. ver pacientes \n3. salir \n'))
if opciones==1:
    nombre=input('ingrese nombre del paciente: ')
    edad=int(input('ingrese edad del paciente: '))
    genero=input('ingrese genero del paciente: ')
    enfermedad=input('ingrese enfermedad del paciente: ')
    print(f'paciente {nombre} registrado con exito')    
    