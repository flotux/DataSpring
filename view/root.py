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
from tkinter.ttk import *
from . import popUp

class Root(Tk):
    """ The menu at the start of the programme. """

    def __init__(self):

        Tk.__init__(self)
        self.title(APP_NAME)
        self.configure(width=800, height=600)

        self.menuBar = Menu(self)

        self.menuFile = Menu(self.menuBar, tearoff=0)

        self.menuNew = Menu(self.menuFile, tearoff=0)
        self.menuNew.add_command(label="Fiche de reglage", command=self.new_reg)
        self.menuNew.add_command(label="Feuille de ressort", command=None)
        self.menuNew.add_command(label="Feuille d'outillage", command=None)
        self.menuFile.add_cascade(label="Nouveau", menu=self.menuNew)

        self.menuFile.add_command(label="Ouvrir", command=self.launch_overview)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Sauvegarder", command=None)
        self.menuFile.add_command(label="Sauvegarder sous...", command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Quiter", command=self.destroy)
        self.menuBar.add_cascade(label="Fichier", menu=self.menuFile)

        self.config(menu=self.menuBar)


    def new_reg(self):
        """ Used too lauch a new regulation viewer """

        self.path = popUp.NewRegulationViewer()
        self.path.mainloop()

    def launch_overview(self):

        self.path = OverView()
        self.path.mainloop()


class OverView(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.machine = "MX20"
        self.overlay()

    def overlay(self):
        """ Overlay of the machine.
            """

        # width
        canw = 220
        canw2 = canw/2
        blocw = 110
        # height
        canh = 220
        canh2 = canh/2
        bloch = 180

        def add():
            """ Adding a slide on layout,
                start the Add_Slide class in popUp.py for
                editing the configuration of the new slide.
                """

            # start the widget for configure the slide.
            popUp.Add_slide(self.machine).mainloop()
            # configure the frame for print the slide information.

        # the overlay is a canvas.
        self.can = Canvas(self, width=canw, height=canh)
        self.can.grid(row=1, column=1, columnspan=3, rowspan=3)

        # creation of line for better visibiliter.
        self.can.create_line(canw2, 0, canw2, canh, width=1.4)
        self.can.create_line(0, canh2, canw, canh2, width=1.4)
        self.can.create_line(0, 0, canw, canh, width=1.4)
        self.can.create_line(canw, 0, 0, canh, width=1.4)
        self.can.create_oval(canw2-20, canh2-20, canw2+20, canh/2+20)

        # the 8 machine slides is representing by a LabelFrame, a Button
        # is placed in every element for adding tool or spinner.
        self.bloc1 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc1.grid(row=0, column=2, padx=10, pady=10)
        self.add1 = Button(self.bloc1, text="AJOUTER", command=add)
        self.add1.pack(padx=20, pady=40)
        self.bloc2 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc2.grid(row=0, column=5, padx=10, pady=10)
        self.add2 = Button(self.bloc2, text="AJOUTER", command=add)
        self.add2.pack(padx=20, pady=40)
        self.bloc3 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc3.grid(row=2, column=5, padx=10, pady=10)
        self.add3 = Button(self.bloc3, text="AJOUTER", command=add)
        self.add3.pack(padx=20, pady=40)
        self.bloc4 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc4.grid(row=5, column=5, padx=10, pady=10)
        self.add4 = Button(self.bloc4, text="AJOUTER", command=add)
        self.add4.pack(padx=20, pady=40)
        self.bloc5 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc5.grid(row=5, column=2, padx=10, pady=10)
        self.add5 = Button(self.bloc5, text="AJOUTER", command=add)
        self.add5.pack(padx=20, pady=40)
        self.bloc6 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc6.grid(row=5, column=0, padx=10, pady=10)
        self.add6 = Button(self.bloc6, text="AJOUTER", command=add)
        self.add6.pack(padx=20, pady=40)
        self.bloc7 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc7.grid(row=2, column=0, padx=10, pady=10)
        self.add7 = Button(self.bloc7, text="AJOUTER", command=add)
        self.add7.pack(padx=20, pady=40)
        self.bloc8 = LabelFrame(self, width=blocw, height=bloch)
        self.bloc8.grid(row=0, column=0, padx=10, pady=10)
        self.add8 = Button(self.bloc8, text="AJOUTER", command=add)
        self.add8.pack(padx=20, pady=40)

    def characteristic(self):
        pass

    def informations(self):
        pass

    def entry(self):
        pass


if __name__ == '__main__':
    Root().mainloop()
