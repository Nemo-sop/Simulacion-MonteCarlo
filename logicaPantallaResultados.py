from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

import simulaciones


class PantallaResultados(QMainWindow):
    """Incializar clase"""

    def __init__(self, ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall, tablaVoluntariadoLlamadas
                 , tablaCallLlamadas):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("defPantallaResultados.ui", self)
        self.inicializarResultados(ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall
                                   , tablaVoluntariadoLlamadas, tablaCallLlamadas)

    def inicializarResultados(self, ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall,
                              tablaVoluntariadoLlamadas, tablaCallLlamadas):
        self.txtGanVol.setText(str(round(ganVoluntariado, 4)))
        self.txtGanCall.setText(str(round(ganCall, 4)))
        self.txtTiempo.setText(str(round(tiempoSim, 2)) + 's')

        self.cargarTablasCHora(tablaVoluntariado, tablaCall)
        self.cargarTablasCLlamada(tablaVoluntariadoLlamadas, tablaCallLlamadas)

    def cargarTablasCHora(self, tablaVoluntariado, tablaCall):
        fila = -9

        self.tablaSimCall.setRowCount(len(tablaCall) - 9)

        for i in range(len(tablaCall)):
            self.tablaSimCall.setItem(fila, 0, QTableWidgetItem(str(tablaCall.at[i, "Hora"])))
            self.tablaSimCall.setItem(fila, 1, QTableWidgetItem(str(tablaCall.at[i, "Cant Llamadas"])))
            self.tablaSimCall.setItem(fila, 2, QTableWidgetItem(str(tablaCall.at[i, "Cant Llamadas Atendidas"])))
            self.tablaSimCall.setItem(fila, 3, QTableWidgetItem(str(tablaCall.at[i, "Cant Compras"])))
            self.tablaSimCall.setItem(fila, 4, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Mujeres"])))
            self.tablaSimCall.setItem(fila, 5, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Hombres"])))
            self.tablaSimCall.setItem(fila, 6, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Total"])))
            self.tablaSimCall.setItem(fila, 7, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Acumulada"])))
            self.tablaSimCall.setItem(fila, 8, QTableWidgetItem(str(round(tablaCall.at[i, "Ganancia Promedio"], 4))))
            fila = fila + 1

        fila = -9
        self.tablaSimVolun.setRowCount(len(tablaVoluntariado) - 9)
        for i in range(len(tablaVoluntariado)):
            self.tablaSimVolun.setItem(fila, 0, QTableWidgetItem(str(tablaVoluntariado.at[i, "Hora"])))
            self.tablaSimVolun.setItem(fila, 1, QTableWidgetItem(str(tablaVoluntariado.at[i, "Cant Llamadas"])))
            self.tablaSimVolun.setItem(fila, 2,
                                       QTableWidgetItem(str(tablaVoluntariado.at[i, "Cant Llamadas Atendidas"])))
            self.tablaSimVolun.setItem(fila, 3, QTableWidgetItem(str(tablaVoluntariado.at[i, "Cant Compras"])))
            self.tablaSimVolun.setItem(fila, 4, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Mujeres"])))
            self.tablaSimVolun.setItem(fila, 5, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Hombres"])))
            self.tablaSimVolun.setItem(fila, 6, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Total"])))
            self.tablaSimVolun.setItem(fila, 7, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Acumulada"])))
            self.tablaSimVolun.setItem(fila, 8, QTableWidgetItem(str(round(tablaVoluntariado.at[i, "Ganancia Promedio"]
                                                                           , 4))))
            fila = fila + 1

    def cargarTablasCLlamada(self, tablaVoluntariadoLlamadas, tablaCallLlamadas):
        fila = -7

        self.tablaSimLlamadasVol.setRowCount(len(tablaVoluntariadoLlamadas) - 7)

        for i in range(len(tablaVoluntariadoLlamadas)):
            self.tablaSimLlamadasVol.setItem(fila, 0, QTableWidgetItem(str(tablaVoluntariadoLlamadas.at[i, "Hora"])))
            self.tablaSimLlamadasVol.setItem(fila, 1, QTableWidgetItem(str(tablaVoluntariadoLlamadas.
                                                                           at[i, "Numero"])))
            rndAtentida = tablaVoluntariadoLlamadas.at[i, "RndAtendida"]
            self.tablaSimLlamadasVol.setItem(fila, 2, QTableWidgetItem(str(simulaciones.truncate(rndAtentida, 4))))
            self.tablaSimLlamadasVol.setItem(fila, 3, QTableWidgetItem(str(tablaVoluntariadoLlamadas.at[i, "Atendida"])))

            consumio = tablaVoluntariadoLlamadas.at[i, "Consume"]
            if consumio:
                self.tablaSimLlamadasVol.setItem(fila, 4, QTableWidgetItem("SI"))
            else:
                self.tablaSimLlamadasVol.setItem(fila, 4, QTableWidgetItem("NO"))

            rndCompra = tablaVoluntariadoLlamadas.at[i, "RndCompra"]
            if rndCompra == "n/a":
                self.tablaSimLlamadasVol.setItem(fila, 5,
                                                 QTableWidgetItem(str(rndCompra)))
            else:
                self.tablaSimLlamadasVol.setItem(fila, 5, QTableWidgetItem(str(simulaciones.truncate(rndCompra, 4))))

            self.tablaSimLlamadasVol.setItem(fila, 6, QTableWidgetItem(str(tablaVoluntariadoLlamadas.at[i, "Compra"])))
            fila = fila + 1

        fila = -7
        self.tablaSimLlamadasCall.setRowCount(len(tablaCallLlamadas) - 7)
        for i in range(len(tablaCallLlamadas)):
            self.tablaSimLlamadasCall.setItem(fila, 0, QTableWidgetItem(str(tablaCallLlamadas.at[i, "Hora"])))
            self.tablaSimLlamadasCall.setItem(fila, 1, QTableWidgetItem(str(tablaCallLlamadas.at[i, "Numero"])))
            rndAtentida = tablaCallLlamadas.at[i, "RndAtendida"]
            self.tablaSimLlamadasCall.setItem(fila, 2, QTableWidgetItem(str(simulaciones.truncate(rndAtentida, 4))))
            self.tablaSimLlamadasCall.setItem(fila, 3, QTableWidgetItem(str(tablaCallLlamadas.at[i, "Atendida"])))

            consumio = tablaCallLlamadas.at[i, "Consume"]
            if consumio:
                self.tablaSimLlamadasCall.setItem(fila, 4, QTableWidgetItem("SI"))
            else:
                self.tablaSimLlamadasCall.setItem(fila, 4, QTableWidgetItem("NO"))

            rndCompra = tablaCallLlamadas.at[i, "RndCompra"]
            if rndCompra == "n/a":
                self.tablaSimLlamadasCall.setItem(fila, 5,
                                                 QTableWidgetItem(str(rndCompra)))
            else:
                self.tablaSimLlamadasCall.setItem(fila, 5, QTableWidgetItem(str(simulaciones.truncate(rndCompra, 4))))

            self.tablaSimLlamadasCall.setItem(fila, 6, QTableWidgetItem(str(tablaCallLlamadas.at[i, "Compra"])))
            fila = fila + 1
