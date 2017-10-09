#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" Machine

    TODO

    Just limited at the MX's machine for the moment.
    """

from machlib import *
from sprlib import LEFT, RIGHT

class Machine(object):
    """ Represent a machine """

    def __init__(self, wire, sens=RIGHT):
        """
            wire -- the wire diameter of the spring to produce
            sens -- the winding direction of the spring to produce
            """

        self.capacity = None
        # information from spring
        self.sens, self.wire = sens, wire
        # the rolling tool
        self.roll_tool = str()
        # the layout of the machine, all of the place are initialized as None,
        # execpt the cut slide.
        # when a slide is renseigned, he is add to the layout dictionnary.
        #self.layout = {'0': None, '45': None, '90':None, '135': None,
        #               '180': None, '225': None, '270': None, '315': None}
        # the entry of the machine, do receive a str() a values.
        self.entry = {'A1': None, 'A2': None, 'A3': None, 'A4': None,
                      'A5': None, 'A6': None, 'A7': None, 'A8': None}
        # the poka-yoke modules
        self.sensors = {'M0': False, 'M1': False, 'SCD': False, 'CAM': False}
        # if a clamp is used
        self.clamp = False


class MxType(Machine):
    """ A MX machine """

    def __init__(self, wire, sens=RIGHT):

        Machine.__init__(self, wire, sens)

        ## Initialisation of the MX layout ##
        self.S = MotorSlide(0, True)
        self.T = MotorSlide(45, True)
        self.U = MotorSlide(90, True)
        self.V = MotorSlide(135, True)
        self.W = MotorSlide(180, True)
        self.X = MotorSlide(225, True)
        self.Y = MotorSlide(270, True)
        self.Z = MotorSlide(315, True)
        ## Availables pinner motors ##
        self.P, self.Q = SpinnerMotor(), SpinnerMotor()
        ## Availables Supports ##
        self.Supports = (SP, STA, STU)
        ## Standard placement ##
        # The S motor is restricted to <ST> support.
        self.S.add_elt(Support(ST, self.roll_tool))
        # Avoid the winding direction, the cut slide and a Spinner motor
        # are directly placed in standard position.
        if self.sens is LEFT:
            self.Z.add_elt(Support(SC, 'TC28'))
            self.U.add_elt(self.P)
        else:
            self.T.add_elt(Support(SC, 'TC28'))
            self.Y.add_elt(self.P)


class Mx20(MxType):
    """ A MX20 machine """

    def __init__(self, wire, sens=RIGHT):

        Mx.__init__(self, wire, sens)
        self.capacity = 2.0
        # the only rolling tools in MX20 machines is 'TB1 [wire diam]'.
        self.roll_tool = 'TB1 ' + str(wire)


class Mx10(MxType):
    """ A MX10 machine """

    def __init__(self, wire, sens=RIGHT):

        Mx.__init__(self, wire, sens)
        self.capacity = 1.0
        self.rackS = Rack(self.S, True)
        # the standard rolling tools is in MX10 machines is 'WT3 [wire diam]'.
        self.roll_tool = 'WT3 ' + str(wire)
