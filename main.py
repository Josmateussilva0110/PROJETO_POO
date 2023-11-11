from funcionartelamain import *
from PyQt5.QtWidgets import QApplication 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Ui_Main()
    sys.exit(app.exec_())
