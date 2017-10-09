#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" sprlib

    A function library for geometric calculs on spring,
    used by Spring class, she can be aslo use directly for direct calculs.
    """

import math

PI = math.pi
SOLID_ANGLE = 360
LEFT = 'left'
RIGHT = 'right'

STEEL = 'Steel'
INOX = 'Inox'
MATERIAL = [STEEL, INOX]

__all__ = ["sensor_tol", "one_degree", "body_length", "body_weight",
           "angle_move", "arc_feed"]


def sensor_tol(tol, nb):
    """ Return the millimeter value to enter in the sensor.

        tol -- body toleration
        nb -- number of coils """

    return (tol + tol) * PI * nb


def one_degree(wire, diam):
    """ Return the millimeter value for having 1 degree.

        wire -- wire diameter
        diam -- body diameter """

    return (diam - wire) * PI / SOLID_ANGLE


def body_length(wire, diam, nb):
    """ Return the body length.

        wire -- wire diameter
        diam -- body diameter
        nb -- number of coils """

    return (diam - wire) * PI * nb


def body_weight(wire, nb):
    """ Return the body weight.

        wire -- wire diameter
        nb -- number of coils """

    return (wire * nb) - wire


def oob_diam(diam, material, diff=0.10):
    """ Return the out of box diameter.

        diam -- body diameter
        material -- material of spring
        diff -- diameter move after treatment """

    if material is STEEL:
        return diam + diff
    else:
        return diam - diff

def angle_move(wire, diam, move):
    """ Return the angle movement for a diameter move.

        wire -- wire diameter
        diam -- body diameter
        move -- movement of the body diameter """

    degree = one_degree(wire, diam)
    return (move * PI) / degree


def arc_feed(ray, angle):
    """ Return the feed necessary to make a angle with
        a ray specify.
        The ray must be at the neutral fiber.

        ray -- ray
        angle -- angle """

    return (ray * PI) / SOLID_ANGLE * angle
