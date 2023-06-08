#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Main module for Python Robocode project."""

import sys

from PyQt5.QtWidgets import QApplication

from python_robocode.GUI.window import MainWindow


def application():
    """Runs the application from base window.

    This function is the root for calling the project as a CLI.

    To execute the application you should use:

    $ pyrobocode

    This is valid for when you install the project throught pip or pipx.
    If you've cloned the repository, you may use:

    (virtualenv) $ task run
    """
    app = QApplication(sys.argv)
    app.setApplicationName("Python-Robocode")
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
