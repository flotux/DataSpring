#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

"""
    guilib.py

        A function library for the GUI.
        """


def format_to_float(var):
    """ Fromat a string to float.
            var -- the string to convert
        if the conversion is imposible, return None.
        """

    try:
        float(var)
    except ValueError as e:
        # if the string have a comma instead of a point.
        if "," in var:
            var = var.replace(",", ".")
            return float(var)
        else:
            return None
    else:
        return float(var)


if __name__ == '__main__':
    str_var = "12,6"
    var = format_to_float(str_var)
    print(var, type(var))
