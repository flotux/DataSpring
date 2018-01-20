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
FULL_MOTOR_MACHINE = (MX20.get("name"), MX10.get("name"))
CAM_MACHINE = (MCS20.get("name"), AX20.get("name"), \
               MCS15G.get("name"), SX15.get("name"))
MOTOR_CAM_MACHINE = (MCS20.get("name"), AX20.get("name"))

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
# Stocked on a tabe because all the supports
# are not compatible on all machines
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
        self.tool = None
        self.descript = None

    def get_position(self):

        return self.position

    def set_module(self, m):

        self.module = m

    def get_module(self):

        return self.module

    def del_module(self):

        self.module = None

    def set_tool(self, t):

        self.tool = t

    def get_tool(self):

        return self.tool

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
            According to the type of machine, a cammes slides are directly
            created and place without cammes, exepted the cut slide, whish as
            camme, camme angle and camme support by default.
            finally , the informations about camme are optional, she can be
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

    def get_cam(self):

        return self.cam

    def set_cam(self, c):

        self.cam = c

    def del_cam(self):

        self.cam, self.cam_pos, self.cam_sup = None, None, None

    def set_cam_pos(self, p):

        self.cam_pos = p

    def get_cam_pos(self):

        return self.cam_pos

    def set_cam_sup(self, s):

        self.cam_sup = s

    def get_cam_sup(self):

        return self.cam_sup

    def __str__(self):

        if self.cam_pos:
            return ('Position : {}\nCamme : {} at {} Deg.'
                    .format(self.position, self.cam, self.cam_pos))
        else:
            return ('Position : {}'.format(self.position))


class MotorSlide(Slide):
    """ A slide controlled by a motor.
        According the type of the machine, motor slide can be directly
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
                .format(self.position, self.module)


class RotaryMotor(object):
    """ A rotary motor module provided that position a spinner tool.
        her name is her axes. It's a empty class """

    def __init__(self, scale=None):

        self.scale = scale

    def set_scale(self, s):

        self.scale = s

    def get_scale(self):

        return self.scale


class Support(object):
    """ A support module provided that position a tool.
        her name is her reference. It's a empty class """

    def __init__(self, name):

        self.name = name


class Rack(object):
    """ A rack, used on MX10,
        he must be place on a MotorSlide"""

    def __init__(self, place):
        """
            place -- the placement of the rack (CammeSlide|MotorSlide) """

        self.position = position


class Tools(object):
    """ A abstract class for inscantiation of tools. """

    def __init__(self, name):

        self.name = name


class Tool(Tools):
    """ A tool on the machine. """

    def __init__(self, name):
        """
            name -- the name of the tool """

        Tools.__init__(self, name)


class Spin(Tools):
    """ A spin mounted in a rotary  motor. """

    def __init__(self, name):
        """
            name -- the name of the spin """

        Tools.__init__(self, name)
