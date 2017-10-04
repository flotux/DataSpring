#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" Spring

    A representation of a spring.
    """

import sprlib

class Spring(object):

    def __init__(self, ref, ind, wire, diam, diam_tol, nb,
                 machine, angle=0, angle_tol=0):
        """
            ref -- reference of the spring
            ind -- indice of the spring
            wire -- wire diameter
            diam -- body diameter
            diam_tol -- diameter toleration
            nb -- number of coils
            machine -- machine used
            angle -OPTIONAL- angle of spring
            angle_tol -OPTIONAL- angle toleration """

        self.ref = ref
        self.ind = ind
        self.wire = wire
        self.diam = diam
        self.diam_tol = diam_tol
        self.nb = nb
        self.machine = machine

        if angle:
            self.angle = angle
            if angle_tol:
                self.angle_tol = angle_tol


    def evaluate(self):
        """ Evaluate the spring and calcul all neccesary informations
            with the sprlib library.
            Called by init. """
        pass


    def save(self):
        """ Saving spring in DTB """
        pass


    def __str__(self):
        pass
