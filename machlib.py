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


class Slide(object):
    """ A slide in the machine layout. """

    def __init__(self, position):
        """ init of Slide.

            position -- the position of the slide in the layout """

        self.position = position
        # present -- boolean to now if the slide is actually monted
        # on the machine.
        self.present = True
        # have_spin -- boolean to now if the slide have actually a
        # spinner mounted.
        self.have_spin = False

    def move(self, new_position):
        """ Move the slide in the layout.

            new_position -- he new position """

        if not self.present:
            raise IllegalSlideMoveError
        else:
            self.position = new_position

    def remove(self):
        """ Remove the slide in the layout.
            the removing just set the position at None, the configuration are
            keeeped. """

        if not self.present:
            raise IllegalSlideMoveError
        else:
            self.position = None
            self.present = False

    def add(self, position):
        """ Add slide in the layout previously removed.

            position -- the new position """

        if self.present:
            raise IllegalSlideMoveError
        else:
            self.position = position
            self.present = True

    def mnt_spin(self, Spinner):
        """ Mount spinner in the slide.

            Spinner -- the spinner to add """

        if self.have_spin:
            raise IllegalSpinnerMoveError
        else:
            self.have_spin = True
            self.spinner = Spinner

    def umnt_spin(self):
        """ Umount the current spinner in the slide. """

        if not self.have_spin:
            raise IllegalSpinnerMoveError
        else:
            self.spinner = None
            self.have_spin = False


class CammeSlide(Slide):
    """ A slide controlled with a camme """

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

        Slide.__init__(position)
        # if a camme is find out. <cam_pos> and <cam_sup> are not
        # checked if not.
        if cam:
            self.cam = cam
            if cam_pos:
                self.cam_pos = cam_pos
            if cam_sup:
                self.cam_sup = cam_sup

    def __str__(self):

        if self.cam:
            return ('Position : {}\nCamme : {} at {} Deg.'
                    .format(self.position, self.cam, self.cam_pos))
        else:
            return ('Position : {}'.format(self.position))

class MotorSlide(Slide):
    """ A slide controlled by motor.
        According the type of the machine, motor slide are directly
        created and places. A motor can be fixed on layout or removable
        """

    def __init__(self, position, motor, fixed=None):
        """ init of MotorSlide.

            pos -- motor position (from 0 to 359)
            motor -- motor name
            fixed -- if the motor is fixed on layout """

        Slide.__init__(position)
        self.motor = motor
        # if is fixed (any value) he can't move or be remove
        self.fixed = fixed
        # if the slide is on the machine actually
        self.present = True

    def __str__(self):
        return ('Motor : {}\nPosition : {}\n'
                .format(self.motor, self.position))


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
    """ The machine dosen't have the capacity to produce this
        spring, the wire is too big. """
    pass


class IllegalSlideMoveError(MachlibError, AttributeError):
    """ the slide cannot be move in her actual configuration. """
    pass


class IllegalSlideMoveError(MachlibError, AttributeError):
    pass

class IllegalSpinnerMoveError(MachlibError, AttributeError):
    pass
