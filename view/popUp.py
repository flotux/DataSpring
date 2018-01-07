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
MACHINE_SELECTOR_LABEL = "Machine "
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

        self.identity()
        self.machine()
        self.wire()
        self.spring()

        self.quit_bton = Button(self, text="Quitter", command=self.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2)

    def identity(self):
        """ A frame for enter informations about the customer
            and the references.
            """

        Label(self, text="Reference Piece : ").grid(row=0, column=1, \
                                                    padx=10, pady=8)
        self.id = Entry(self, width=20)
        self.id.grid(row=0, column=2)
        Label(self, text="Client : ").grid(row=0, column=3, padx=10, pady=8)
        self.customer = Entry(self, width=10)
        self.customer.grid(row=0, column=4)

    def machine(self):
        """ A frame for selected the machine.
            """

        self.fm = LabelFrame(self, text=MACHINE_SELECTOR_LABEL)
        self.fm.grid(row=1, column=1, pady=20, padx=10, columnspan=2)
        # Machine selection listBox
        self.listMachine = Listbox(self.fm, height=7, width=16)
        for ind, elt in enumerate(utils.machlib.MODEL_LIST):
            self.listMachine.insert(ind, elt.get("name"))
        self.listMachine.bind('<ButtonRelease-1>',self.machine_select)
        self.listMachine.pack(padx=10, pady=5)

    def wire(self):
        """ A frame for enter the diameter, references and
            material of the wire.
            """

        self.fw = LabelFrame(self, text=WIRE_DIAMETER_LABEL)
        self.fw.grid(row=1, column=3, pady=20, padx=10, columnspan=2)
        self.wire = DoubleVar()
        self.wire.set(0.4)
        self.scaleWire = Spinbox(self.fw, from_=0.4, to=2.0, width=8,\
                                 increment=0.1, wrap=True, \
                                 command=self.wire_select)
        self.scaleWire.grid(row=1, column=2)
        Label(self.fw, text="Diametre : ").grid(row=1, column=1, \
                                                padx=10, pady=8)
        Label(self.fw, text="mm").grid(row=1, column=3)
        # Wire references
        Label(self.fw, text="Reference : ").grid(row=2, column=1, \
                                                 padx=10, pady=8)
        self.entryWireRef = Entry(self.fw, width=10)
        self.entryWireRef.grid(row=2, column=2)
        # Wire material
        self.material = StringVar()
        self.material.set("Acier")
        Label(self.fw, text="Matiere : ").grid(row=3, column=1, padx=10, pady=8)
        self.radiogroup_mat = Frame(self.fw)
        self.radiogroup_mat.grid(row=3, column=2)
        self.steel = Radiobutton(self.radiogroup_mat, text="Acier", indicatoron=0, \
                                 variable=self.material, value="steel", \
                                 width=4)
        self.steel.grid(row=1, column=1)
        self.steel.deselect()
        self.inox = Radiobutton(self.radiogroup_mat, text="Inox", indicatoron=0, \
                                variable=self.material, value="inox", \
                                width=4)
        self.inox.grid(row=1, column=2)
        self.inox.deselect()

    def spring(self):

        self.sep = ("_" * 80)
        Label(self, text=self.sep).grid(row=2, padx=2, pady=10, columnspan=10)

        self.fs = Frame(self)
        self.fs.grid(row=3, column=0, pady=20, padx=10, columnspan=4)

        self.dir = StringVar()
        self.dir.set("Right")
        Label(self.fs, text="sens d'enroulement : ").grid(row=1, column=1, \
                                                          padx=5, pady=8)
        self.radiogroup_dir = Frame(self.fs)
        self.radiogroup_dir.grid(row=1, column=2)
        self.right = Radiobutton(self.radiogroup_dir, text="Droite", indicatoron=0, \
                                 variable=self.dir, value="right", \
                                 width=8)
        self.right.grid(row=1, column=2)
        self.right.deselect()
        self.left = Radiobutton(self.radiogroup_dir, text="Gauche", indicatoron=0, \
                                variable=self.dir, value="left", \
                                width=8)
        self.left.grid(row=1, column=3)
        self.left.deselect()

        Label(self.fs, text="Diametre exterieur : ").grid(row=2, column=1, \
                                                         padx=5, pady=8)
        self.diam = DoubleVar()
        self.diam.set(10.00)
        self.entryDiam = Entry(self.fs, width=10)
        self.entryDiam.grid(row=2, column=2)
        Label(self.fs, text="mm").grid(row=2, column=3)

        Label(self.fs, text="Nombre de spire : ").grid(row=3, column=1, \
                                                         padx=5, pady=8)
        self.nb = DoubleVar()
        self.nb.set(10.00)
        self.entryNb = Entry(self.fs, width=10)
        self.entryNb.grid(row=3, column=2)
        Label(self.fs, text="spires").grid(row=3, column=3)

        Label(self.fs, text="Tolerance diametre +/- : ").grid(row=4, column=1, \
                                                         padx=5, pady=8)
        self.tol = DoubleVar()
        self.tol.set(0.10)
        self.entryTol = Entry(self.fs, width=10)
        self.entryTol.grid(row=4, column=2)
        Label(self.fs, text="mm").grid(row=4, column=3)

    def tools(self):
        pass



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
