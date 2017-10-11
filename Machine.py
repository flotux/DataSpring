#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" Machine

    TODO

    Just limited at the MX's machine for the moment.
    """

from machlib import *

class Machine(object):
    """ Represent a machine """

    def __init__(self, wire, sens):
        """
            wire -- the wire diameter of the spring to produce
            sens -- the winding direction of the spring to produce
            """

        self.capacity = None
        self.sens, self.wire = sens, wire
        self.roll_tool = None
        self.cut_tool = Tool('TC28')
        self.clamp = False
        self.sensors = {'M0': False, 'M1': False, 'SCD': False, 'CAM': False}
        self.entry = {'A1': None, 'A2': None, 'A3': None, 'A4': None,
                      'A5': None, 'A6': None, 'A7': None, 'A8': None}


class MotorType(Machine):
    """ A motor type include MX machine, all of these slides are locked
        in the layout.

        regulare (MX) :
        - 8 motorised non-linear axes slides -- S - T - U - V - W - X - Y - Z
        - 2 rotary motor -- P - Q
        - 1 optionnal rotary motor -- J

        The rotary motor can mount anywhere exepted in the S axe.
        Acording the generation  of the machine, the machine can have a linear
        modules to mount directly in any motor slide.
        """

    def __init__(self, wire, sens):

        Machine.__init__(self, wire, sens)

        ## initialisation of the MX layout ##
        self.s = MotorSlide(0, True)
        self.t = MotorSlide(45, True)
        self.u = MotorSlide(90, True)
        self.v = MotorSlide(135, True)
        self.w = MotorSlide(180, True)
        self.x = MotorSlide(225, True)
        self.y = MotorSlide(270, True)
        self.z = MotorSlide(315, True)
        ## rotary motors ##
        self.p, self.q = SpinnerMotor(), SpinnerMotor()
        ## supports ##
        self.Supports = (SP, STA, STU, SC)
        # avoid the winding direction, the cut slide
        # are directly placed in standard position.
        if self.sens is 'left':
            self.z.add_elt(Support(SC, self.cut_tool))
        else:
            self.t.add_elt(Support(SC, self.cut_tool))



class CamType(Machine):
    """ A camme machine type, all of these slide, linear motor and rotary motor
        can be removed from the layout. the rotary motors can be mount anywhere
        there a tree type of camme machine with different axe, motor names.

        no motorised (SX):
        - 8 cammes slides

        1st generation motorised (MCS-G):
        - 8 cammes slides
        - 2 rotary/linear combo motors -- Y - X
        - 1 optionnal rotary/linear combo motor -- Z

        2nd generation motorised (AX-MCS):
        - 8 cammes slides
        - 2 motorised linear axes -- X (for rolling tool by default) - Y
        - 2 rotary motors -- Q - P
        - 1 optionnal rotary motor -- J

        The motorised axe can be mounted in a regular slide like a rotary motor
        but it is inpossible to mount a linear motors axes and rotary motors
        in the same slide.
        """

    def __init__(self, wire, sens):

        Machine.__init__(self, wire, sens)
        ## initalisation of the camme layout ##
        # slide0 not initialized
        self.slide1 = CammeSlide(45)
        self.slide2 = CammeSlide(90)
        self.slide3 = CammeSlide(135)
        self.slide4 = CammeSlide(180)
        self.slide5 = CammeSlide(225)
        self.slide6 = CammeSlide(270)
        self.slide7 = CammeSlide(315)
        ## rolling tool ##
        self.roll_tool = Tool(('WT3 ' + str(wire)))
        self.s.add_elt(SUPPORT(STS, self.roll_tool))
        # avoid the winding direction, the cut slide
        # are directly placed in standard position.
        if self.sens is 'left':
            self.slide7.add_elt(Support(SC, self.cut_tool))
        else:
            self.slide1.add_elt(Support(SC, self.cut_tool))


class Mx20(MotorType):
    """ A MX20 machine """

    def __init__(self, wire, sens):

        MotorType.__init__(self, wire, sens)
        self.capacity = 2.0
        # the only rolling tools in MX20 machines is 'TB1 [wire diam]'.
        self.roll_tool = Tool(('TB1 ' + str(wire)))
        self.s.add_elt(SUPPORT(ST, self.roll_tool))


class Mx10(MotorType):
    """ A MX10 machine """

    def __init__(self, wire, sens):

        MotorType.__init__(self, wire, sens)
        self.capacity = 1.0
        self.rackS = Rack(self.S, True)
        # the standard rolling tools is in MX10 machines is 'WT3 [wire diam]'.
        self.roll_tool = Tool(('WT3 ' + str(wire)))
        self.s.add_elt(SUPPORT(ST, self.roll_tool))


class Ax20(CamType):
    """ A AX20 machine """

    def __init__(self, wire, sens):

        CamType.__init__(self, wire, sens)
        self.x = MotorSlide(0)
        self.p, self,q = SpinnerMotor(), SpinnerMotor()
        self.capacity = 2.0
        self.s.add_elt(STS, self.roll_tool)


class Mcs20(Ax20):
    """ A MCS20 machine """

    def __init__(self, wire, sens):

        Ax20.__init__(self, wire, sens)
