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
        regExpr = QRegExp("^([1-9]|[1-9][0-9]+)+$")
        self.txtCantHoras.setValidator(QRegExpValidator(regExpr, self))
        self.txtPtoPartida.setValidator(QRegExpValidator(regExpr, self))

    def cargarResultados(self, ganVoluntariado, ganCall, tiempoSim, tablaVoluntariado, tablaCall,
                         tablaVoluntariadoLlamadas, tablaCallLlamadas):
        self.pantallaResultados = logicaPantallaResultados.PantallaResultados(ganVoluntariado, ganCall,
                                                                         tiempoSim, tablaVoluntariado, tablaCall
                                                                              , tablaVoluntariadoLlamadas
                                                                              , tablaCallLlamadas)

        self.pantallaResultados.show()

    def nuevaSimulacion(self):

        if self.validarDatosValidos():
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

            simulaciones.nuevaSimulacion(int(self.txtCantHoras.text()), int(self.txtPtoPartida.text())-1,
                                         self, self.vectorTodasProbs)

    def validarDatosValidos(self):

        if self.txtCantHoras.text() == '' or self.txtPtoPartida.text() == '' \
                or self.txtCantHoras.text() == " " or self.txtPtoPartida.text() == " ":
            QMessageBox.warning(self, "Alerta", "Debe ingresar valores en los campos!")
            return False

        cantidadHoras = float(self.txtCantHoras.text())
        puntoPartida = float(self.txtPtoPartida.text())

        if cantidadHoras < puntoPartida:
            QMessageBox.warning(self, "Alerta", "El Punto de Partida no puede ser mayor a la cantidad de horas (" +
                                                str(cantidadHoras) +
                                                ") ya que no hay hora simulada con tal valor!")
            return False

        return True