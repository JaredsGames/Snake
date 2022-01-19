"""
Main driver code for Snake
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

import pygame
import random
import sys
import time
import functools
import typing


from Snake.Difficulty import Difficulty
from Snake.Display import GameDisplay, IntroDisplay, HighScoreDisplay
from Snake.DisplayManager import DisplayManager
from Snake.Point import Point

difficulty = Difficulty.EASY.value
username = input("[INFO] What is your name: ")

options: typing.Dict[str, int] = {
    "EASY": Difficulty.EASY.value,
    "MEDIUM": Difficulty.MEDIUM.value,
    "HARD": Difficulty.HARD.value,
}

_exit_condition = True

print("\n" * 2)

while _exit_condition:
    for (name, value) in options.items():
        print(f"[{name}]: {value} FPS")
    print("\n" * 2)
    try:
        _option = input("[INPUT] Select option: ")
    except EOFError:
        break
    difficulty = options.get(_option)
    if not difficulty:
        print("please select again")
    else:
        _exit_condition = False

manager = DisplayManager(
    functools.partial(IntroDisplay, ()),
    functools.partial(GameDisplay, difficulty),
    functools.partial(HighScoreDisplay, (username)),
)
manager.deploy()
