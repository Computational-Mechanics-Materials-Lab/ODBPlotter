#!/usr/bin/env python3

"""
Utility methods for odb_plotter
"""

from typing import Union, TypeAlias


AnswerType: TypeAlias = Union[tuple[str, str], tuple[str, str, str]]
DefaultType: TypeAlias = Union[None, str]
def confirm(message: str, confirmation: str, default: DefaultType = None) -> bool:
    yes_vals: AnswerType = ("yes", "y")
    no_vals: AnswerType = ("no", "n")
    if isinstance(default, str):
        if default.lower() in yes_vals:
            yes_vals = ("yes", "y", "")
            confirmation += " (Y/n)? "
        elif default.lower() in no_vals:
            no_vals = ("no", "n", "")
            confirmation += " (y/N)? "

    else:
        confirmation += " (y/n)? "

    while True:
        print(message)
        user_input: str = input(confirmation).lower()
        if user_input in yes_vals:
            return True
        elif user_input in no_vals:
            return False
        else:
            print("Error: invalid input")