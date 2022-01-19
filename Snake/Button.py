"""
This contains implementations for a Button
class present in Pygame
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

import functools
import pygame

from Snake.Point import Point


class Button:
    """
    Button class for Pygame, where a rectangle represents the body
    of the button and when there is a click/collision on the rectangle,
        a callback function is invoked
    """

    def __init__(
        self,
        surface: pygame.Surface,
        point: Point,
        width: int,
        height: int,
        contents: str,
        callback: functools.partial,
    ):
        """
        For some weird reason, Pygame doesn't have buttons?
        Found this here and decided to add upon it
        https://github.com/russs123/pygame_tutorials/blob/main/Button/button.py
        """

        self._surface = surface
        self.width, self.height = width, height
        self.point = point
        self.contents = contents
        self.rectangle = pygame.Rect(
            self.point.x, self.point.y, self.width, self.height
        )
        self.clicked = False
        self.callback = callback

    def draw(self) -> None:
        """
        Draw the current button to the screen
        and listen for collision along with a click.
        Once clicked, invoke the callback function
        @return - None
        """

        position = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.callback()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        pygame.draw.rect(self._surface, pygame.Color(
            "white"), self.rectangle, 1)

    def center(self) -> Point:
        """
        Obtain the center of the button and
        apply padding to x and y positions
        @return - Point
        """

        # TODO : CSS style padding
        x, y = self.rectangle.center

        return Point(x - 30, y - 5)
