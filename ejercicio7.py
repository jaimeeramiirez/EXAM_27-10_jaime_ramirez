#EJERCICIO 7

listado= [18, 50, 210, 80, 145, 333, 70, 30]

#El problema está en que, en el bucle for no consigo hacer referencia a los numero por lo que las operaciones que escribo van a salir incorrectas. 

def main():
  for  n in listado:
    if n%10==0 && n<200:
      print(n)
    elif n>300:
      pass


if __name__ == '__main__':
  main()