import sys

class Calculadora():

    #error al intentar poner operador preguntar?????????
    def __init__(self, operando1, operando2, operador):
        self.operando1 = operando1
        self.operando2 = operando2
        self.operador = operador
        
    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

if __name__ == "__main__":

    Usarcalc = Calculadora(float(sys.argv[1]), float(sys.argv[3]), sys.argv[2] )
 
    if Usarcalc.operador == "suma":
       print(Usarcalc.suma())
    elif Usarcalc.operador == "resta":
      print(Usarcalc.resta())

    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
        
