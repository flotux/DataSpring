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
    """ A slide in the machine layout.

        Members :

        - position -- position of the slide in the machine layout.
        - module -- module mounted in the slide.
        - element -- tool mounted in the slide.

        A slide can be <MotorSlide> or <CammeSlide>. """

    def __init__(self, position):

        self.position = position
        self.module = None
        self.element = None
        self.descript = None

    def get_position(self):

        return self.position

    def set_module(self, m):

        self.module = m

    def get_module(self):

        return self.module

    def del_module(self):

        self.module = None

    def set_element(self, e):

        self.element = e

    def get_element(self):

        return self.element

    def set_descript(self, msg):

        self.descript = msg

    def get_descript(self):

        return self.descript

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

            position -- position of the motor in the machine
            cam -- camme used
            cam_pos -- camme position
            cam_sup -- support camme used """

        Slide.__init__(self, position)
        self.cam, self.cam_pos, self.cam_sup = cam, cam_pos, cam_sup

    def set_position(self, p):

        self.position = p

    def del_position(self):

        self.position = None

    def add_cam(self, cam, cam_pos, cam_sup):
        """ Add a camme on slide.

            cam -- camme used
            cam_pos -- position of the camme
            cam_sup -- support camme used """

        self.cam, self.cam_pos, self.cam_sup = cam, cam_pos, cam_sup

    def del_cam(self):

        self.cam, self.cam_pos, self.cam_sup = None, None, None

    def set_cam_pos(self, p):

        self.cam_pos = p

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

    def __init__(self, position):
        """
            position -- motor position (from 0 to 359) """

        Slide.__init__(self, position)

    def __str__(self):

        return "Motor Slide.\n\
                Position : {}\n\
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

    def __init__(self, place):
        """
            place -- the placement of the rack (CammeSlide|MotorSlide) """

        self.position = position


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
