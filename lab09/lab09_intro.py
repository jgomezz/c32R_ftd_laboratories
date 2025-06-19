
# Ejercicio 03

import numpy as np

Trafico = np.array([[  0,   50,   30,   20 ],
                    [ 40,    0,   60,   25 ],
                    [ 35,   45,    0,   40 ],
                    [ 15,   30,   50,    0 ]
                    ])

print(Trafico)

trafico_total = np.sum(Trafico)

print(f"El trafico total es {trafico_total} MB/hora")

