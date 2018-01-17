
from tkinter import *
import utils.machlib
import utils.sprlib
import utils.tklib

class Add_slide(object):
    """ Add a slide in overlay.
        Create a widget to enter many information :
            - The type of the module
            - the support
            - the name
            - the accessory
            - the motor (according the type of the machine)
            - note
        """

    def __init__(self, master, machine):

        self.master = master
        # The machine used.
        self.machine = machine

        #==== The variables used in the class. ===========================
        self.type_add = "tool"
        self.sup = StringVar()
        self.spin_motor = StringVar()
        self.spin_scale = StringVar()
        self.spin_scale.set("None")
        self.tool_name = StringVar()
        self.tool_name.set("tool name")
        self.accessory = StringVar()
        self.tool_note = StringVar()
        self.spin_name = StringVar()
        self.spin_note = StringVar()
        self.linear_motor = StringVar()
        self.motor_used = IntVar()
        #=================================================================

        # 1. frame : selected tool or spinner. ===========================
        self.f1 = Frame(self.master)
        self.f1.grid(row=1, column=1, padx=70, pady=10)
        self.tool_b = Button(self.f1, text="Outil", \
                             command=self.tool, width=10)
        self.tool_b.grid(row=1, column=1, pady=10)
        self.spin_b = Button(self.f1, text="Tournette", \
                             command=self.spin, width=10)
        self.spin_b.grid(row=1, column=2, pady=10)
        #=================================================================

        # 2. frame : informations entry ==================================
        self.f2 = Frame(self.master)
        self.f2.grid(row=2, column=1)
        #=================================================================

        # 3. frame : quit and ok button. =================================
        self.f3 = Frame(self.master)
        self.f3.grid(row=3, column=1)
        self.quit = Button(self.f3, text="Quitter", command=self.master.destroy)
        self.quit.grid(row=1, column=2, padx=10, pady=5)
        self.next = Button(self.f3, text="Ok", command=self.button_ok_pressed)
        self.next.grid(row=1, column=1, padx=10, pady=5)
        #=================================================================

        # by default the tool option are launch.
        self.tool()

    def tool(self):
        """ for add a tool. """

        self.type_add = "tool"
        self.f2.destroy()
        self.f2 = Frame(self.master)
        self.f2.grid(row=2, column=1)
        self.lf = LabelFrame(self.f2, text="Informations", \
                             width=120, height=100)
        self.lf.pack()

        # radioGroupfor selection of the support.
        sup_rg = Frame(self.lf)
        sup_rg.grid(row=0, column=1, padx=10, pady=15, columnspan=5)

        self.sta_button = utils.tklib.radiobutton(sup_rg, "STA", self.sup, \
                                                  "STA", indicatoron=0, column=1)
        self.stu_button = utils.tklib.radiobutton(sup_rg, "STU", self.sup, \
                                                  "STU", indicatoron=0, column=2)
        self.sc_button = utils.tklib.radiobutton(sup_rg, "SC", self.sup, \
                                                 "SC", indicatoron=0, column=3)

        if self.machine in utils.machlib.CAM_MACHINE:
            self.stb_button = utils.tklib.radiobutton(sup_rg, "STB", self.sup, \
                                                      "STB", indicatoron=0, column=4)

        self.tool_name_entry = utils.tklib.label_entry(self.lf, "Nom", self.tool_name, 1, 20)

        self.accessory_entry = utils.tklib.label_entry(self.lf, "Accesoire", self.accessory, 2, 20)

        # if the machine have a linear motor
        if self.machine in utils.machlib.MOTOR_CAM_MACHINE:


            Label(self.lf, text="Moteur :", width=10).grid(row=5, column=1, padx=10, pady=5)

            self.linear_motor_frame = Frame(self.lf)
            self.linear_motor_frame.grid(row=5, column=2, padx=10, pady=5, columnspan=3)

            self.motor_used_button = Checkbutton(self.linear_motor_frame, \
                                                 variable=self.motor_used, \
                                                 command=self.motor_check, \
                                                 onvalue=1, offvalue=0)
            self.motor_used_button.grid(row=1, column=0)

            self.motor_x_button = utils.tklib.radiobutton(self.linear_motor_frame, \
                                                          "X", self.linear_motor, \
                                                          "X", indicatoron=0, column=1, width=5)
            self.motor_x_button.config(state="disabled")
            self.motor_y_button = utils.tklib.radiobutton(self.linear_motor_frame, \
                                                          "Y", self.linear_motor, \
                                                          "Y", indicatoron=0, column=2, width=5)
            self.motor_y_button.config(state="disabled")

        self.tool_note_entry = utils.tklib.label_entry(self.lf, "Note", self.tool_note, 10, 20)



    def spin(self):
        """ for add a spinner. """

        self.type_add = "spinner"
        self.f2.destroy()
        self.f2 = Frame(self.master)
        self.f2.grid(row=2, column=1)
        self.lf = LabelFrame(self.f2, text="Informations", width=120, \
                             height=100)
        self.lf.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
        # radiogroup for selection of the support.
        radiogroup = Frame(self.lf)
        radiogroup.grid(row=0, column=1, padx=10, pady=15, columnspan=5)

        self.sp_button = utils.tklib.radiobutton(radiogroup, "SP", self.sup, "SP", indicatoron=0, column=1)

        if self.machine in utils.machlib.CAM_MACHINE:
            self.sps_button = utils.tklib.radiobutton(radiogroup, "SPS", self.sup, "SPS", indicatoron=0, column=2)

        # name of the spin.
        self.spin_name_entry = utils.tklib.label_entry(self.lf, "Nom", self.spin_name, 1, 20)

        # motors used.
        Label(self.lf, text="Moteur : ", width=10)\
        .grid(row=2, column=1, padx=10, pady=5)
        motor_rg = Frame(self.lf)
        motor_rg.grid(row=2, column=2, padx=10, pady=5, columnspan=3)

        self.spin_motor1_button = utils.tklib.radiobutton(motor_rg, "P", self.spin_motor, \
                                                          "P", indicatoron=0, column=1, width=5)
        self.spin_motor2_button = utils.tklib.radiobutton(motor_rg, "Q", self.spin_motor, \
                                                          "Q", indicatoron=0, column=2, width=5)

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

        self.spin_note_entry = utils.tklib.label_entry(self.lf, "note", self.spin_note, 10, 20)


    def motor_check(self):
        """ called when the checkbutton motor_user is clicked.
            """


        print (self.motor_used.get())
        if self.motor_used.get():
            self.motor_x_button.config(state="normal")
            self.motor_y_button.config(state="normal")
        else :
            self.motor_x_button.config(state="disabled")
            self.motor_x_button.config(state="disabled")
            self.linear_motor.set("None")

        self.motor_used_button.update()

    def button_ok_pressed(self):
        """ Start when the button ok is pressed. """

        self.tool_name_entry.bind()
        the_name = self.tool_name_entry.get()
        print(the_name)
        if self.type_add is "tool":
            print("tool")
            name = self.tool_name.get()
            print(name)
        else:
            print(self.sup.get(),\
                self.spin_motor.get(),\
                self.spin_scale.get(),\
                self.spin_name.get(),\
                self.spin_note.get())
