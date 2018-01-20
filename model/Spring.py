#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" Spring

    A representation of a spring.
    """

class Spring(object):

    def __init__(self, ref, customer, wire, diam, diam_tol, nb,
                 material, angl=0, angl_tol=0):
        """
            ind -- indice of the spring
            wire -- wire diameter
            diam -- body diameter
            diam_tol -- diameter toleration
            nb -- number of coils
            material -- the material used
            angl -OPTIONAL- angle of spring
            angl_tol -OPTIONAL- angle toleration """

        self.ref = ref
        self.customer = customer
        self.wire = wire
        self.diam, diam_tol = diam, diam_tol
        self.nb = nb
        self.machine = machine
        self.material = material

        ## if angle are find out ##
        if angle:
            self.angle = angle
            if angle_tol:
                self.angle_tol = angle_tol

        ## evaluation of the spring ##
        self.sensor_tol = sprlib.sensor_tol(tol, nb)
        self.mm_deg = sprlib.one_degree(wire, diam)
        self.body_length = sprlib.body_length(wire, diam, nb)
        self.body_weight = sprlib.body_weight(wire, nb)
        self.diam_oob = sprlib.oob_diam(diam, material)

    def __repr__(self):
        pass

    def __getattr__(self, attr):
        return None

    def __setattr__(self, attr, value):
        object.__setattr__(self, attr, value)
