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


def situacion(rnd_persona, vectorProb):
    """
    A partir de la tabla obtenida de personas que compran y que no con su sexo,
    permite que a partir de un número random, se obtenga el resultado correspondiente.

    :param rnd_persona: Un número mayor e igual a 0 y menor a 1,
     con una distribución uniforme.
    :return: Boolean, string: Se devuelve como booleano si compra y
     un string que indica el sexo de la persona que responde.

    VectorProb = [[ProbAtencion, ProbMujer, ProbMujerCompra, ProbHombreCompra],
                  [GM1, PM1, GM2, PM2, GM3, PM3, GM4, PM4],
                  [GH1, PH1, GH2, PH2, GH3, PH3, PH4, PH4],
                  [CantLlamadasVol, CantLlamadasCall, Comision]]
    """
    #Calculo de prob acumuladas


    nadieAteinde = 1-vectorProb[0][0]
    mujerCompra = vectorProb[0][0]*vectorProb[0][1]*vectorProb[0][2] + nadieAteinde
    mujerNoCompra = vectorProb[0][0]*vectorProb[0][1]*(1-vectorProb[0][2]) + mujerCompra
    hombreCompra = vectorProb[0][0]*(1-vectorProb[0][1])*vectorProb[0][3] + mujerNoCompra
    hombreNoCompra = vectorProb[0][0]*(1-vectorProb[0][1])*(1-vectorProb[0][3]) + hombreCompra


    if rnd_persona < nadieAteinde:
        return False, "nadie"
    elif rnd_persona < mujerCompra:
        return True, "mujer"
    elif rnd_persona < mujerNoCompra:
        return False, "mujer"
    elif rnd_persona < hombreCompra:
        return True, "hombre"
    else:
        return False, "hombre"


def gasto(sexo, rnd, v):
    """
        VectorProb = [[ProbAtencion, ProbMujer, ProbMujerCompra, ProbHombreCompra],
                      [GM1, PM1, GM2, PM2, GM3, PM3, GM4, PM4],
                      [GH1, PH1, GH2, PH2, GH3, PH3, PH4, PH4],
                      [CantLlamadasVol, CantLlamadasCall, Comision]]
    """


    if sexo == "hombre":
        if rnd < v[2][1]:
            return v[2][0]
        elif rnd < v[2][3]+v[2][1]:
            return v[2][2]
        elif rnd < v[2][5]+v[2][3]+v[2][1]:
            return v[2][4]
        else:
            return v[2][6]
    else:
        if rnd < v[1][1]:
            return v[1][0]
        elif rnd < v[1][3]+v[1][1]:
            return v[1][2]
        elif rnd < v[1][5]+v[1][3]+v[1][1]:
            return v[1][4]
        else:
            return v[1][6]


def simular(horas, cantLlamadas, vector, puntoPartida=0):

    global gastoTotal
    columnas = ["Hora", "Cant Llamadas", "Cant Llamadas Atendidas", "Cant Compras", "Ganancia Mujeres",
                "Ganancia Hombres", "Ganancia Total", "Ganancia Acumulada", "Ganancia Promedio"]
    columnasLlamadas = ["Hora", "Numero", "RndAtendida", "Atendida", "Compra", "RndCompra", "Compra"]

    tabla = pd.DataFrame(columnas)
    tablaLlamadas = pd.DataFrame(columnasLlamadas)

    gastoAcumulado = 0

    for j in range(horas):
        acumAtendidas = 0
        acumCompra = 0
        gastos = {"hombre": 0, "mujer": 0}

        for k in range(cantLlamadas):

            rnd1 = random.random()
            consume, sexo = situacion(rnd1, vector)
            rnd2= "n/a"
            gastoTemp = 0
            if consume:
                rnd2 = random.random()
                gastoTemp = gasto(sexo, rnd2, vector)

                if cantLlamadas == 28:
                    gastoTemp = gastoTemp*(1-(vector[3][2]/100))

                gastoAcumulado += gastoTemp

                acumCompra += 1
                gastos[sexo] += gastoTemp

            if sexo != "nadie":
                acumAtendidas += 1

            if (puntoPartida <= j < puntoPartida + 20) or j == horas - 1:
                filaLlamada = pd.DataFrame(
                    {"Hora": [j + 1],
                     "Numero": [k+1],
                     "RndAtendida": [rnd1],
                     "Atendida": [sexo],
                     "Consume": [consume],
                     "RndCompra":[rnd2],
                     "Compra": [gastoTemp]
                     })
                tablaLlamadas = pd.concat([tablaLlamadas, filaLlamada], ignore_index=True)

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

            tabla = pd.concat([tabla, fila], ignore_index=True)


    nadieAteinde = 1-vector[0][0]
    mujerCompra = vector[0][0]*vector[0][1]*vector[0][2] + nadieAteinde
    mujerNoCompra = vector[0][0]*vector[0][1]*(1-vector[0][2]) + mujerCompra
    hombreCompra = vector[0][0]*(1-vector[0][1])*vector[0][3] + mujerNoCompra
    hombreNoCompra = vector[0][0]*(1-vector[0][1])*(1-vector[0][3]) + hombreCompra

    print(tablaLlamadas)

    return gastoAcumulado / horas, tabla, tablaLlamadas


def nuevaSimulacion(horas, partida, pantalla, vector=0):
    """
        VectorProb = [[ProbAtencion, ProbMujer, ProbMujerCompra, ProbHombreCompra],
                      [GM1, PM1, GM2, PM2, GM3, PM3, GM4, PM4],
                      [GH1, PH1, GH2, PH2, GH3, PH3, PH4, PH4],
                      [CantLlamadasVol, CantLlamadasCall, Comision]]
    hola
    """
    if vector == 0:
        vector = [[0.85, 0.80, 0.70, 0.40],
                      [5, 0.20, 10, 0.60, 15, 0.15, 25, 0.5],
                      [5, 0.05, 10, 0.20, 15, 0.35, 25, 0.40],
                      [20, 28, 35]]

    llamadasHora = [vector[3][0], vector[3][1]]


    start = time.time()

    ganVoluntariado, tablaVoluntariado, tablaVoluntariadoLlamadas = simular(horas, llamadasHora[0], vector, partida)
    ganCall, tablaCall, tablaCallLlamadas = simular(horas, llamadasHora[1], vector,partida)

    tiempoSim = time.time() - start

    pantalla.cargarResultados(ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall
                              , tablaVoluntariadoLlamadas, tablaCallLlamadas)
