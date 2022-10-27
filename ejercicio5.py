print("\n\n")

def main():
  
  num= float(input("INGRESE UN NÚMERO DE 4 CIFRAS: "))

  mil= (num - (num%1000)) / 1000
  resto= num%1000
  centena= (resto-(resto%100)) / 100
  resto = num%100
  decena= (resto-(resto%10)) / 10
  unidad = resto % 10 
  print("\n")

  print("UNIDADES:",'%04d' % unidad)
  print("DECENAS:", '%03d' % decena)
  print("CENTENAS:",'%02d' % centena)
  print("MIL:",'%01d' % mil)

if __name__ == '__main__':
  main()

