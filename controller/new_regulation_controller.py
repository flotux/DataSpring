
"""
    The controller of the class NewRegulation in view/new_regulation.py

        validation -- control if the variables is correct.
        format_to_float -- format a string to float.
        send -- send the variables too root.
    """

def validation(id, customer, machine, wire, ref_wire, material, sens, \
               diam, nb, tol):
    """ Control all information send by new_regulation windows.
        """
    pass

def send():
    """ Send information too view/root.py """
    pass

def format_to_float(var):
    """ Fromat a string to float.
            var -- the string to convert
        if the conversion is imposible, raise a ValueError.
        """

    try:
        float(var)
    except ValueError as e:
        # if the string have a comma instead of a point.
        if "," in var:
            var = var.replace(",", ".")
            return float(var)
        else:
            raise ValueError
    else:
        return float(var)


if __name__ == '__main__':
    str_var = "12,6"
    var = format_to_float(str_var)
    print(var, type(var))
