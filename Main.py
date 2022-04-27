import random
import time

import numpy as np
import pandas as pd


horas = int(input("Ingrese la cantidad de horas:"))
cantidad = 20*horas


def truncate(self, values, decs=0):
    """funcion utilizada para truncar nuevaDistr y no trabajar con todos los decimales de python """
    return np.trunc(values * 10 ** decs) / (10 ** decs)

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

def simular(horas, cantLlamadas):
    acum = 0
    for j in range(horas):
        for k in range(cantLlamadas):
            rnd1 = random.random()

            consume,sexo = situacion(rnd1)
            if consume:
                rnd2 = random.random()

                acum += gasto(sexo,rnd2)

    return acum / horas

llamadasHora = [20,28]

start = time.time()

resultado1 = simular(horas, llamadasHora[0])
resultado2 = simular(horas, llamadasHora[1]) * 0.65

time = time.time()-start


print("Ganancia promedio por hora de voluntariado: "+str(round(resultado1, 3))+"\n"
      "Ganancia promedio por hora del callcenter: "+str(round(resultado2, 3)))
print("Tiempo usado en la simulacion: "+str(round(time, 2))+"s")
