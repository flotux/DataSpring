#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" machlib

    A library for machine construction
    """

# Machine model.
#   name -- her name
#   capacity -- her capacity
MX20 = {"name": "MX20", "capacity": 2.0}
MCS20 = {"name": "MCS20", "capacity": 2.0}
AX20 = {"name": "AX20", "capacity": 2.0}
MCS15G = {"name": "MCS15G", "capacity": 1.5}
SX15 = {"name": "SX15", "capacity": 1.5}
MX10 = {"name": "MX10", "capacity": 1.0}

# Listing of model available.
# Stocked on a tuple, because she do not need to be modify.
MODEL_LIST = (MX20, MCS20, AX20, MCS15G, SX15, MX10)

# Support
STA = "STA"
STB = "STB"
STU = "STU"
SP = "SP"
SPS = "SPS"
ST = "ST"
STS = "STS"
SC = "SC"

# table of support available.
# Stocked on a tabe because the support are not available
# for all machine.
SUPPORT_LIST = [STA, STB, STU, SP, SPS, ST, STS, SC]

# Cammes
CD1 = "CD1"
CFD1 = "CFD1"
CD2 = "CD2"
CFD2 = "CFD2"
CD62 = "CD62"
CE2 = "CE2"
CCD13 = "CCD13"
CH38 = "CH38"

# Cammes tools
SB = "SB"
HRU = "HRU"
CAMME_TOOLS_LIST = (SB, HRU)

# Elements
SPINNER_MOTOR = 'SPINNER_MOTOR'
SUPPORT = 'SUPPORT'
ELEMENTS_LIST = (SPINNER_MOTOR, SUPPORT)

def check_capacity(model, wire):
    """ Check if the machine have the capacity too
        produce the spring.

        model -- dict of the machine
        wire --  wire diameter

        return
            True -- the a machine have the capacity too produce
                    with this wire diameter
            False -- she can't
            """

    return model.get("capacity") >= wire


class Slide(object):
    """ A slide in the machine layout. """

    def __init__(self, position, fixed=False):
        """
            position -- the position of the slide in the layout """

        self.position = position
        # present -- if the slide is actually monted on the machine.
        self.present = True
        self.module_mounted = False
        # module can have a --'SUPPORT' or 'SPINNER'--
        # else he have None
        self.module = None
        # It's possible to describe the utility of a slide.
        self.descript = None

    def move(self, new_position):
        """ Move the slide in the layout.

            new_position -- he new position """

        if not self.fixed:
            self.position = new_position

    def remove(self):
        """ Remove the slide in the layout.
            the removing just set the position at None, the configuration are
            keeeped. """

        if not self.fixed:
            self.position = None
            self.present = False

    def add(self, position):
        """ Add slide in the layout previously removed.

            position -- the new position """

        if not self.present:
            self.position = position
            self.present = True

    def add_module(self, Module):
        """ Add a element on Slide.

            Element -- the element (Spinner | Support) """

        self.module = Module
        self.module_mounted = True

    def rm_module(self):
        """ remove element on slide. """

        self.module = None
        self.module_mounted = False

    def descript(self, mess):
        """ Add a desciption of the slide utility in the actualy production.

            mess -- A desciption of the slide utility """

        self.descript = mess

    def __str__(self):
        pass


class CammeSlide(Slide):
    """ A slide controlled with a camme """

    def __init__(self, position, cam=None, cam_pos=None, cam_sup=None):
        """
            According to the type of machine, cammes slides are directly
            created and place without cammes, exepted the cut slide, whish as
            camme, camme angle and camme support by default.
            to over, the informations about camme are optional, she can be
            decide later.

            position -- the position of the motor in the machine
            cam -OPTINAL- camme used
            cam_pos -OPTINAL- position of the camme
            cam_sup -OPTINAL- support camme used """

        Slide.__init__(self, position)
        # if a camme is find out. <cam_pos> and <cam_sup> are not
        # checked if not.
        if cam:
            self.cam = cam
            if not cam_pos:
                raise IllegalCammeSetError
            self.cam_pos = cam_pos
            if not cam_sup:
                raise IllegalCammeSetError
            self.cam_sup = cam_sup
            self.have_cam = True
        else:
            self.cam, self.cam_pos, self.cam_sup = None, None, None
            self.have_cam = False

    def add_cam(self, cam, cam_pos, cam_sup):
        """ Add a camme on slide.

            cam -- camme used
            cam_pos -- position of the camme
            cam_sup -- support camme used """

        self.cam, self.cam_pos, self.cam_sup = cam, cam_pos, cam_sup

    def rm_cam(self):
        """ Remove cam from slide. """

        self.cam, self.cam_pos, self.cam_sup = None, None, None

    def move_cam(self, new_position):
        """ move cam position.

            new_position -- the new position of the cam """

        self.cam_pos = new_position

    def __str__(self):

        if self.cam_pos:
            return ('Position : {}\nCamme : {} at {} Deg.'
                    .format(self.position, self.cam, self.cam_pos))
        else:
            return ('Position : {}'.format(self.position))


class MotorSlide(Slide):
    """ A slide controlled by motor.
        According the type of the machine, motor slide are directly
        created and places. A motor can be fixed on layout or removable
        """

    def __init__(self, position, fixed=False):
        """
            pos -- motor position (from 0 to 359)
            fixed -- if the motor is fixed on layout """

        Slide.__init__(self, position)
        # if he is fixed
        self.fixed = fixed
        # if the slide is on the machine actually
        self.present = True

    def __str__(self):

        return "Motor Slide.\n\
                Position : {}\n\
                Fixed : {}\n\
                Present : {}\n\
                Module : {}\n"\
                .format(self.position, self.fixed, self.present, self.module.name)


class RotaryMotor(object):
    """ A rotary motor modulee provided that position a spinner tool.
        her name is her axes. It's a empty class """

    def __init__(self):
        pass


class Support(object):
    """ A support modulee provided that position a tool.
        her name is her reference. It's a empty class """

    def __init__(self):
        pass


class Rack(object):
    """ A rack, used on MX10,
        he must be place on a MotorSlide"""

    def __init__(self, place, fixed=False):
        """
            place -- the placement of the rack (CammeSlide|MotorSlide) """

        self.place = place
        self.fixed = fixed


class Tool(object):
    """ A tool on the machine. """

    def __init__(self, name):
        """
            name -- the name of the tool """

        self.name = name

class Spinner(Tool):
    """ A spinner mounted in a spinner motor. """

    def __init__(self, name):
        """
            name -- the name of the spinner """

        Tool.__init__(self, name)

# Error Class
class MachlibError(Exception):
    pass


class MachineCapacityError(MachlibError, OverflowError):
    """ The machine dosen't have the capacity to produce this
        spring, the wire is too big. """
    pass


class IllegalSlideMoveError(MachlibError, AttributeError):
    """ the slide cannot be move in her actual configuration. """
    pass


class IllegalElementAddError(MachlibError, AttributeError):
    """ The element cannot be add. """
    pass


class IllegalElementRemoveError(MachlibError, AttributeError):
    """ The element cannot be remove. """
    pass


class IllegalCammeSetError(MachlibError, AttributeError):
    pass
