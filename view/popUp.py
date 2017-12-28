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

# Labels on interface
NEW_REGULATION = "Nouvelle fiche "
MACHINE_SELECTOR_LABEL = "Machine utilisee "
WIRE_DIAMETER_LABEL = "Diametre du fil "

from tkinter import *
import utils.machlib


class LoadPage(Tk):
    """ Find and load programmes. """
    pass


class NewRegulationViewer(Tk):
    """ Create a new regulation viewer. """

    def __init__(self):
        Tk.__init__(self)
        self.title(NEW_REGULATION)
        # Machine selection Frame
        self.fm = LabelFrame(self, text=MACHINE_SELECTOR_LABEL)
        self.fm.grid(row=1, column=1, pady=20, padx=10)
        # Machine selection listBox
        self.listMachine = Listbox(self.fm)
        for ind, elt in enumerate(utils.machlib.MODEL_LIST):
            self.listMachine.insert(ind, elt.get("name"))
        self.listMachine.bind('<ButtonRelease-1>',self.machine_select)
        self.listMachine.pack(padx=10, pady=5)
        # Wire diameter selection
        self.wire = 0.4
        self.fw = LabelFrame(self, text=WIRE_DIAMETER_LABEL)
        self.fw.grid(row=1, column=2, pady=20, padx=10)
        self.scaleWire = Spinbox(self.fw, from_=0.4, to=2.0, \
                                 increment=0.1, bg="yellow", \
                                 wrap=True, command=self.wire_select )
        self.scaleWire.pack()
        self.labelWire = Label(self.fw, text="{} mm".format(self.wire), fg="grey")
        self.labelWire.pack()

        self.quit_bton = Button(self, text="Quitter", command=self.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2)

    def machine_select(self, evt):
        """ Whrite the machine selected on <listMachine> to
            <machine>.
            Configure the maximum wire diameter for <scaleWire> with
            the machine capacity. """

        i=self.listMachine.curselection()
        self.machine = utils.machlib.MODEL_LIST[i[0]]
        self.scaleWire.config(to=self.machine.get("capacity"))
        self.scaleWire.config(bg="yellow")

    def wire_select(self):
        """ Set <wire> with the <scaleWire> value. """

        self.wire = self.scaleWire.get()
        self.scaleWire.config(bg="white")
        self.labelWire.config(text="{} mm".format(self.wire))


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
