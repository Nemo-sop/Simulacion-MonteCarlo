import sys
from PyQt5.QtWidgets import QApplication

import logicaPantallaIngresoDatos as interfaz


def inicializarPantalla():
    app = QApplication(sys.argv)
    GUI = interfaz.PantallaIngresoDatos()
    GUI.show()
    sys.exit(app.exec_())


inicializarPantalla()



