#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

"""
    forms_controller

        A function library for the GUI.
        """


def format_float(var):
    """ Fromat a string to float.

            var -str- the variable.
            Return :
                float(var) - var is convertible to float
                False - is not
        """

    try:
        float(var)
    except ValueError as e:
        # if the string have a comma instead of a point.
        if "," in var:
            var = var.replace(",", ".")
            # the function is recursive
            format_float(var)
        else:
            return False

    return float(var)


def can_be_float(var):
    """ Check if the var can be converted in float type.

        var -str- the variable to check
        Return:
            True - a can be float
            False - a cannot
        """

    is_float = isinstance(format_float(var), float)
    return is_float


def empty(var):
    """ check if the received variable is empty or not.

        var -float- the variable.
        Return:
            True -  it is empty
            False - it is not empty
        """

    is_empty = not len(var)
    return is_empty


def valide(var):
    """ check if the var is valide.
        The value do not be empty and must be convertible to float.

        var -float- the variable.
        return:
            True - is valide
            False - is not valide
        """

    if not empty(var) and can_be_float(var):
        return True
    else:
        return False


def highlight(item, color="Yellow"):
    """ Highlight the item received.

        item -tk object- the item
        color -str- the color used for highlighting
        """

    item.config(background=color)


if __name__ == '__main__':
    var = 12.0
    print(can_be_float(var))
