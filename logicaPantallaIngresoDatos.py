from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

import logicaPantallaResultados
import simulaciones


class PantallaIngresoDatos(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("defPantallaIngresoDatos.ui", self)
        self.btnSimular.clicked.connect(self.nuevaSimulacion)

        """Validación de que se acepten campos enteros y solo números"""
        regExpr = QRegExp("^([1-9]|[1-9][0-9]+)+$")
        self.txtCantHoras.setValidator(QRegExpValidator(regExpr, self))
        self.txtPtoPartida.setValidator(QRegExpValidator(regExpr, self))
        self.txtCantLlamadasVol.setValidator(QRegExpValidator(regExpr, self))
        self.txtCantLlamadasCall.setValidator(QRegExpValidator(regExpr, self))
        self.txtRecCall.setValidator(QRegExpValidator(regExpr, self))
        self.txtProbsAtendidas.setValidator(QRegExpValidator(regExpr, self))
        self.txtProbAtMujer.setValidator(QRegExpValidator(regExpr, self))
        self.txtCompraMujer.setValidator(QRegExpValidator(regExpr, self))
        self.txtCompraHombre.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoM1.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoM2.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoM3.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoM4.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcM1.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcM2.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcM3.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcM4.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoH1.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoH2.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoH3.setValidator(QRegExpValidator(regExpr, self))
        self.txtGastoH4.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcH1.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcH2.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcH3.setValidator(QRegExpValidator(regExpr, self))
        self.txtPorcH4.setValidator(QRegExpValidator(regExpr, self))



    def cargarResultados(self, ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall,
                         tablaVoluntariadoLlamadas, tablaCallLlamadas):
        self.pantallaResultados = logicaPantallaResultados.PantallaResultados(ganVoluntariado, ganCall,
                                                                         tiempoSim, tablaVoluntariado, tablaCall
                                                                              , tablaVoluntariadoLlamadas
                                                                              , tablaCallLlamadas)

        self.pantallaResultados.show()

    def nuevaSimulacion(self):


        if self.validarCamposNoVacios():
            """VectorProb = [[ProbAtencion, ProbMujer, ProbMujerCompra, ProbHombreCompra],
                                  [GM1, PM1, GM2, PM2, GM3, PM3, GM4, PM4],
                                  [GH1, PH1, GH2, PH2, GH3, PH3, PH4, PH4],
                                  [CantLlamadasVol, CantLlamadasCall, Comision]]"""
            vectorLlamadas = [int(self.txtCantLlamadasVol.text()), int(self.txtCantLlamadasCall.text()),
                              float(self.txtRecCall.text())]
            vectorProbs = [float(self.txtProbsAtendidas.text()) / 100,
                           float(self.txtProbAtMujer.text()) / 100,
                           float(self.txtCompraMujer.text()) / 100,
                           float(self.txtCompraHombre.text()) / 100]

            vectorGastosMujeres = [float(self.txtGastoM1.text()), float(self.txtPorcM1.text()) / 100,
                                   float(self.txtGastoM2.text()), float(self.txtPorcM2.text()) / 100,
                                   float(self.txtGastoM3.text()), float(self.txtPorcM3.text()) / 100,
                                   float(self.txtGastoM4.text()), float(self.txtPorcM4.text()) / 100]

            vectorGastosHombres = [float(self.txtGastoH1.text()), float(self.txtPorcH1.text()) / 100,
                                   float(self.txtGastoH2.text()), float(self.txtPorcH2.text()) / 100,
                                   float(self.txtGastoH3.text()), float(self.txtPorcH3.text()) / 100,
                                   float(self.txtGastoH4.text()), float(self.txtPorcH4.text()) / 100]

            self.vectorTodasProbs = [vectorProbs, vectorGastosMujeres, vectorGastosHombres, vectorLlamadas]

            if self.validarDatos(self.vectorTodasProbs):

                simulaciones.nuevaSimulacion(int(self.txtCantHoras.text()), int(self.txtPtoPartida.text()) - 1,
                                             self, self.vectorTodasProbs)

    def validarCamposNoVacios(self):
        vectorStrings = [self.txtCantHoras.text(), self.txtPtoPartida.text(), self.txtCantLlamadasVol.text(),
                         self.txtCantLlamadasCall.text(), self.txtRecCall.text(), self.txtProbsAtendidas.text(),
                         self.txtProbAtMujer.text(), self.txtCompraMujer.text(), self.txtCompraHombre.text(),
                         self.txtGastoM1.text(), self.txtGastoM2.text(), self.txtGastoM3.text(), self.txtGastoM4.text(),
                         self.txtPorcM1.text(), self.txtPorcM2.text(), self.txtPorcM3.text(), self.txtPorcM4.text(),
                         self.txtGastoH1.text(), self.txtGastoH2.text(), self.txtGastoH3.text(), self.txtGastoH4.text(),
                         self.txtPorcH1.text(), self.txtPorcH2.text(), self.txtPorcH3.text(), self.txtPorcH4.text()]

        for string in vectorStrings:
            if string == '' or string == " ":
                QMessageBox.warning(self, "Alerta", "Debe ingresar valores en los campos!")
                return False
                break
        return True

    def validarDatos(self, vector):

        cantidadHoras = float(self.txtCantHoras.text())
        puntoPartida = float(self.txtPtoPartida.text())

        if cantidadHoras < puntoPartida:
            QMessageBox.warning(self, "Alerta", "El Punto de Partida no puede ser mayor a la cantidad de horas (" +
                                                str(cantidadHoras) +
                                                ") ya que no hay hora simulada con tal valor!")
            return False

        if not self.validarDatosVector(vector):
            return False

        return True

    def validarDatosVector(self, vector):
        """VectorProb = [[ProbAtencion, ProbMujer, ProbMujerCompra, ProbHombreCompra],
                                          [GM1, PM1, GM2, PM2, GM3, PM3, GM4, PM4],
                                          [GH1, PH1, GH2, PH2, GH3, PH3, PH4, PH4],
                                          [CantLlamadasVol, CantLlamadasCall, Comision]]"""
        for i in range(len(vector[0])):
            if vector[0][i] > 1:
                QMessageBox.warning(self, "Alerta", "Los porcentajes de probabilidad deben ser menor o igual a 100%")
                return False

        probabilidadesMujeres = 0
        for i in range(1, len(vector[1]), 2):
            probabilidadesMujeres += vector[1][i]

        if probabilidadesMujeres != 1:
            QMessageBox.warning(self, "Alerta", "La suma de los porcentajes de probabilidad"
                                                " de Gasto de las Mujeres debe sumar 100%")
            return False

        probabilidadesHombres = 0
        for i in range(1, len(vector[2]), 2):
            probabilidadesHombres += vector[2][i]

        if probabilidadesHombres != 1:
            QMessageBox.warning(self, "Alerta", "La suma de los porcentajes de probabilidad"
                                                " de Gasto de los Hombres debe sumar 100%")
            return False


        if vector[3][2] > 100:
            QMessageBox.warning(self, "Alerta", "Los porcentajes de probabilidad deben ser menor o igual a 100%")
            return False

        return True