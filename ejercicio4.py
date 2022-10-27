#EJERCICIO 4

print("\n\n")

def lista__():
  
  lista=["hola", 5, 7.8, True]
  print(lista[-2],lista[-4])
  print("\n")
  a,b = lista.index("hola"), lista.index(True)
  (lista[a], lista[b])= (list[b], lista[a])

  print(lista)
  print("\n")

  lista.pop(3)
  print(lista)
  print("\n")

  lista_nueva=list(set(lista))

  print(lista_nueva)


  


lista__()