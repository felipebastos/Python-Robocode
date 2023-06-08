# -*- coding: utf-8 -*-

"""
Module implementing Battle.
"""

import os
import pickle
from importlib import import_module

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from python_robocode.GUI.Ui_battle import Ui_Dialog
from python_robocode.Objects.robot import Robot


class Battle(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.window = parent
        bot_names = []
        self.list_bots = {}
        bot_files = os.listdir(os.path.join(os.getcwd(), "python_robocode", "Robots"))
        for bot_file in bot_files:
            if bot_file.endswith(".py"):
                bot_name = bot_path = bot_file[: bot_file.rfind(".")]
                if bot_name not in bot_names:
                    bot_names.append(bot_name)
                    try:
                        bot_module = import_module(f"python_robocode.Robots.{bot_path}")

                        for name in dir(bot_module):
                            if getattr(bot_module, name) in Robot.__subclasses__():
                                some_bot = getattr(bot_module, name)
                                bot = some_bot
                                self.list_bots[
                                    str(bot).replace("<class '", "").replace("'>", "")
                                ] = bot
                                break
                    except Exception as exception:
                        print(f"Problem with bot file '{bot_file}': {str(exception)}")

        for key in self.list_bots:
            self.listWidget.addItem(key)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Add Bot
        """

        self.listWidget_2.addItem(self.listWidget.currentItem().text())

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Remove Bot
        """
        item = self.listWidget_2.takeItem(self.listWidget_2.currentRow())
        item = None

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Start
        """
        width = self.spinBox.value()
        height = self.spinBox_2.value()
        bot_list = []
        for i in range(self.listWidget_2.count()):
            key = str(self.listWidget_2.item(i).text())
            bot_list.append(self.list_bots[key])

        self.save(width, height, bot_list)
        self.window.setUpBattle(width, height, bot_list)

    def save(self, width, height, bot_list):
        """Saves the battle configuration.

        Args:
            width (float): Field width
            height (float): Field height
            botList (List[Robot]): List of robots selected
        """
        dico = {}
        dico["width"] = width
        dico["height"] = height
        dico["botList"] = bot_list

        if not os.path.exists(os.getcwd() + "/.datas/"):
            os.makedirs(os.getcwd() + "/.datas/")

        with open(os.getcwd() + "/.datas/lastArena", "wb") as file:
            pickler = pickle.Pickler(file)
            pickler.dump(dico)
        file.close()
