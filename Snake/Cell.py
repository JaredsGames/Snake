"""
This contains implementations for a Cell
class that gets drawn to the screen.
Each of these entities represent where the snake
can move to
"""

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

import dataclasses
import pygame
import typing

from Snake.Direction import Direction
from Snake.Point import Point


@dataclasses.dataclass
class Cell:
    """
    This object is used in the Grid class
    """

    position: Point
    size: int

    margin: int = 5
    state: typing.Tuple[int, int, int] = (255, 255, 255)

    def draw(self, screen_reference):
        """
        Draw the cell instance to the screen
        """

        pygame.draw.rect(screen_reference, self.state, self.rectangle, 1)
        screen_reference.fill(self.state, self.rectangle)

    def __post_init__(self):
        """
        Use the information given to the "constructor" and
        create the proper dimensions for a Cell instance
        """

        x, y = dataclasses.astuple(self.position)

        def transformation(a: int):
            return (self.margin + self.size) * a

        x = transformation(x)
        y = transformation(y)

        self.rectangle = pygame.Rect(x, y, self.size, self.size)
