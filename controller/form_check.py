#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

"""
    form_check

        A function library for the GUI.
        """


def format_float(var, mode=0):
    """ Fromat a string to float.

            var -str- the variable.
            mode 0 - return the float value
            mode 1 - return True if the converstion is possible
            Return mode 0:
                float(var) - var is convertible to float
                False - is not
            Return mode 1:
                True - var is convertible to float
                False - is not
        """

    try:
        float(var)
    except ValueError as e:
        # if the string have a comma instead of a point.
        if "," in var:
            var = var.replace(",", ".")
            format_float(var, mode)
    else:
        if mode is 0:
            return float(var)
        elif mode is 1:
            return True

    return False


def empty(var):
    """ check if the received variable is empty or not.

        var -float- the variable.
        Return:
            True -  it is empty
            False - it is not empty
        """

    if len(var):
        return False
    else:
        return True


def valide(var):
    """ check if the var is valide.
        The value do not be empty and must be convertible to float.

        var -float- the variable.
        return:
            True - is valide
            False - is not valide
        """

    if not empty(var) and format_float(var, 1):
        return True
    else:
        return False


def highlight(item, color="Yellow"):
    """ Highlight the item received. """

    item.config(background=color)


if __name__ == '__main__':
    str_var = "12,6"
    var = format_to_float(str_var)
    print(var, type(var))
