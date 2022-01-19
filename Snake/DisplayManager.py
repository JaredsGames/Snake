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
This module contains the implementation
of a manager class to manage a queue of scenes
"""

import functools
import typing

from Snake.Display import Display, GameDisplay


class DisplayManager:
    """
    Manager class that handles all possible Displays (scenes)
    that can be drawn
    """

    def __init__(self, *args):
        self.displays: typing.List[Display] = args
        self.score = 0

    def deploy(self) -> None:
        """
        We can run all of the current scenes queued however they are shown in a linear manner
        There is no possibility to return to a previous scene, this is something I would
        like to do when I have more time to refine this project
        """

        for display in self.displays:
            if not isinstance(display, functools.partial):
                raise ValueError(
                    f"expecting functools.partial class, obtained {type(display)} instead"
                )
            try:
                if display.func.__name__ == "GameDisplay":
                    self.score = display().draw()
            except IndexError:
                pass

            if display.func.__name__ == "HighScoreDisplay":
                display.func(self.score, *display.args).draw()

            if display.func.__name__ == "IntroDisplay":
                self.difficulty = display.func().draw()
