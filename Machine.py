#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" Machine

    TODO
    """

import machlib

class Machine(object):
    """ Represent a machine """

    def __init__(self, model):
        """
            model -- a dict correspond to a Machine
            """
        self.model = model.get("name")
