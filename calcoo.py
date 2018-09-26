import sys

class Calculadora(object):


    def suma(self, operando1, operando2):
        return operando1 + operando2

    def resta(self, operando1, operando2):
        return operando1 - operando2

if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    Usarcalc = Calculadora()

    if sys.argv[2] == "suma":
        resultado = calc.suma(operando1, operando2)
    elif operacion == "resta":
       sys.argv[2] = calc.resta(operando1, operando2)
    else:
        sys.exit("operacion no valida")
    print(resultado)
