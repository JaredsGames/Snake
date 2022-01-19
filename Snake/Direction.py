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
This represents the cardinal direction the snake can
be oriented on the grid
"""

import enum


class Direction(enum.Enum):
    """
    Represents cardinal direction
    """

    NORTH = enum.auto()
    EAST = enum.auto()
    WEST = enum.auto()
    SOUTH = enum.auto()
