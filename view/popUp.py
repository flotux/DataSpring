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

        # Selection of the Machine
        self.fm = LabelFrame(self, text="Machine utilisee : ")
        self.fm.grid(row=1, column=1, pady=20, padx=10)
        self.list_machine = Listbox(self.fm)
        self.list_machine.insert(1, "RX20")
        self.list_machine.insert(2, "MX20")
        self.list_machine.insert(3, "MCS20")
        self.list_machine.insert(4, "AX20")
        self.list_machine.insert(5, "MCS15-G")
        self.list_machine.insert(6, "SX15")
        self.list_machine.insert(7, "MX10")
        self.list_machine.pack(padx=10, pady=5)

        self.fw = LabelFrame(self, text="Diametre du fil : ")
        self.fw.grid(row=1, column=2, pady=20, padx=10)
        self.wire = DoubleVar()
        self.scale_wire = Spinbox(self.fw, from_=0.1, to=2.0)
        self.scale_wire.pack()

        self.quit_bton = Button(self, text="Quitter", command=self.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2)

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
