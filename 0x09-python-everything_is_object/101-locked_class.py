#!/usr/bin/python3

class LockedClass:
    """
    Represents a class with restricted instance attribute creation.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initializes a LockedClass instance.
        """
        pass
