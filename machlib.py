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
MCS15G = {"name": "MCS15G", "capacity": 1.5}
SX15 = {"name": "SX15", "capacity": 1.5}
MX10 = {"name": "MX10", "capacity": 1.0}

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

    return model.get("capacity") >= wire


class CammeSlide(object):
    """ A slide with camme """

    def __init__(self, position, cam=None, cam_pos=None, cam_sup=None):
        """ init of cammeSlide.
            According to the type of machine, cammes slides are directly
            created and place without cammes, exepted the cut slide, whish as
            camme, camme angle and camme support by default.
            to over, the informations about camme are optional, she can be
            decide later.

            position -- the position of the motor in the machine
            cam -OPTINAL- camme used
            cam_pos -OPTINAL- position of the camme
            cam_sup -OPTINAL- support camme used """

        self.position = position
        # if a camme is find out. <cam_pos> and <cam_sup> are not
        # checked if not.
        if cam:
            self.cam = cam
            if cam_pos:
                self.cam_pos = cam_pos
            if cam_sup:
                self.cam_sup = cam_sup

    def place_cam(self, cam, cam_pos, cam_sup):
        """ placing a camme. """

        self.cam = cam
        self.cam_pos = cam_pos
        self.cam_sup = cam_sup

    def __str__(self):
        pass


class MotorSlide(object):
    """ A slide controlled by motor.
        According the type of the machine, motor slide are directly
        created and places. A motor can be fixed on layout or removable
        """

    def __init__(self, position, motor, fixed=None):
        """ init of MotorSlide.

            pos -- motor position
            motor -- motor name
            fixed -- if the motor is fixed on layout """

        self.position = position
        self.motor = motor
        # if is fixed (any value) he can't move or be remove
        self.fixed = fixed
        # if the motor is on the machine actually
        self.present = True

    def move(self, new_position):
        """ Moving motor position.
            According the type of the machine, any motors cannot be move.

        motor -- the motor would be move
        pos -- new position in layout """

        if self.fixed:
            raise IllegalMotorMoveError
        if not self.present:
            raise IllegalMotorMoveError
        else:
            self.position = new_position


    def remove(self):
        """ Removing motor on layout. """

        if self.fixed:
            raise IllegalMotorMoveError
        elif not self.present:
            raise IllegalMotorMoveError
        else:
            self.position = None
            self.present = False

    def add(self, position):
        """ add motor on layout.
            If the motor a ben remove.

            position -- motor new position """

        if self.present:
            raise IllegalMotorMoveError
        elif self.fixed:
            raise IllegalMotorMoveError
        else:
            self.position = position

    def __str__(self):
        return ('Motor : {}\n',
                'Position : {}\n')


class Camme(object):
    pass


class Support(object):
    pass


class Tool(object):
    pass


class Spinner(Tool):
    pass


# Error Class
class MachlibError(Exception):
    pass

class MachineCapacityError(MachlibError, OverflowError):
    pass

class IllegalMotorMoveError(MachlibError, AttributeError):
    pass
