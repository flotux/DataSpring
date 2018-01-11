#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

"""
    popUp.py

    Contain the pop up pages.

        -- NewRegulationViewer -- create new regulation viewer.
        -- Add_slide -- add a slide in overlay.
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
        # the windows is diviser by frame, any frame have a function,
        # all functions are launch at the degining.
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
        """ A frame for selected the machine,
            according the MODEL_list in utils/machlib.
            """

        self.fm = LabelFrame(self, text=MACHINE_SELECTOR_LABEL)
        self.fm.grid(row=1, column=1, pady=20, padx=10, columnspan=2)
        # Machine selection listBox
        self.listMachine = Listbox(self.fm, height=7, width=16)
        for ind, elt in enumerate(utils.machlib.MODEL_LIST):
            self.listMachine.insert(ind, elt.get("name"))
        # launch the machine_select function when a machine is select.
        self.listMachine.bind('<ButtonRelease-1>',self.machine_select)
        self.listMachine.pack(padx=10, pady=5)

    def wire(self):
        """ A frame for enter the diameter, references and
            type material of the wire.
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
                                 width=4, selectcolor="LightBlue")
        self.steel.grid(row=1, column=1)
        self.steel.deselect()
        self.inox = Radiobutton(self.radiogroup_mat, text="Inox", indicatoron=0, \
                                variable=self.material, value="inox", \
                                width=4, selectcolor="LightBlue")
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
                                 width=8, selectcolor="LightBlue")
        self.right.grid(row=1, column=2)
        self.right.deselect()
        self.left = Radiobutton(self.radiogroup_dir, text="Gauche", indicatoron=0, \
                                variable=self.dir, value="left", \
                                width=8, selectcolor="LightBlue")
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

    def machine_select(self, evt):
        """ executed when a machine is selected.
            change the maximum size of the wire according The
            machine selected.
            """
        # this block set all element in the listbox in white background,
        # for more lisibiliter.
        ind = 0
        while ind < self.listMachine.size():
            self.listMachine.itemconfig(ind, bg="White")
            ind += 1
        # set the current selection in LightBlue background.
        i=self.listMachine.curselection()
        self.listMachine.itemconfig(i[0], bg="LightBlue")
        # according the capacity of the machine selected, change the wire
        # maximum size can be select.
        self.machine = utils.machlib.MODEL_LIST[i[0]]
        self.scaleWire.config(to=self.machine.get("capacity"))

    def wire_select(self):
        """ Set <wire> with the <scaleWire> value. """
        pass


