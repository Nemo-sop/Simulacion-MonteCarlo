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


        columnas = ["Hora", "Cant Llamadas", "Cant Llamadas Atendidas", "Cant Compras", "Ganancia Mujeres",
                    "Ganancia Hombres", "Ganancia Total", "Ganancia Acumulada", "Ganancia Promedio"]

        # for i in range(len(tablaVoluntariado)):
        #     for j in columnas:
        #         self.tablaSimVolun.setItem(fila, i, QTableWidgetItem(str(tablaVoluntariado.at[i, j])))

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


        #
        #
        #
        # for i in range(len(self.tablaCall)):
        #     self.tablaSimCall.setItem(fila, 0, QTableWidgetItem(numero[0]))
        #     self.tablaSimCall.setItem(fila, 1, QTableWidgetItem(str(self.frecuencias.at[i, "Frec. Observadas"])))
        #     self.tablaSimCall.setItem(fila, 2, QTableWidgetItem(str(self.frecuencias.at[i, "Frec. Esperada"])))
        #     self.tablaSimCall.setItem(fila, 3, QTableWidgetItem(str(self.frecuencias.at[i, "Frec. Relativa"])))
        #     self.tablaSimCall.setItem(fila, 4, QTableWidgetItem(str(self.frecuencias.at[i, "Marca de Clase"])))

    def validarDatosValidos(self):
        cantidadHoras = self.txtCantHoras.text()
        puntoPartida = self.txtPtoPartida.text()

        if cantidadHoras == '' or puntoPartida == '':
            QMessageBox.warning(self, "Alerta", "Debe ingresar valores en los campos!")
            return False
        if float(cantidadHoras) <= 0 or float(puntoPartida) < 0:
            QMessageBox.warning(self, "Alerta", "Debe ingresar números positivos!")
            return False
        if not self.esDecimal():
            QMessageBox.warning(self, "Alerta", "Los números a ingresar deben ser enteros!")
            return False
        if float(puntoPartida) > (float(cantidadHoras) - 400):
            QMessageBox.warning(self, "Alerta", "El Punto de Partida no puede ser mayor a " + str(cantidadHoras - 400) +
                                " ya que no se pueden generar las 400 líneas a mostrar!")
            return False
        if float(cantidadHoras) < float(puntoPartida):
            QMessageBox.warning(self, "Alerta", "El Punto de Partida no puede ser mayor a la cantidad de horas (" +
                                                str(cantidadHoras) +
                                                ") ya que no hay hora simulada con tal valor!")
            return False

        return True