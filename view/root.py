#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

APP_NAME = "Data springs"

"""
    Root.py

    The main windows of the programme, contains many class.

        -- Overlay
        -- Geometry
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
        self.geometry("1024x768+384+0")
        self.resizable(width=False,height=False)

        # Creation of the menu
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
        self.menuFile.add_command(label="Quitter", command=self.destroy)
        self.menuBar.add_cascade(label="Fichier", menu=self.menuFile)

        self.config(menu=self.menuBar)

    def new_reg(self):
        """ Used too lauch a new regulation viewer """

        self.new_regulation_windows = Toplevel(self)
        self.new_regulation_windows.transient(self)
        windows = view.new_regulation.NewRegulation(self.new_regulation_windows)

    def launch_overview(self):

        self.overlay = Overlay(self)
        self.overlay.grid(row=1, column=1, rowspan=2, columnspan=2)
        self.geometry = Geometry(self)
        self.geometry.grid(row=1, column=0)


#===============================================================================
class Overlay(Frame):
    """
        The Classe Overlay is a visual representation of the machine overlay,
        it's use too place the slides and add tools, spinners, linear motors,
        cammes and commentary.

        in first, a canva is used to draw lines and circle
        for a greate visibility.
        8 blocs are place like the 8 slides of the machine, a button
        on each bloc allows to add tool or spinner on it.
        The spinner/tool added is written on the bloc.
        """

    def __init__(self, master):
        Frame.__init__(self, master)
        self.machine = "MCS20"

        # width, height of the canvas self.can
        canw = canh = 220
        canw2 = canh2 = 110

        # the overlay is an canvas.
        self.can = Canvas(self, width=canw, height=canh)
        self.can.grid(row=1, column=1, columnspan=3, rowspan=3)

        # creation of lines and oval in the center of
        # the canvas for a better visibility.
        self.can.create_line(canw2, 0, canw2, canh, width=1.4)
        self.can.create_line(0, canh2, canw, canh2, width=1.4)
        self.can.create_line(0, 0, canw, canh, width=1.4)
        self.can.create_line(canw, 0, 0, canh, width=1.4)
        self.can.create_oval(canw2-20, canh2-20, canw2+20, canh/2+20)

        # the 8 machine slides are represent by a LabelFrame, a Button
        # is placed on each element for adding tool or spinner.
        self.bloc1, add1 = utils.tklib.overbutton(self, 0, 2, self.add_slide)
        self.bloc2, add2 = utils.tklib.overbutton(self, 0, 5, self.add_slide)
        self.bloc3, add3 = utils.tklib.overbutton(self, 2, 5, self.add_slide)
        self.bloc4, add4 = utils.tklib.overbutton(self, 5, 5, self.add_slide)
        self.bloc5, add5 = utils.tklib.overbutton(self, 5, 2, self.add_slide)
        self.bloc6, add6 = utils.tklib.overbutton(self, 5, 0, self.add_slide)
        self.bloc7, add7 = utils.tklib.overbutton(self, 2, 0, self.add_slide)
        self.bloc8, add8 = utils.tklib.overbutton(self, 0, 0, self.add_slide)


    def add_slide(self):
        """ For add a slide on the layout, just
            launch the Add_slide class
            """

        self.add_window = Toplevel(self.master)
        window = view.add_slide.Add_slide(self.add_window, self.machine)
        # configure the frame for print the slide information.


#===============================================================================
class Geometry(LabelFrame):
    """ Print the information of the spring. """

    def __init__(self, master):
        LabelFrame.__init__(self, master, text="Information")

        self.diam = utils.tklib.info_label(self, "Diametre exterieur", 12.0, 0)
        self.tol = utils.tklib.info_label(self, "toleration", 0.1, 1)
        self.nb = utils.tklib.info_label(self, "Nombre de spires", 5.5, 2)
        self.de = utils.tklib.info_label(self, "Diametre exterieur", 12.0, 3)
        self.dr = utils.tklib.info_label(self, "Diametre exterieur", 12.0, 4)


#===============================================================================
class CalculateValue(LabelFrame):
    pass


#===============================================================================
class Sensors(LabelFrame):
    pass


#===============================================================================
class Note(LabelFrame):
    pass


#===============================================================================
class InputOutput(LabelFrame):
    pass


#===============================================================================
class Counter(LabelFrame):
    pass


#===============================================================================
class ProductionData(LabelFrame):
    pass
