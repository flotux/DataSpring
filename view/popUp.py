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
        self.sep = ("_" * 80)

        self.identity()
        self.machine()
        self.wire()
        self.spring()

        self.quit_bton = Button(self, text="Quitter", command=self.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2, pady=5)
        self.next_bton = Button(self, text="Suivant")
        self.next_bton.grid(row=30, column=9, padx=2, pady=5)

    def identity(self):
        """ A frame for enter informations about the customer
            and the references.
            """

        Label(self, text="Reference Piece : ").grid(row=0, column=1, \
                                                    padx=10, pady=8)
        self.id_e = Entry(self, width=20)
        self.id_e.grid(row=0, column=2)
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
        self.wire_ref_e = Entry(self.fw, width=10)
        self.wire_ref_e.grid(row=2, column=2)
        # Wire material
        self.material = StringVar()
        self.material.set("Acier")
        Label(self.fw, text="Matiere : ").grid(row=3, column=1, padx=10, pady=8)
        self.radiogroup_mat = Frame(self.fw)
        self.radiogroup_mat.grid(row=3, column=2)
        self.steel = Radiobutton(self.radiogroup_mat, text="Acier", indicatoron=0, \
                                 variable=self.material, value="steel", \
                                 width=4, activebackground="LightBlue")
        self.steel.grid(row=1, column=1)
        self.steel.deselect()
        self.inox = Radiobutton(self.radiogroup_mat, text="Inox", indicatoron=0, \
                                variable=self.material, value="inox", \
                                width=4, activebackground="LightBlue")
        self.inox.grid(row=1, column=2)
        self.inox.deselect()

    def spring(self):

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
                                 width=8, activebackground="LightBlue")
        self.right.grid(row=1, column=2)
        self.right.deselect()
        self.left = Radiobutton(self.radiogroup_dir, text="Gauche", indicatoron=0, \
                                variable=self.dir, value="left", \
                                width=8, activebackground="LightBlue")
        self.left.grid(row=1, column=3)
        self.left.deselect()

        Label(self.fs, text="Diametre exterieur : ").grid(row=2, column=1, \
                                                         padx=5, pady=8)
        self.diam = DoubleVar()
        self.diam.set(10.00)
        self.diam_e = Entry(self.fs, width=10)
        self.diam_e.grid(row=2, column=2)
        Label(self.fs, text="mm").grid(row=2, column=3)

        Label(self.fs, text="Nombre de spire : ").grid(row=3, column=1, \
                                                         padx=5, pady=8)
        self.nb = DoubleVar()
        self.nb.set(10.00)
        self.nb_e = Entry(self.fs, width=10)
        self.nb_e.grid(row=3, column=2)
        Label(self.fs, text="spires").grid(row=3, column=3)

        Label(self.fs, text="Tolerance diametre +/- : ").grid(row=4, column=1, \
                                                         padx=5, pady=8)
        self.tol = DoubleVar()
        self.tol.set(0.10)
        self.tol_e = Entry(self.fs, width=10)
        self.tol_e.grid(row=4, column=2)
        Label(self.fs, text="mm").grid(row=4, column=3)

    def tools(self):
        pass

    def machine_select(self, evt):
        """ Whrite the machine selected on <listMachine> to
            <machine>.
            Configure the maximum wire diameter for <scaleWire> with
            the machine capacity. """

        ind = 0
        while ind < self.listMachine.size():
            self.listMachine.itemconfig(ind, bg="White")
            ind += 1

        i=self.listMachine.curselection()
        self.listMachine.itemconfig(i[0], bg="LightBlue")
        self.machine = utils.machlib.MODEL_LIST[i[0]]
        self.scaleWire.config(to=self.machine.get("capacity"))

    def wire_select(self):
        """ Set <wire> with the <scaleWire> value. """
        pass


class Add_slide(Tk):
    """ Add a slide in overlay.
        """

    def __init__(self, machine):

        Tk.__init__(self)
        self.resizable(False, False)
        self.machine = machine

        self.f1 = Frame(self)
        self.f1.grid(row=1, column=1, padx=70, pady=10)
        self.tool_b = Button(self.f1, text="Outil", command=self.tool, width=10)
        self.tool_b.grid(row=1, column=1, pady=10)
        self.spin_b = Button(self.f1, text="Tournette", command=self.spin, width=10)
        self.spin_b.grid(row=1, column=2, pady=10)

        self.f2 = Frame(self)
        self.f2.grid(row=2, column=1)
        self.lf = LabelFrame(self.f2, text="Informations", width=120, height=100)
        self.lf.pack()

        self.f3 = Frame(self)
        self.f3.grid(row=3, column=1)
        self.quit = Button(self.f3, text="Quitter", command=self.destroy)
        self.quit.grid(row=1, column=2, padx=10, pady=5)


    def tool(self):
        """ for add a tool. """

        def add_sta():
            self.sta.config(bg="LightBlue")
            self.stu.config(bg="Grey")
            self.sc.config(bg="Grey")

        def add_stu():
            self.stu.config(bg="LightBlue")
            self.sta.config(bg="Grey")
            self.sc.config(bg="Grey")


        def add_sc():
            self.sc.config(bg="LightBlue")
            self.sta.config(bg="Grey")
            self.stu.config(bg="Grey")


        self.tool_b.config(bg="LightBlue")

        self.sta = Button(self.lf, text="STA", command=add_sta, width=8)
        self.sta.grid(row=0, column=1, padx=10, pady=10)
        self.stu = Button(self.lf, text="STU", command=add_stu, width=8)
        self.stu.grid(row=0, column=2, padx=10, pady=10)
        self.sc = Button(self.lf, text="SC", command=add_sc, width=8)
        self.sc.grid(row=0, column=3, padx=10, pady=10)

        Label(self.lf, text="Nom : ", width=10).grid(row=1, column=1, padx=10, pady=5)
        self.name_e = Entry(self.lf, width=20)
        self.name_e.grid(row=1, column=2, padx=10, pady=5, columnspan=2)

        Label(self.lf, text="Accesoire : ", width=10).grid(row=3, column=1, padx=10, pady=5)
        self.attachmnent_e = Entry(self.lf, width=20)
        self.attachmnent_e.grid(row=3, column=2, padx=10, pady=5, columnspan=2)

        Label(self.lf, text="Note : ", width=10).grid(row=10, column=2, padx=10, pady=5)
        self.note = Entry(self.lf)
        self.note.grid(row=11, column=2, padx=10, pady=5)

        self.next = Button(self.f3, text="Suivant", command=None)
        self.next.grid(row=1, column=1, padx=10, pady=5)



    def spin(self):
        """ for add a spinner. """
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
