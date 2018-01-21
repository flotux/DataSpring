
#========== TEMPORARY ==========================================================
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


#==== Imports ==================================================================
from tkinter import *
#=======================#
import controller.machlib
import controller.sprlib
from controller.form_check import empty, format_float, valide, highlight
#=======================#
from view import tklib
#===============================================================================

class NewRegulation(object):
    """ Create a new regulation viewer. """

    def __init__(self, master):

        self.master = master
        self.master.title(NEW_REGULATION)
        self.sep = ("_" * 80)

        ## the variables of the class. ##
        self.id = StringVar()           # the reference
        self.customer = StringVar()     # the customer
        self.machine = StringVar()      # the machine used
        self.machine_ok = False         # if a machine is selected
        self.wire = DoubleVar()         # the wire diameter
        self.wire_ref = StringVar()     # the wire reference
        self.dir = StringVar()          # the winding direction
        self.diam = StringVar()     # the ext. diameter
        self.nb = StringVar()           # the number of coils
        self.tol = StringVar()          # the diameter toleration

        # the windows is diviser by frame, several frame have a function,
        # all functions are launch at the degining.
        self.identity_form()
        self.machine_form()
        self.wire_form()
        self.spring_form()

        self.quit_bton = Button(self.master, text=QUIT, command=self.master.destroy)
        self.quit_bton.grid(row=30, column=10, padx=2, pady=5)
        self.next_bton = Button(self.master, text=NEXT, command=self.validation)
        self.next_bton.bind('<Return>',self.__repr__)

        self.next_bton.grid(row=30, column=9, padx=2, pady=5)

    def identity_form(self):
        """ A frame for enter informations about the customer
            and the references.
            """

        # id entry, for self.id
        self.id_entry = tklib.label_entry(self.master, REF_PROD, self.id, 0, width=20)
        # customer entry, for self.custommer
        self.customer_entry = tklib.label_entry(self.master, CUSTOMER, self.customer, 0, width=20, column=3)

    def machine_form(self):
        """ A frame for selected the machine,
            according the MODEL_list in utils/machlib.
            """

        self.fm = LabelFrame(self.master, text=MACHINE_SELECTOR_LABEL)
        self.fm.grid(row=1, column=1, pady=20, padx=10, columnspan=2)
        # Machine selection listBox
        self.list_machine = Listbox(self.fm, height=7, width=16)
        for ind, elt in enumerate(controller.machlib.MODEL_LIST):
            self.list_machine.insert(ind, elt.get("name"))
        # launch the machine_select function when a machine is select.
        self.list_machine.bind('<ButtonRelease-1>',self.machine_selected)
        self.list_machine.bind('<Return>',self.machine_selected)
        self.list_machine.pack(padx=10, pady=5)

    def wire_form(self):
        """ A frame for enter the diameter, references and
            type material of the wire.
            """

        self.fw = LabelFrame(self.master, text=WIRE_DIAMETER_LABEL)
        self.fw.grid(row=1, column=3, pady=20, padx=10, columnspan=2)

        self.wire.set(0.4)
        self.scaleWire = Spinbox(self.fw, from_=0.4, to=2.0, width=8,\
                                 increment=0.1, wrap=True, \
                                 command=self.wire_selected)
        self.scaleWire.grid(row=1, column=2)
        Label(self.fw, text=DIAM).grid(row=1, column=1, padx=10, pady=8)
        Label(self.fw, text="mm").grid(row=1, column=3)
        # Wire references
        self.wire_ref_entry = tklib.label_entry(self.fw, REF, self.wire_ref, 2)

        self.material = StringVar()
        self.material.set("None")
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

    def spring_form(self):
        """ A frame for enter information about the spring.
            """

        Label(self.master, text=self.sep).grid(row=2, padx=2, pady=10, columnspan=10)

        self.fs = Frame(self.master)
        self.fs.grid(row=3, column=0, pady=20, padx=10, columnspan=4)

        self.dir.set("None")

        # sens of winding, for self.dir
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

        # diameter entry, for self.diam
        self.diam_entry = tklib.label_entry(self.fs, EXT_DIAM, self.diam, 2)
        Label(self.fs, text="mm").grid(row=2, column=3)

        # number of coils entry, for self.nb.
        self.nb_entry = tklib.label_entry(self.fs, NB, self.nb, 3)
        Label(self.fs, text="spires").grid(row=3, column=3)

        # diameter toleration entry, for self.tol.
        self.diam_tol = tklib.label_entry(self.fs, TOLERATION, self.tol, 4)
        Label(self.fs, text="mm").grid(row=4, column=3)

    def machine_selected(self, *evt):
        """ executed when a machine is selected.
            change the maximum size of the wire according The
            machine selected.
            """
        # this block set all element in the listbox in white background,
        # for more lisibiliter.
        ind = 0
        while ind < self.list_machine.size():
            self.list_machine.itemconfig(ind, bg="White")
            ind += 1
        self.list_machine.config(background="White")

        # set the current selection in LightBlue background.
        i=self.list_machine.curselection()
        self.list_machine.itemconfig(i[0], bg=LB_COLOR, \
                                     selectbackground=LB_COLOR)

        # set the machine variable and
        # according the capacity of the machine selected, change the wire
        # maximum size can be select.
        self.machine = controller.machlib.MODEL_LIST[i[0]]
        self.scaleWire.config(to=self.machine.get("capacity"))
        self.machine_ok = True

        # if the wire selected is too big for the machine, he is change
        # too the machine capacity (like in the screen)
        if self.wire.get() > self.machine.get("capacity"):
            self.wire.set(self.machine.get("capacity"))

    def wire_selected(self, *evt):
        """ Set self.wire with the scaleWire value. """

        self.wire.set(self.scaleWire.get())

    def validation(self):
        """ validate each values.

            """

        if not valide(self.diam.get()):
            highlight(self.diam_entry)


    def next(self):
        """ TODO """
        pass

    def show(self):
        print (self.id.get(), self.customer.get(),\
               self.machine.get("name"), self.wire.get(),\
               self.wire_ref.get(), self.material.get())
        print(self.diam.get(), type(self.diam.get()), self.dir.get())
