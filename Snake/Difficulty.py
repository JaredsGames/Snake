# Jared Dyreson
# CPSC 386-01
# 2021-11-29
# jareddyreson@csu.fullerton.edu
# @JaredDyreson
#
# Lab 00-04
#
# Some filler text
#

"""
Basic enumeration class for how difficult
the level should be
"""

import aenum


class Difficulty(aenum.Enum):
    """
    Each integer represents how many frames per second
    the canvas will be written to
    """

    EASY = 10
    MEDIUM = 25
    HARD = 40
    HARDER = 60
    IMPOSSIBLE = 120
