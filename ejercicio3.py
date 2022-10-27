#EJERCICIO 3 

print("\n")
def multiplicador():
  numero_magico= 12345679 

  numero_usuario= int(input("Introduce un número entre 1 y 9: "))
  
  print("\n")

  numero_usuario= numero_usuario*9

  print("El número introducido multiplicado por 9 es:", numero_usuario)

  numero_magico= numero_magico*numero_usuario
  
  print("\n")

  print("El número resultante es: ", numero_magico)

multiplicador()
