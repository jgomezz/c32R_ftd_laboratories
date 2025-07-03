
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
