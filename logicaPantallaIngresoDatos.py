from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import simulaciones


class PantallaIngresoDatos(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("defPantallaIngresoDatos.ui", self)
        self.btnSimular.clicked.connect(self.nuevaSimulacion)

    def cargarResultados(self, ganVoluntariado, ganCall, tiempoSim):
        self.txtGanVol.setText(str(round(ganVoluntariado,4)))
        self.txtGanCall.setText(str(round(ganCall,4)))
        self.txtTiempo.setText(str(round(tiempoSim,2))+'s')

    def nuevaSimulacion(self):
        simulaciones.nuevaSimulacion(int(self.txtCantHoras.text()), self)
