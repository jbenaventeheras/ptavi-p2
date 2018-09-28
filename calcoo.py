import sys

class Calculadora():

    
    def __init__(self, operando1, operando2, operador):
        self.operando1 = operando1
        self.operando2 = operando2
        self.operador = operador
        
    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

if __name__ == "__main__":

   
	
    while len(sys.argv) != 4:
        sys.exit("Input: python3 calc.py operando1 operador operando2")
   
    try:
        Usarcalc = Calculadora(float(sys.argv[1]), float(sys.argv[3]), sys.argv[2] )

    except ValueError:
        sys.exit("Los operandos tienen que ser números")

 
    if Usarcalc.operador == "suma":
        print(Usarcalc.suma())
    elif Usarcalc.operador == "resta":
        print(Usarcalc.resta())
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
        
