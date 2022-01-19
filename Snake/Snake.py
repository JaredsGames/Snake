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
This module contains the snake component
"""

import dataclasses
import typing

from Snake.Cell import Cell
from Snake.Direction import Direction
from Snake.Grid import Grid
from Snake.Point import Point


@dataclasses.dataclass
class Snake:
    """
    Snake implementation
    """

    # position is (0, 0) so we want to move right
    direction: Direction = Direction.EAST.name
    color: typing.Tuple[int, int, int] = dataclasses.field(
        default_factory=lambda: (255, 0, 0)
    )
    body: typing.List[Point] = dataclasses.field(
        default_factory=lambda: [Point(0, 0)])

    @property
    def length(self):
        """
        How long is it?
        """

        return len(self.body)

    @property
    def head(self):
        """
        Current head position
        """

        return self.body[0]

    @property
    def tail(self):
        """
        Current tail position
        """
        return self.body[-1]

    def append(self, position):
        """
        Add more to the end of the snake
        """
        self.body.append(position)