class Add_slide(Tk):
    """ Add a slide in overlay.
        Create a widget to enter many information :
            - The type of the module
            - the support
            - the name
            - the accessory
            - the motor (according the type of the machine)
            - note
        """

    def __init__(self, machine):

        Tk.__init__(self)
        # The machine used in the current regulation.
        self.machine = machine
        # the support used.
        self.sup = StringVar()
        # if the machine can have additional motor, he go here.
        self.motor = StringVar()
        self.motor.set("None")
        # the scale of the spin support.
        self.spin_scale = StringVar()
        self.spin_scale.set("None")

        # the first frame of the widget, allows to select a tool or a
        # spinner, he configure the second frame by the choice.
        self.f1 = Frame(self)
        self.f1.grid(row=1, column=1, padx=70, pady=10)
        self.tool_b = Button(self.f1, text="Outil", \
                             command=self.tool, width=10)
        self.tool_b.grid(row=1, column=1, pady=10)
        self.spin_b = Button(self.f1, text="Tournette", \
                             command=self.spin, width=10)
        self.spin_b.grid(row=1, column=2, pady=10)
        # the second frame, allows to enter information about the slide added.
        self.f2 = Frame(self)
        self.f2.grid(row=2, column=1)
        # the last frame, quit and ok button.
        self.f3 = Frame(self)
        self.f3.grid(row=3, column=1)
        self.quit = Button(self.f3, text="Quitter", command=self.destroy)
        self.quit.grid(row=1, column=2, padx=10, pady=5)

        # by default the tool option are launch.
        self.tool()

    def tool(self):
        """ for add a tool. """

        self.tool_b.config(bg="LightBlue")
        self.spin_b.config(bg="LightGrey")

        self.f2.destroy()
        self.f2 = Frame(self)
        self.f2.grid(row=2, column=1)
        self.lf = LabelFrame(self.f2, text="Informations", \
                             width=120, height=100)
        self.lf.pack()

        # radioGroupfor selection of the support.
        sup_rg = Frame(self.lf)
        sup_rg.grid(row=0, column=1, padx=10, pady=15, columnspan=5)
        self.sta = Radiobutton(sup_rg, text="STA", indicatoron=0, \
                               variable=self.sup, value="STA", \
                               width=8, selectcolor="LightBlue")
        self.sta.grid(row=0, column=1, padx=10, pady=10)
        self.stu = Radiobutton(sup_rg, text="STU", indicatoron=0, \
                               variable=self.sup, value="STU", \
                               width=8, selectcolor="LightBlue")
        self.stu.grid(row=0, column=2, padx=10, pady=10)
        self.sc = Radiobutton(sup_rg, text="SC", indicatoron=0, \
                              variable=self.sup, value="SC", \
                              width=8, selectcolor="LightBlue")
        self.sc.grid(row=0, column=3, padx=10, pady=10)

        if self.machine in utils.machlib.CAM_MACHINE:
            self.stb = Radiobutton(sup_rg, text="STB", indicatoron=0, \
                                   variable=self.sup, value="STB", \
                                   width=8, selectcolor="LightBlue")
            self.stb.grid(row=0, column=4, padx=10, pady=10)

        Label(self.lf, text="Nom : ", width=10)\
        .grid(row=1, column=1, padx=10, pady=5)
        self.name_e = Entry(self.lf, width=20)
        self.name_e.grid(row=1, column=2, padx=10, pady=5, columnspan=3)

        Label(self.lf, text="Accesoire : ", width=10)\
        .grid(row=3, column=1, padx=10, pady=5)
        self.attachmnent_e = Entry(self.lf, width=20)
        self.attachmnent_e.grid(row=3, column=2, padx=10, \
                                pady=5, columnspan=3)

        if self.machine in utils.machlib.MOTOR_CAM_MACHINE:

            Label(self.lf, text="Moteur : ", width=10)\
            .grid(row=4, column=1, padx=10, pady=5)
            motor_rg = Frame(self.lf)
            motor_rg.grid(row=4, column=2, padx=10, pady=5, columnspan=3)
            self.x_motor = Radiobutton(motor_rg, text="X", variable=self.motor, \
                                       value="x", selectcolor="LightBlue", \
                                       indicatoron=0, width=4)
            self.x_motor.grid(row=0, column=1, padx=4, pady=5)

            self.y_motor = Radiobutton(motor_rg, text="Y", \
                                       variable=self.motor, value="y", \
                                       indicatoron=0, selectcolor="LightBlue", width=4)
            self.y_motor.grid(row=0, column=2, padx=4, pady=5)

        Label(self.lf, text="Note : ", width=10).grid(row=10, column=1, \
                                                      padx=10, pady=5)
        self.note = Entry(self.lf)
        self.note.grid(row=10, column=2, padx=10, pady=5, columnspan=3)

        self.next = Button(self.f3, text="Suivant", command=None)
        self.next.grid(row=1, column=1, padx=10, pady=5)

    def spin(self):
        """ for add a spinner. """

        self.spin_b.config(bg="LightBlue")
        self.tool_b.config(bg="LightGrey")

        self.f2.destroy()
        self.f2 = Frame(self)
        self.f2.grid(row=2, column=1)
        self.lf = LabelFrame(self.f2, text="Informations", width=120, \
                             height=100)
        self.lf.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
        # radiogroup for selection of the support.
        radiogroup = Frame(self.lf)
        radiogroup.grid(row=0, column=1, padx=10, pady=15, columnspan=5)
        self.sp = Radiobutton(radiogroup, text="SP", indicatoron=0, \
                               variable=self.sup, value="SP", \
                               width=8, selectcolor="LightBlue")
        self.sp.grid(row=0, column=1, padx=10, pady=10)
        # if the machine is a camme machine,
        # the SPS support is available.
        if self.machine in utils.machlib.CAM_MACHINE:
            self.sps = Radiobutton(radiogroup, text="SPS", indicatoron=0, \
                                   variable=self.sup, value="SPS", \
                                   width=8, selectcolor="LightBlue")
            self.sps.grid(row=0, column=2, padx=10, pady=10)
        else:
            pass
        # name of the spin. (entry)

        # motors used. (radiobutton)

        # scale for selection of the spin support scale.
        Label(self.lf, text="Echelle : ", \
              width=10).grid(row=3, column=1, padx=10, pady=5)
        self.scale_s = Spinbox(self.lf, from_=0, to=20, width=8,\
                                 increment=1, wrap=True, \
                                 command=None)
        self.scale_s.grid(row=3, column=2, padx=10, pady=5)

        Label(self.lf, text="Note : ", width=10).grid(row=10, column=1, \
                                                      padx=10, pady=5)
        self.note = Entry(self.lf)
        self.note.grid(row=10, column=2, padx=10, pady=5, columnspan=3)

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
