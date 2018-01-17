
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
    """ Fromat a StringVar to float """

    target = float()
    try:
        target = float(var)
    except ValueError as e:
        var = var.replace(",", ".")
        target = float(var)
    finally:
        if type(target) is float:
            return target
        else:
            pass

if __name__ == '__main__':
    float_var = format_to_float("bonjour")
    print(float_var, type(float_var))
