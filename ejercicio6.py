print("\n\n")
import random
lista = random.sample(range(50), 20)
print(lista)

def modificar():
  print("\n\n")
  lista1=list(set(lista))
  print("Esta es la lista sin los números repetidos:", lista1)
  print("\n\n")

  lista1=sorted(lista1, reverse=True)
  print("Esta es la lista ordenada de mayor a menor:", lista1)
  
  print("\n\n")

  lista2=[]
  for n in lista1:
    if n % 2 == 0:
      lista2.append(n)
    else:
      pass

  print("Esta es la lista sin impares y ordenada de mayor a menor:" +     str(lista2))

  print("\n\n")

  sumalista2= sum(lista2)
  print("La suma de los elementos de la lista sin impares es:",           sumalista2)

  print("\n\n")

  lista2.append(sumalista2)
  lista2=sorted(lista2, reverse=True)

  print("Esta es la lista con el valor de la suma como primer elmento de la lista:",lista2)
  print("\n\n")

  print("*",lista2[0]==sum(lista2[1:]),"*")

modificar()