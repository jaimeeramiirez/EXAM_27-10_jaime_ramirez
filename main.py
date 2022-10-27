#EJERCICIO 1

def mayusculaminuscula():
  var_1 = "Módulo 1 de Python"
  var_1_mayuscula= var_1.upper()
  var_1_minuscula=var_1.lower()
  print(var_1_mayuscula)
  print(var_1_minuscula)
  division= len(var_1)/7
  print(round(division,4))

mayusculaminuscula()

print("\n\n")
def funcion_1():
  operación= 12-(4*2)-(2+2)
  print(operación)
funcion_1()

def funcion_2():
  operacion= 12 - 4 * (2 - 2) + 2
  print(operacion)
funcion_2()

print("\n\n")
def edad():
  edad=int(input("Introduce tu edad: "))
  if edad >= 18:
    print("Eres mayor de edad")
  else:
    print("Eres menor de edad")
edad()
  