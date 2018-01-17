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

#==== Imports ==================================================================
from tkinter import *
from tkinter.ttk import *
#==========================#
import utils.machlib
import utils.sprlib
import utils.tklib
import utils.guilib
#==========================#
import view.popUp
import view.add_slide
import view.new_regulation
#===============================================================================


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

        self.new_regulation_windows = Toplevel(self)
        self.new_regulation_windows.transient(self)
        windows = view.new_regulation.NewRegulation(self.new_regulation_windows)

    def launch_overview(self):

        self.path = OverView()
        self.path.mainloop()


class OverView(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.machine = "MCS20"
        self.overlay()

    def overlay(self):
        """ Overlay of the machine.
            """

        # width, height of the canvas self.can
        canw, canh = 220, 220
        canw2, canh2 = canw/2, canh/2

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
        self.bloc1, add1 = utils.tklib.overbutton(self, 0, 2, self.add_slide)
        self.bloc2, add2 = utils.tklib.overbutton(self, 0, 5, self.add_slide)
        self.bloc3, add3 = utils.tklib.overbutton(self, 2, 5, self.add_slide)
        self.bloc4, add4 = utils.tklib.overbutton(self, 5, 5, self.add_slide)
        self.bloc5, add5 = utils.tklib.overbutton(self, 5, 2, self.add_slide)
        self.bloc6, add6 = utils.tklib.overbutton(self, 5, 0, self.add_slide)
        self.bloc7, add7 = utils.tklib.overbutton(self, 2, 0, self.add_slide)
        self.bloc8, add8 = utils.tklib.overbutton(self, 0, 0, self.add_slide)


    def add_slide(self):
        """ Adding a slide on layout,
            start the Add_Slide class in popUp.py for
            editing the configuration of the new slide.
            """

        self.add_window = Toplevel(self)
        window = view.add_slide.Add_slide(self.add_window, self.machine)
        # configure the frame for print the slide information.

    def characteristic(self):
        pass

    def informations(self):
        pass

    def entry(self):
        pass


if __name__ == '__main__':
    Root().mainloop()
