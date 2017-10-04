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
MS20 = {"name": "MS20", "capacity": 2.0}
MCS15G = {"name": "MCS15G", "capacity" : 1.5)
SX15 = {"name": "SX15", "capacity": 1.5}
MX10 = {"name": "MX10", "capacity": 1.0)

# Listing of model available.
# Stocked on a tuple, because she do not need to be modify.
MODEL = (MX20, MCS20, AX20, MS20, MCS15G, SX15, MX10)

# Support
STA = "STA"
STB = "STB"
STU = "STU"
SP = "SP"
SPS = "SPS"
ST = "ST"
STS = "STS"

# table of support available.
# Stocked on a tabe because the support are not available
# for all machine.
SUPPORT = [STA, STB, STU, SP, SPS, ST, STS]

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

__all__ = ["check_capacity"]


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

    return if model.get("capacity") >= wire


class CammeSlide(Slide):
    """ A slide with camme """

    def __init__(self, position, cam=None, cam_pos=None, cam_sup=None):

        self.position = position
        if cam:
            self.cam = cam
            if cam_pos:
                self.cam_pos = cam_pos
            if cam_sup:
                self.cam_sup = cam_sup

    def add_cam(self, cam, cam_pos, cam_sup):
        """ Adding a camme. """

        self.cam = cam
        self.cam_pos = cam_pos
        self.cam_sup = cam_sup

    def __str__(self):
        pass

class MotorSlide(Slide):
    """ A slide with motor """

    def __init__(self, position, motor=None):

        self.position = position


class Camme(object):
    pass


class Motor(object):
    pass


class FixedMotor(Motor):
    pass


class AdditionalMotor(Motor):
    pass


class SpinnerMotor(Motor):
    pass


class Support(object):
    pass


class Tool(object):
    pass


class Spinner(Tool):
    pass

# Error Class
class MachineCapacityError():
    """ Error class call if the machine don't have the capacity to
        produce the spring because the wire is too big. """

    pass
