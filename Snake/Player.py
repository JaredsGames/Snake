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
This module contains a dataclass for the Player
"""

import dataclasses


@dataclasses.dataclass
class Player:
    """
    Basic dataclass
    """

    name: str
    score: int
    tod: str

    def __lt__(self, other):
        """
        For sorting
        """

        return self.score < other.score
