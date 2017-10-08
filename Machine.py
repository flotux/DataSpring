#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" Machine

    TODO
    """

import machlib
from machlib import MotorSlide, CammeSlide, SpinnerMotor, Rack
from sprlib import LEFT, RIGHT

class Machine(object):
    """ Represent a machine """

    def __init__(self, sens=RIGHT):
        """
            sens -- the winding direction of the spring to produce
            """
        self.model = str()
        self.capacity = float()
        self.clamp = bool()
        self.cam = (bool)
        self.sens = sens
        # the layout of the machine, all of the place are initialized as None,
        # execpt the cut slide.
        # when a slide is renseigned, he is add to the layout dictionnary.
        #self.layout = {'0': None, '45': None, '90':None, '135': None,
        #               '180': None, '225': None, '270': None, '315': None}
        # the entry of the machine.
        self.entry = {'A1': None, 'A2', None, 'A3':None, 'A4': None,
                      'A5': None, 'A6': None, 'A7': None, 'A8': None}
        # the sensors on machine.
        self.sensors = {'M0': None, 'M1': None}


class Mx(Machine):
    """ A MX-- machine. """

    def __init__(self, sens=RIGHT):

        Machine.__init__(self, sens)
        # Initialisation of the MX layout
        self.S = MotorSlide(0, True)
        self.T = MotorSlide(45, True)
        self.U = MotorSlide(90, True)
        self.V = MotorSlide(135, True)
        self.W = MotorSlide(180, True)
        self.X = MotorSlide(225, True)
        self.Y = MotorSlide(270, True)
        self.Z = MotorSlide(315, True)
        # Spinner motors
        self.P = SpinnerMotor()
        self.Q = SpinnerMotor()


class Mx20(Mx):
    """ A MX20 machine """

    def __init__(self, sens=RIGHT):

        Mx.__init__(self, sens)
        self.capacity = 2.0


class Mx10(Mx):
    """ A MX10 machine """

    def __init__(self, sens=RIGHT):

        Mx.__init__(self, sens)
        self.capacity = 1.0
        self.rack0 = Rack(self.S, True)
