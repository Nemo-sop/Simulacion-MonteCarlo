from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

import simulaciones


class PantallaIngresoDatos(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("defPantallaIngresoDatos.ui", self)
        self.btnSimular.clicked.connect(self.nuevaSimulacion)
        regExpr = QRegExp("^([1-9]|[1-9][0-9]+)+$")
        self.txtCantHoras.setValidator(QRegExpValidator(regExpr, self))
        self.txtPtoPartida.setValidator(QRegExpValidator(regExpr, self))

    def cargarResultados(self, ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall):
        self.txtGanVol.setText(str(round(ganVoluntariado, 4)))
        self.txtGanCall.setText(str(round(ganCall, 4)))
        self.txtTiempo.setText(str(round(tiempoSim, 2)) + 's')

        self.cargarTabla(tablaVoluntariado, tablaCall)

    def nuevaSimulacion(self):
        if self.validarDatosValidos():
            simulaciones.nuevaSimulacion(int(self.txtCantHoras.text()), int(self.txtPtoPartida.text())-1, self)

    def cargarTabla(self, tablaVoluntariado, tablaCall):
        fila = -9
        self.tablaSimCall.setRowCount(len(tablaCall)-9)

        for i in range(len(tablaCall)):
            self.tablaSimCall.setItem(fila, 0, QTableWidgetItem(str(tablaCall.at[i, "Hora"])))
            self.tablaSimCall.setItem(fila, 1, QTableWidgetItem(str(tablaCall.at[i, "Cant Llamadas"])))
            self.tablaSimCall.setItem(fila, 2, QTableWidgetItem(str(tablaCall.at[i, "Cant Llamadas Atendidas"])))
            self.tablaSimCall.setItem(fila, 3, QTableWidgetItem(str(tablaCall.at[i, "Cant Compras"])))
            self.tablaSimCall.setItem(fila, 4, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Mujeres"])))
            self.tablaSimCall.setItem(fila, 5, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Hombres"])))
            self.tablaSimCall.setItem(fila, 6, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Total"])))
            self.tablaSimCall.setItem(fila, 7, QTableWidgetItem(str(tablaCall.at[i, "Ganancia Acumulada"])))
            self.tablaSimCall.setItem(fila, 8, QTableWidgetItem(str(round(tablaCall.at[i, "Ganancia Promedio"],4))))
            fila = fila + 1

        fila = -9
        self.tablaSimVolun.setRowCount(len(tablaVoluntariado)-9)
        for i in range(len(tablaVoluntariado)):
            self.tablaSimVolun.setItem(fila, 0, QTableWidgetItem(str(tablaVoluntariado.at[i, "Hora"])))
            self.tablaSimVolun.setItem(fila, 1, QTableWidgetItem(str(tablaVoluntariado.at[i, "Cant Llamadas"])))
            self.tablaSimVolun.setItem(fila, 2, QTableWidgetItem(str(tablaVoluntariado.at[i, "Cant Llamadas Atendidas"])))
            self.tablaSimVolun.setItem(fila, 3, QTableWidgetItem(str(tablaVoluntariado.at[i, "Cant Compras"])))
            self.tablaSimVolun.setItem(fila, 4, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Mujeres"])))
            self.tablaSimVolun.setItem(fila, 5, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Hombres"])))
            self.tablaSimVolun.setItem(fila, 6, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Total"])))
            self.tablaSimVolun.setItem(fila, 7, QTableWidgetItem(str(tablaVoluntariado.at[i, "Ganancia Acumulada"])))
            self.tablaSimVolun.setItem(fila, 8, QTableWidgetItem(str(round(tablaVoluntariado.at[i, "Ganancia Promedio"]
                                                                           , 4))))
            fila = fila + 1

    def validarDatosValidos(self):
        cantidadHoras = int(self.txtCantHoras.text())
        puntoPartida = int(self.txtPtoPartida.text())

        if cantidadHoras <= 0 or puntoPartida < 0:
            QMessageBox.warning(self, "Alerta", "Debe ingresar números positivos!")
            return False
        rangoPtoPartida = cantidadHoras - 400
        if 0 < rangoPtoPartida < puntoPartida:
            QMessageBox.warning(self, "Alerta", "El Punto de Partida no puede ser mayor a " + str(cantidadHoras - 400) +
                                " ya que no se pueden generar las 400 líneas a mostrar!")
            return False
        if cantidadHoras < puntoPartida:
            QMessageBox.warning(self, "Alerta", "El Punto de Partida no puede ser mayor a la cantidad de horas (" +
                                                str(cantidadHoras) +
                                                ") ya que no hay hora simulada con tal valor!")
            return False

        return True