from PyQt6 import QtWidgets
import sys
from win import prihlaseni as s

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    prihlaseni = QtWidgets.QMainWindow()
    ui = s.Ui_prihlaseni()
    ui.setupUi(prihlaseni)
    prihlaseni.show()
    sys.exit(app.exec())