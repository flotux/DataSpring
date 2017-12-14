#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

"""
    popUp.py

    Contain the pop up pages.

        -- LoadPage -- Find and load programmes.
        -- NewPage -- Create a new programme.
        -- EntryConf -- Configure Entry.
        -- SensorConf -- Configure Sensors.
        -- CalcSpr -- Calculate values for springs.
        -- CalcSpin -- Calculate values for spinners.
        """

NEW_REGULATION = "Nouvelle fiche"

from tkinter import *


class LoadPage(Tk):
    """ Find and load programmes. """
    pass


class NewRegulationViewer(Tk):
    """ Create a new regulation viewer. """

    def __init__(self):
        Tk.__init__(self)
        self.title(NEW_REGULATION)
        self.resizable(False,False)

        # Selection of the Machine
        self.f = LabelFrame(self, text="Machine utilisee : ")
        self.f.grid(row=1, column=1, pady=20, padx=10)
        # 2mm machines
        self.bton1 = Button(self.f, text="MX20", relief=FLAT)
        self.bton1.grid(row=2, column=2, columnspan=3, ipadx=50)
        self.bton2 = Button(self.f, text="RX20", relief=FLAT)
        self.bton2.grid(row=3, column=2, columnspan=3, ipadx=50)
        self.bton3 = Button(self.f, text="MCS20", relief=FLAT)
        self.bton3.grid(row=4, column=2, columnspan=3, ipadx=50)
        self.bton4 = Button(self.f, text="AX20", relief=FLAT)
        self.bton4.grid(row=5, column=2, columnspan=3, ipadx=50)
        # 1.5mm machines
        self.bton5 = Button(self.f, text="MCS-15G", relief=FLAT)
        self.bton5.grid(row=6, column=2, columnspan=3, ipadx=50)
        self.bton6 = Button(self.f, text="SX15", relief=FLAT)
        self.bton6.grid(row=7, column=2, columnspan=3, ipadx=50)
        # 1mm machines
        self.bton7 = Button(self.f, text="MX10", relief=FLAT)
        self.bton7.grid(row=8, column=2, columnspan=3, ipadx=50)

        self.quit_bton = Button(self, text="Quitter", command=self.destroy)
        self.quit_bton.grid(row=10, column=10, padx=2)

class EntryConf(Tk):
    """ Configure Entry. """
    pass


class SensorConf(Tk):
    """ Configure Sensors. """
    pass


class CalcSpr(Tk):
    """ Calculate values for springs. """
    pass


class CalcSpin(Tk):
    """ Calculate values for spinners. """
    pass

if __name__ == '__main__':
    NewRegulationViewer().mainloop()
