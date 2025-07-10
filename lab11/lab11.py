
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


# sub-arbol izq.
n20.izq = n10
n20.der = n30

# sub-arbol der.
n60.izq = n50
n60.der = n70

# arbol total
n40.izq = n20
n40.der = n60

raiz = n40

print(raiz) # <__main__.Nodo object at 0x7f87e00f3b80>

def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=" ")
        inorden(nodo.der)

inorden(raiz)


# Search
'''
40, 20, 10, 30, 60, 50, 70

            40
         20     60 
       10  30 50  70

'''

nros = [40, 20, 10, 30, 60, 50, 70]

# encontrar el valor de 10
print("\n-----------")

for valor in nros:
    if valor == 10 :
        print("numero encontrado")
    print(valor)



