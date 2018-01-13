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
# text on interface
QUIT = "Quitter "
NEXT = "Suivant "
LB_COLOR = "DodgerBlue4"
REF_PROD = "Reference piece"
CUSTOMER = "Client"
DIAM = "Diametre"
EXT_DIAM = "Diametre exterieur"
NB = "Nombre de spire"
TOLERATION = "Tolerance +/-"
REF = "Reference"
NAME = "Nom"
RIGHT = "Droite"
LEFT = "Gauche"
STEEL = "Acier"
INOX = "Inox"
MATERIAL = "Matier"
ACCESSORY = "Accesoire"
NOTE = "Note"
MOTOR = "Motor"

from tkinter import *
import utils.machlib
import utils.sprlib
import utils.tklib


class LoadPage(Tk):
    """ Find and load programmes. """
    pass


class NewRegulationViewer(Tk):
    """ Create a new regulation viewer. """

    def __init__(self):
        Tk.__init__(self)
        self.title(NEW_REGULATION)
        self.sep = ("_" * 80)

        ## the variable of the class. ##
        self.id = StringVar()
        self.customer = StringVar()
        self.wire_ref = StringVar()
        self.diam_ext = DoubleVar()
        self.nb = DoubleVar()
        self.tol = DoubleVar()
        # the windows is diviser by frame, any frame have a function,
        # all functions are launch at the degining.
        self.identity()
        self.machine()
        self.wire()
        self.spring()

        self.quit_bton = Button(self, text=QUIT, command=self.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2, pady=5)
        self.next_bton = Button(self, text=NEXT)
        self.next_bton.grid(row=30, column=9, padx=2, pady=5)

    def identity(self):
        """ A frame for enter informations about the customer
            and the references.
            """

        # id entry, for self.id
        self.id_entry = utils.tklib.label_entry(self, REF_PROD, self.id, 0, width=20)
        # customer entry, for self.custommer
        self.customer_entry = utils.tklib.label_entry(self, CUSTOMER, self.customer, 0, width=20, column=3)

    def machine(self):
        """ A frame for selected the mac"hine,
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
        Label(self.fw, text=DIAM).grid(row=1, column=1, padx=10, pady=8)
        Label(self.fw, text="mm").grid(row=1, column=3)
        # Wire references
        self.wire_ref_entry = utils.tklib.label_entry(self.fw, REF, self.wire_ref, 2)

        self.material = StringVar()
        self.material.set("Acier")
        Label(self.fw, text=MATERIAL).grid(row=3, column=1, padx=10, pady=8)
        self.radiogroup_mat = Frame(self.fw)
        self.radiogroup_mat.grid(row=3, column=2)
        self.steel = Radiobutton(self.radiogroup_mat, text=STEEL, indicatoron=0, \
                                 variable=self.material, value="steel", \
                                 width=4, selectcolor=LB_COLOR)
        self.steel.grid(row=1, column=1)
        self.steel.deselect()
        self.inox = Radiobutton(self.radiogroup_mat, text=INOX, indicatoron=0, \
                                variable=self.material, value="inox", \
                                width=4, selectcolor=LB_COLOR)
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
        self.right = Radiobutton(self.radiogroup_dir, text=RIGHT, indicatoron=0, \
                                 variable=self.dir, value="right", \
                                 width=8, selectcolor=LB_COLOR)
        self.right.grid(row=1, column=2)
        self.right.deselect()
        self.left = Radiobutton(self.radiogroup_dir, text=LEFT, indicatoron=0, \
                                variable=self.dir, value="left", \
                                width=8, selectcolor=LB_COLOR)
        self.left.grid(row=1, column=3)
        self.left.deselect()

        # diameter entry, for self.diam_ext
        self.diam_entry = utils.tklib.label_entry(self.fs, EXT_DIAM, self.diam_ext, 2)
        Label(self.fs, text="mm").grid(row=2, column=3)

        # number of coils entry, for self.nb.
        self.nb_entry = utils.tklib.label_entry(self.fs, NB, self.nb, 3)
        Label(self.fs, text="spires").grid(row=3, column=3)

        # diameter toleration entry, for self.tol.
        self.diam_tol = utils.tklib.label_entry(self.fs, TOLERATION, self.tol, 4)
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
        self.listMachine.itemconfig(i[0], bg=LB_COLOR)
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
        self.spin_motor = StringVar()
        # the scale of the spin support.
        self.spin_scale = StringVar()
        self.spin_scale.set("None")
        self.tool_name = StringVar()
        self.accessory = StringVar()
        self.tool_note = StringVar()
        self.spin_name = StringVar()
        self.spin_note = StringVar()
        self.linear_motor = StringVar()
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
        self.quit = Button(self.f3, text=QUIT, command=self.destroy)
        self.quit.grid(row=1, column=2, padx=10, pady=5)

        # by default the tool option are launch.
        self.tool()

    def tool(self):
        """ for add a tool. """

        self.tool_b.config(bg=LB_COLOR)
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

        self.sta_button = utils.tklib.radiobutton(sup_rg, "STA", self.sup, "STA", indicatoron=0, column=1, color=LB_COLOR)
        self.stu_button = utils.tklib.radiobutton(sup_rg, "STU", self.sup, "STU", indicatoron=0, column=2, color=LB_COLOR)
        self.sc_button = utils.tklib.radiobutton(sup_rg, "SC", self.sup, "SC", indicatoron=0, column=3, color=LB_COLOR)

        if self.machine in utils.machlib.CAM_MACHINE:
            self.stb_button = utils.tklib.radiobutton(sup_rg, "STB", self.sup, "STB", indicatoron=0, column=4, color=LB_COLOR)

        self.tool_name_entry = utils.tklib.label_entry(self.lf, NAME, self.tool_name, 1, 20)

        self.accessory_entry = utils.tklib.label_entry(self.lf, ACCESSORY, self.accessory, 2, 20)

        # if the machine have a linear motor
        if self.machine in utils.machlib.MOTOR_CAM_MACHINE:

            Label(self.lf, text=MOTOR, width=10).grid(row=5, column=1, padx=10, pady=5)
            lmotor = Frame(self.lf)
            lmotor.grid(row=5, column=2, padx=10, pady=5, columnspan=3)

            self.motor_x_button = utils.tklib.radiobutton(lmotor, "X", self.linear_motor, "X", indicatoron=0, column=1, color=LB_COLOR, width=5)
            self.motor_y_button = utils.tklib.radiobutton(lmotor, "Y", self.linear_motor, "Y", indicatoron=0, column=2, color=LB_COLOR, width=5)
            self.not_motor_button = utils.tklib.radiobutton(lmotor, " ", self.linear_motor, False, indicatoron=0, column=3, color=LB_COLOR, width=5)

        self.tool_note_entry = utils.tklib.label_entry(self.lf, NOTE, self.tool_note, 10, 20)

        self.next = Button(self.f3, text="Ok", command=None)
        self.next.grid(row=1, column=1, padx=10, pady=5)

    def spin(self):
        """ for add a spinner. """

        self.spin_b.config(bg=LB_COLOR)
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

        self.sp_button = utils.tklib.radiobutton(radiogroup, "SP", self.sup, "SP", indicatoron=0, column=1, color=LB_COLOR)

        if self.machine in utils.machlib.CAM_MACHINE:
            self.sps_button = utils.tklib.radiobutton(radiogroup, "SPS", self.sup, "SPS", indicatoron=0, column=2, color=LB_COLOR)

        # name of the spin.
        self.spin_name_entry = utils.tklib.label_entry(self.lf, NAME, self.spin_name, 1, 20)

        # motors used.
        Label(self.lf, text="Moteur : ", width=10)\
        .grid(row=2, column=1, padx=10, pady=5)
        motor_rg = Frame(self.lf)
        motor_rg.grid(row=2, column=2, padx=10, pady=5, columnspan=3)

        self.spin_motor1_button = utils.tklib.radiobutton(motor_rg, "P", self.spin_motor, "P", indicatoron=0, column=1, color=LB_COLOR, width=5)
        self.spin_motor2_button = utils.tklib.radiobutton(motor_rg, "Q", self.spin_motor, "Q", indicatoron=0, column=2, color=LB_COLOR, width=5)
        self.spin_motor0_button = utils.tklib.radiobutton(motor_rg, " ", self.spin_motor, False, indicatoron=0, column=3, color=LB_COLOR, width=5)

        # if the machine is a MCS15-G, the spinner motor
        # have a different name.
        if self.machine is utils.machlib.MCS15G.get("name"):
            self.spin_motor1_button.config(text="Y", value="Y")
            self.spin_motor2_button.config(text="X", value="X")
        else:
            pass

        # scale for selection of the spin support scale.
        Label(self.lf, text="Echelle : ", \
              width=10).grid(row=3, column=1, padx=10, pady=5)
        self.scale_s = Spinbox(self.lf, from_=0, to=20, width=8,\
                                 increment=1, wrap=True, \
                                 command=None)
        self.scale_s.grid(row=3, column=2, padx=10, pady=5, columnspan=3)

        self.spin_note_entry = utils.tklib.label_entry(self.lf, NOTE, self.spin_note, 10, 20)


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
