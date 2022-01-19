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
Simple class for the fruit
"""

import dataclasses
import random

from Snake.Cell import Cell
from Snake.Point import Point


@dataclasses.dataclass
class Fruit:
    """
    Represents fruit the class the snake
    can eat
    """
    value: int = 1  # how many squares does the fruit award
    instance: Cell = None

    def __post_init__(self):
        self.instance = Cell(
            Point(random.randint(0, 16), random.randint(
                0, 18)), 20, 5, (255, 255, 0)
        )
