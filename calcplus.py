import sys
import calcoohija

if __name__ == "__main__":

    while len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")

    fich = open(sys.argv[1], "r")
    lineas = fich.readlines()
    fich.close()

    for linea in lineas:
        lista = linea.split(',')
        print(lista)
       
