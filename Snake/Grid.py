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
This module contains the logic for a grid class
"""

import dataclasses

from Snake.Cell import Cell
from Snake.Point import Point
from Snake.Fruit import Fruit


@dataclasses.dataclass
class Grid:
    """
    This is normally not done but because we need to
    have the grid and snake positions be the same memory addreses, we are forced to embded it into this class
    This would not be an issue if we could pass pointers from one another but since this is Python, we have no choice :(
    Copying memory each loop is going to be costly
    """

    width: int
    height: int
    cell_width: int = 20  # in pixels

    def __post_init__(self):
        self.grid = []
        for x in range(0, self.width):
            container = []
            for y in range(0, self.height):
                cell = Cell(Point(x, y), self.cell_width)
                container.append(cell)
            self.grid.append(container)
        self.center = (int(self.width / 2), int(self.height / 2))
        x, y = self.center
        # self.snake_body: typing.List[Cell] = [self.grid[x][y]]

    def draw(self, screen):
        """
        Draw all the cells to the screen
        """

        for x in self.grid:  # x
            for element in x:  # y
                element.draw(screen)

    def draw_select_components(self, screen, positions):
        """
        Only draw select cells on the screen
        """

        for part in positions:
            x, y = dataclasses.astuple(part)
            self.grid[x][y].state = (255, 0, 0)
            self.grid[x][y].draw(screen)

    def spawn_fruit(self):
        """
        Spawn a fruit
        """

        f = Fruit()
        x, y = dataclasses.astuple(f.instance.position)
        self.grid[x][y] = f.instance
        return [x, y]
