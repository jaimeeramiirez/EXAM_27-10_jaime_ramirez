listado= [18, 50, 210, 80, 145, 333, 70, 30]

def main():
  for  numero in listado:
    if numero%10:
      print(numero)
    elif numero>300:
      pass


if __name__ == '__main__':
  main()