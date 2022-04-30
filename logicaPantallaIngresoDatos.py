from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class PantallaIngresoDatos(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("defPantallaIngresoDatos.ui", self)
        # self.btnSimular.clicked.connect(self.nuevaSimulacion)

    def cargarResultados(self, ganVoluntariado, ganCall, tiempoSim):
        self.txtGanVol.setText(ganVoluntariado)
        self.txtGanCall.setText(ganCall)
        self.txtTiempo.setText(str(tiempoSim))

    # def nuevaSimulacion(self):
    #     Main.nuevaSimulacion(int(self.txtCantHoras.text()), self)
