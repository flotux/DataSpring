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
WIRE_DIAMETER_LABEL = "Fil "

from tkinter import *
import utils.machlib
import utils.sprlib


class LoadPage(Tk):
    """ Find and load programmes. """
    pass


class NewRegulationViewer(Tk):
    """ Create a new regulation viewer. """

    def __init__(self):
        Tk.__init__(self)
        self.title(NEW_REGULATION)

        self.machine_frame()
        self.wire_frame()

        self.quit_bton = Button(self, text="Quitter", command=self.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2)

    def machine_frame(self):
        """ A frame for selected the machine.
            """

        self.fm = LabelFrame(self, text=MACHINE_SELECTOR_LABEL)
        self.fm.grid(row=1, column=1, pady=20, padx=10)
        # Machine selection listBox
        self.listMachine = Listbox(self.fm, height=7, width=16)
        for ind, elt in enumerate(utils.machlib.MODEL_LIST):
            self.listMachine.insert(ind, elt.get("name"))
        self.listMachine.bind('<ButtonRelease-1>',self.machine_select)
        self.listMachine.pack(padx=10, pady=5)

    def wire_frame(self):
        """ A frame for enter the diameter, references and
            material of the wire.
            """

        self.fw = LabelFrame(self, text=WIRE_DIAMETER_LABEL)
        self.fw.grid(row=1, column=2, pady=20, padx=10)
        self.wire = DoubleVar()
        self.wire.set(0.4)
        self.scaleWire = Spinbox(self.fw, from_=0.4, to=2.0, width=8,\
                                 increment=0.1, wrap=True, \
                                 command=self.wire_select)
        self.scaleWire.grid(row=1, column=2)
        Label(self.fw, text="Diametre : ").grid(row=1, column=1, padx=10, pady=8)
        Label(self.fw, text="mm").grid(row=1, column=3)
        # Wire references
        Label(self.fw, text="Reference : ").grid(row=2, column=1, padx=10, pady=8)
        self.entryWireRef = Entry(self.fw, width=10)
        self.entryWireRef.grid(row=2, column=2)
        # Wire material
        self.wire_material = StringVar()
        self.wire_material.set("Acier")
        Label(self.fw, text="Matiere : ").grid(row=3, column=1, padx=10, pady=8)
        self.radiogroup = Frame(self.fw)
        self.radiogroup.grid(row=3, column=2)
        self.steel = Radiobutton(self.radiogroup, text="Acier", indicatoron=0, \
                                 variable=self.wire_material, value="steel", \
                                 width=4)
        self.steel.grid(row=1, column=1)
        self.steel.deselect()
        self.inox = Radiobutton(self.radiogroup, text="Inox", indicatoron=0, \
                                variable=self.wire_material, value="inox", \
                                width=4)
        self.inox.grid(row=1, column=2)
        self.inox.deselect()

    def machine_select(self, evt):
        """ Whrite the machine selected on <listMachine> to
            <machine>.
            Configure the maximum wire diameter for <scaleWire> with
            the machine capacity. """

        i=self.listMachine.curselection()
        self.machine = utils.machlib.MODEL_LIST[i[0]]
        self.scaleWire.config(to=self.machine.get("capacity"))

    def wire_select(self):
        """ Set <wire> with the <scaleWire> value. """
        pass


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
