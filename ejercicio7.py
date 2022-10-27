#EJERCICIO 7

listado= [18, 50, 210, 80, 145, 333, 70, 30]

#El problema está en que, en el bucle for no consigo hacer referencia a los numero por lo que las operaciones que escribo van a salir incorrectas. 

def main():
  for numero in listado:
    if numero in listado %10==0 && numero<200:
      print(numero)
    elif numero in listado >300:
      print("ERROR")
  
if __name__ == '__main__':
  main()

  