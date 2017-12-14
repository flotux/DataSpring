#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

APP_NAME = "Data springs"

"""
    Root.py

    A collection of the principal windows on the programme.

        -- StartMenu -- The menu at the start of the programme.
        -- OverView -- The page how the principal informations have been print.
        """

from tkinter import *
import popUp

class StartMenu(Tk):
    """ The menu at the start of the programme. """

    def __init__(self):

        Tk.__init__(self)
        self.title(APP_NAME)
        self.configure(width=800, height=600)

        self.menuBar = Menu(self)

        self.menuFile = Menu(self.menuBar, tearoff=0)

        self.menuNew = Menu(self.menuFile, tearoff=0)
        self.menuNew.add_command(label="Fiche de reglage", command=self.n_reg)
        self.menuNew.add_command(label="Feuille de ressort", command=None)
        self.menuNew.add_command(label="Feuille d'outillage", command=None)
        self.menuFile.add_cascade(label="Nouveau", menu=self.menuNew)

        self.menuFile.add_command(label="Ouvrir", command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Sauvegarder", command=None)
        self.menuFile.add_command(label="Sauvegarder sous...", command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Quiter", command=self.destroy)
        self.menuBar.add_cascade(label="Fichier", menu=self.menuFile)

        self.config(menu=self.menuBar)

    def n_reg(self):
        """ Used too lauch a new regulation viewer """

        self.path = popUp.NewRegulationViewer()
        self.path.mainloop()

class OverView(Tk):
    """ The page how the principal informations have been print. """
    pass

if __name__ == '__main__':
    StartMenu().mainloop()
