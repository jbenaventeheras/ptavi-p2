import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplica(self):
        return self.operando1 * self.operando2

    def divide(self):
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Input: python3 calc.py operando1 operador operando2")

    
    try:
        UsarCalchija = CalculadoraHija(float(sys.argv[1]), float(sys.argv[3]), sys.argv[2])

    except ValueError:
        sys.exit("Los operandos tienen que ser números")

    if UsarCalchija.operador == "suma":
        print(UsarCalchija.suma())

    elif UsarCalchija.operador == "resta":
        print(UsarCalchija.resta())

    elif UsarCalchija.operador == "multiplica":
        print(UsarCalchija.multiplica())

    elif UsarCalchija.operador == "divide":
        print(UsarCalchija.divide())

    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
        

