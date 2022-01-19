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
This module contains the dataclass for the position on the screen
"""

import dataclasses


@dataclasses.dataclass
class Point:
    """
    Represents a Cartesian point in R^2
    """

    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
