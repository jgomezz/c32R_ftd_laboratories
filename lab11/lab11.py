
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

n50 = Nodo(50)
n30 = Nodo(30)
n70 = Nodo(70)

n50.izq = n30
n50.der = n70

'''
40, 20, 10, 30, 60, 50, 70

            40
         20     60 
       10  30 50  70

'''

n10 = Nodo(10)
n20 = Nodo(20)
n30 = Nodo(30)
n40 = Nodo(40)
n50 = Nodo(50)
n60 = Nodo(60)
n70 = Nodo(70)

