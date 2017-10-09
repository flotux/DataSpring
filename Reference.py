#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

"""
    Reference.

        It is the principal class in the programme.
        Contain all information about a reference of spring :

            - quotations of the spring
            - machine used
            - regulation of the machine
            - tool used
            - cadency

        """

import Spring
import Machine

class Reference(object):

    def __init__(self, ref, Spring, Machine):
        """
            ref -- the reference, for indexing
            Spring -- the Spring link <class>
            Machine -- a Machine link <class> """

        self.ref = ref
        self.Spring = Spring
        self.Machine = Machine

    def save(self):
        pass

    def delete(self):
        pass

    def __str__(self):
        pass
