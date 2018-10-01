import sys
import calcoohija
import csv

if __name__ == "__main__":

    while len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")

try:
    with open(sys.argv[1], newline="") as csvfile:
        operaciones = csv.reader(csvfile)
        for operacion in operaciones:
            result = float(operacion[1])
            Not_Allowed = False
            try:
                for number in operacion[2:]:
                    operando = float(number)
                    cuenta = calcoohija.CalculadoraHija(result, operando,
                                                        operacion[0])
                    if cuenta.operador == 'suma':
                        result = cuenta.suma()
                    elif cuenta.operador == 'resta':
                        result = cuenta.resta()
                    elif cuenta.operador == 'multiplica':
                        result = cuenta.multiplica()
                    elif cuenta.operador == 'divide':
                        result = cuenta.divide()
                    else:
                        Not_Allowed = True
                if not Not_Allowed:
                    print(result)
                else:
                    print(cuenta.operador + ' is not allowed')
            except ValueError:
                print('Not an integer number')
except FileNotFoundError as not_found:
    print(not_found.filename)
