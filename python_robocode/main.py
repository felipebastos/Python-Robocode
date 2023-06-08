#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from python_robocode.GUI.window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Python-Robocode")
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
