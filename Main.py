import random

import numpy as np
import pandas as pd


horas = int(input("Ingrese la cantidad de horas:"))
cantidad = 20*horas

def situacion(rnd_persona):
    if rnd_persona < 0.15:
        return False,"nadie"
    elif rnd_persona < 0.626:
        return True,"mujer"
    elif rnd_persona < 0.83:
        return False, "mujer"
    elif rnd_persona < 0.898:
        return True, "hombre"
    else:
        return False, "hombre"


def gasto(sexo,rnd):
    if sexo == "hombre":
        if rnd < 0.05:
            return 5
        elif rnd < 0.25:
            return 10
        elif rnd < 0.6:
            return 15
        else:
            return 25
    else:
        if rnd < 0.2:
            return 5
        elif rnd < 0.8:
            return 10
        elif rnd < 0.95:
            return 15
        else:
            return 25


llamadasHora = [20,28]
acum= [0,0]
for i in range(len(llamadasHora)):
    for j in range(horas):
        for k in range(llamadasHora[i]):
            rnd1 = random.random()

            consume,sexo = situacion(rnd1)
            if consume:
                rnd2 = random.random()

                acum[i] += gasto(sexo,rnd2)

acum[1] *= 0.65
acum = [acum[i]/horas for i in range(len(acum))]
print(acum)