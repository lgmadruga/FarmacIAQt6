import sys
from PyQt6.QtWidgets import QApplication
from views.MainWindow import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())

