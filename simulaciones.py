import time
import random

import numpy as np
import pandas as pd

columnas = ["Hora", "Cant Llamadas", "Cant Llamadas Atendidas", "Cant Compras", "Ganancia Mujeres",
             "Ganancia Hombres", "Ganancia Total", "Ganancia Acumulada", "Ganancia Promedio"]

tabla = pd.DataFrame(columnas)

def truncate(values, decs=0):
    """funcion utilizada para truncar nuevaDistr y no trabajar con todos los decimales de python """
    return np.trunc(values * 10 ** decs) / (10 ** decs)


def situacion(rnd_persona):
    """
    A partir de la tabla obtenida de personas que compran y que no con su sexo,
    permite que a partir de un número random, se obtenga el resultado correspondiente.

    :param rnd_persona: Un número mayor e igual a 0 y menor a 1,
     con una distribución uniforme.
    :return: Boolean, string: Se devuelve como booleano si compra y
     un string que indica el sexo de la persona que responde.
    """
    if rnd_persona < 0.15:
        return False, "nadie"
    elif rnd_persona < 0.626:
        return True, "mujer"
    elif rnd_persona < 0.83:
        return False, "mujer"
    elif rnd_persona < 0.898:
        return True, "hombre"
    else:
        return False, "hombre"


def gasto(sexo, rnd):
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


def simular(horas, cantLlamadas, puntoPartida=0):

    global gastoTotal
    columnas = ["Hora", "Cant Llamadas", "Cant Llamadas Atendidas", "Cant Compras", "Ganancia Mujeres",
                "Ganancia Hombres", "Ganancia Total", "Ganancia Acumulada", "Ganancia Promedio"]

    tabla = pd.DataFrame(columnas)

    gastoAcumulado = 0

    for j in range(horas):
        acumAtendidas = 0
        acumCompra = 0
        gastos = {"hombre": 0, "mujer": 0}

        for k in range(cantLlamadas):

            rnd1 = random.random()
            consume, sexo = situacion(rnd1)
            if consume:
                rnd2 = random.random()
                gastoTemp = gasto(sexo, rnd2)


                if cantLlamadas == 28:
                    gastoTemp = gastoTemp*0.65

                gastoAcumulado += gastoTemp

                acumCompra += 1
                gastos[sexo] += gastoTemp

            if sexo != "nadie":
                acumAtendidas +=1

        if (puntoPartida <= j < puntoPartida + 400) or j == horas-1:
            gastoTotal = (gastos["mujer"] + gastos["hombre"])

            fila = pd.DataFrame(
                {"Hora": [j+1],
                 "Cant Llamadas": [cantLlamadas],
                 "Cant Llamadas Atendidas": [acumAtendidas],
                 "Cant Compras": [acumCompra],
                 "Ganancia Mujeres": [gastos["mujer"]],
                 "Ganancia Hombres": [gastos["hombre"]],
                 "Ganancia Total": [gastoTotal],
                 "Ganancia Acumulada": [gastoAcumulado],
                 "Ganancia Promedio": [gastoAcumulado/(j+1)]
                 })
            #print(fila)

            tabla = pd.concat([tabla, fila], ignore_index=True)


    return gastoAcumulado / horas, tabla


def nuevaSimulacion(horas, partida,pantalla):

    llamadasHora = [20, 28]

    start = time.time()

    ganVoluntariado, tablaVoluntariado = simular(horas, llamadasHora[0], partida)
    ganCall, tablaCall = simular(horas, llamadasHora[1], partida)

    tiempoSim = time.time() - start

    pantalla.cargarResultados(ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall)

    # print("Ganancia promedio por hora de voluntariado: " + str(round(ganVoluntariado, 3)) + "\n"
    #       "Ganancia promedio por hora del callcenter: " + str(round(ganCall, 3)))
    # print("Tiempo usado en la simulacion: " + str(round(tiempoSim, 2)) + "s")