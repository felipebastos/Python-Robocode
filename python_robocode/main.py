#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from python_robocode.GUI.window import MainWindow


def application():
    app = QApplication(sys.argv)
    app.setApplicationName("Python-Robocode")
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
