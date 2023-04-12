from PyQt6 import QtWidgets
import sys
from src.win import prihlaseni as s

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        prihlaseni = QtWidgets.QMainWindow()
        ui = s.Ui_Prihlaseni()
        ui.setupUi(prihlaseni)
        prihlaseni.show()
        sys.exit(app.exec())
    except Exception:
        pass