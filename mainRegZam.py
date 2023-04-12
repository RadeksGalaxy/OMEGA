from PyQt6 import QtWidgets
import sys
from winZam import registraceZam as s

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = s.Ui_RegistraceZam()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
    except Exception:
        pass