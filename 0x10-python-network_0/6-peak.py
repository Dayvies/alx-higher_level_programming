#!/usr/bin/python3
"""just using max"""


def find_peak(list_of_integers):
    """trying to get peaks"""
    if list_of_integers == [] or list_of_integers is None:
        return None
    else:
        return(max(list_of_integers))
