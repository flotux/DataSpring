#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Author : florian Vitalli
# Contact : flvitalli@gmail.com

""" tklib

    A library for make tkinter object.
    """

import tkinter

def label(root, caption, row, **options):

    caption += " : "
    tkinter.Label(root, text=caption).grid(row=row, **options)

def label_entry(root, caption, var,  row, width=10, padx=16, pady=8, column=1, \
                **options):
    """ Create a label, entry in the same row.
            root : the parent
            caption : the text of the label
            var : the textvariable of the entry
        """

    caption += " : "
    tkinter.Label(root, text=caption).grid(row=row, column=column, \
                                           padx=padx, pady=pady)
    entry = tkinter.Entry(root, textvariable=var, width=width)
    entry.grid(row=row, column=column+1)

    return entry

def radiobutton(root, caption, var, value, width=8, indicatoron=1, column=1, \
                             color="White", **options):
    """ make a radiobutton """

    radiobutton = tkinter.Radiobutton(root, text=caption, variable=var, \
                                 value=value, width=width, selectcolor=color, \
                                 indicatoron=indicatoron)

    radiobutton.grid(row=1, column=column, **options)

    return radiobutton

def info_label(root, caption, var, row, unity="mm", width=20, padx=4, pady=8, \
                 column=1, **options):
    """ Creat a triple label wiget.
            1. caption - the description
            2. var - the contain
            3. row - the row of the object
            4. unity - the unity of the Contain (mm bye default)

        Return the contain label.
        """

    caption += " : "
    tkinter.Label(root, text=caption, width=width).grid(row=row, column=column, \
                                           padx=padx, pady=pady)
    var_label = tkinter.Label(root, text=var, width=int(width/4))
    var_label.grid(row=row, column=int(column+1), padx=padx, pady=pady)

    tkinter.Label(root, text=unity, width=int(width/4))\
    .grid(row=row, column=int(column+2), padx=0, pady=pady)

    return var_label

def overbutton(root, row, column, command, **options):

    lbf = tkinter.LabelFrame(root, width=110, height=180)
    lbf.grid(row=row, column=column, padx=10, pady=10)
    button= tkinter.Button(lbf, text="AJOUTER", command=command)
    button.pack(padx=20, pady=40)

    return lbf, button

def combo_radio(root, caption, row, column, command, elt):
    """ Create a radiobutton group with a label and checkbutton
        for disabled/enabled the radiogroup.
            root -- the root
            row -- the row
            column -- the column
            command -- the command associated too buttons
        """
