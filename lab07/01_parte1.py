# -----------------------------
# 1. Conjuntos (set) en Python
# -----------------------------
print("== 1. Conjuntos ==")

A = {1, 2, 3, 4}
B = {3, 4, 5}

# TODO 1-a: crea la unión de A y B en una variable llamada union_AB
union_AB = A.union(B)

# TODO 1-b: crea la intersección en inter_AB
inter_AB =  A.intersection(B)

# TODO 1-c: crea la diferencia A \ B en diff_AB
diff_AB =  A.difference(B)

assert union_AB == {1, 2, 3, 4, 5}, "Fallo en unión"
assert inter_AB == {3, 4}, "Fallo en intersección"
assert diff_AB == {1, 2}, "Fallo en diferencia"
print("✔️  Conjuntos OK\n")


# ------------------------------------------
# 2. Par ordenado y producto cartesiano
# ------------------------------------------
print("== 2. Producto cartesiano ==")

def cart_product(X, Y):
    """Devuelve el producto cartesiano X×Y como conjunto de tuplas."""
    return {(x, y) for x in X for y in Y}

# TODO 2-a: genera C = {a,b} y D = {1,2,3}
C = {'a','b'} 
D = {1,2,3}

# TODO 2-b: calcula C×D en prod_CD
prod_CD = cart_product(C, D)

assert prod_CD == {('a', 1), ('a', 2), ('a', 3),
                   ('b', 1), ('b', 2), ('b', 3)}, "Producto cartesiano incorrecto"
print("✔️  Producto cartesiano OK\n")


# -------------------------------
# 3. Relaciones binarias
# -------------------------------
print("== 3. Relaciones ==")

U = {1, 2, 3}

# Ejemplo de relación: "<" sobre U
leq = [(x, y) for x in U for y in U if x < y]

print("Relación '<':", leq)

# TODO 3-a: define la relación 'menor_estricto' (<) sobre U
menor_estricto = leq

assert (1, 1) not in menor_estricto and (1, 2) in menor_estricto, "Comprueba la definición"
print("✔️  Relación definida\n")

'''

# -------------------------------------------
# 4. Propiedades de relaciones en un conjunto
# -------------------------------------------
print("== 4. Propiedades de relaciones ==")

def es_reflexiva(R, S):
    return all((x, x) in R for x in S)

def es_simetrica(R):
    return all((y, x) in R for (x, y) in R)

def es_antisimetrica(R):
    return all((y, x) not in R or x == y for (x, y) in R)

def es_transitiva(R):
    return all((x, z) in R
               for (x, y) in R
               for (w, z) in R
               if y == w)

# Pruebas rápidas
assert es_reflexiva(leq, U)
assert es_antisimetrica(leq)
assert es_transitiva(leq)

assert not es_reflexiva(menor_estricto, U)
assert es_transitiva(menor_estricto)

print("✔️  Propiedades verificadas\n")
'''

# ------------------------------------
# 5. Funciones, dominio y rango
# ------------------------------------
print("== 5. Funciones ==")

# Representaremos una función total finita como diccionario
f = {1: 2, 2: 4, 3: 6}   # f(x) = 2x sobre {1,2,3}
dom_f = set(f.keys())
img_f = set(f.values())

print("Dominio f:", dom_f)
print("Imagen f:", img_f)

# TODO 5-a: implementa funcion_identidad(S) que devuelva {x: x for x in S}
def funcion_identidad(S):
    return {x: x for x in S}

assert funcion_identidad({1, 2, 3}) == {1: 1, 2: 2, 3: 3}
print("✔️  Función identidad OK\n")

# ----------------------------------
# 6. Tipos de funciones
# ----------------------------------
'''
print("== 6. Tipos de funciones ==")

def es_inyectiva(func):
    return len(set(func.values())) == len(func)

def es_sobreyectiva(func, codominio):
    return set(func.values()) == codominio

def es_biyectiva(func, codominio):
    return es_inyectiva(func) and es_sobreyectiva(func, codominio)

# TODO 6-a: construye g = {1: 'a', 2: 'b', 3: 'c'}
g = ...

assert es_inyectiva(g) and es_sobreyectiva(g, {'a', 'b', 'c'})
print("✔️  g es biyectiva\n")
'''
# -------------------------------------------------
# 7. Composición de funciones (sobre diccionarios)
# -------------------------------------------------
print("== 7. Composición ==")

def componer(g, f):
    """Devuelve g∘f, suponiendo f: A→B y g: B→C, ambas dict."""
    return {a: g[f[a]] for a in f}

# Ejemplo: f: {1→2, 2→3}, h: {2→'x', 3→'y'}
f2 = {1: 2, 2: 3}
h = {2: 'x', 3: 'y'}

# TODO 7-a: calcula h ∘ f2 (llámalo h_of2)
h_of2 = componer(h, f2)

assert h_of2 == {1: 'x', 2: 'y'}, "Composición incorrecta"
print("✔️  Composición OK")

print("\n¡Todos los tests han pasado! Ahora juega cambiando los ejemplos o ampliándolos 👍")