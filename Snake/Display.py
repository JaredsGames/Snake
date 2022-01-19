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
This module contains a basic "factory" pattern for generating new Display instances
"""

from datetime import datetime
import abc
import dataclasses
import functools
import json
import pathlib
import pygame
import sys
import time
import typing

from Snake.Button import Button
from Snake.Difficulty import Difficulty
from Snake.Direction import Direction
from Snake.Fruit import Fruit
from Snake.Grid import Grid
from Snake.Player import Player
from Snake.Point import Point
from Snake.Snake import Snake


class Display:
    """
    Not fully virtual class for each display to
    inherit from
    """

    def __init__(
        self, width: int = 800, height: int = 650, color=pygame.Color("black")
    ):
        # Checks for errors encountered
        num_pass, num_fail = pygame.init()
        if num_fail > 0:
            print(f"[FATAL] There were {num_fail} error(s) produced!")
            sys.exit(-1)
        else:
            print("[+] Game successfully initialised")
        pygame.font.init()
        self.width, self.height = width, height
        self._display_surface = pygame.display.set_mode(
            (self.width, self.height), pygame.HWSURFACE
        )
        self.last_position = Point(-1, -1)
        self.background_color = color
        self.fps_meter = pygame.time.Clock()

    @abc.abstractmethod
    def draw(self):
        """
        Abstract draw class that must be implemented
        """

        pass

    def get_surface(self) -> pygame.Surface:
        """
        Obtain the current display surface
        to a given window
        @return - pygame.Surface
        """

        return self._display_surface

    def clear_text(self) -> None:
        """
        This removes all text from the screen
        """

        self._display_surface.fill(self.background_color)

    def draw_image(self, img_object: pygame.Surface, position: Point) -> None:
        """
        Draw an image object (in the form of a surface) to the screen
        at a given position
        @param img_object : currently loaded pygame surface that represents an image
        @param position : Cartesian coordinates that represent where on the screen to be drawn to
        """

        self._display_surface.blit(img_object, dataclasses.astuple(position))

    def write_text(self, text: str, position: Point, font, color=pygame.Color("white")) -> None:
        """
        Write text to the screen, thanks to @NICE
        for helping with this!
        @param text - stuff we want to write to the screen
        @param position - where on the screen should it be writing to
        @param font - current font used
        @param color - selected color
        """

        lines = [line.split(" ") for line in text.splitlines()]
        space = font.size(" ")[0]

        x, y = dataclasses.astuple(position)
        self.last_position = position

        for line in lines:
            for word in line:
                word_surface = font.render(word, 0, color)
                width, height = word_surface.get_size()
                if x + width >= self.width + 100:
                    x = position.x
                    y += height
                self._display_surface.blit(word_surface, (x, y))
                x += width + space
            x = position.x
            y += height

    def center(self) -> Point:
        """
        Obtain the center of the current scene
        @return Point
        """

        return Point(self.width // 4, self.height // 4)


class GameDisplay(Display):
    """
    Class that represents the game scene
    All logic is handled internally
    """

    def __init__(self, difficulty: int):
        super().__init__()
        self.score_board_position = Point(650, 10)
        self.snake = Snake()
        self.grid = Grid(width=20, height=20)

        self.internal_timer = 0
        self.MOVEEVENT, self.GENFRUIT, self.t = (
            pygame.USEREVENT + 1,
            pygame.USEREVENT + 2,
            250,
        )
        self.COLLIDED = pygame.USEREVENT + 3
        self.has_spawned_fruit = False
        self.fruit = Fruit()
        self.score = 0
        self.difficulty = difficulty

    def collision_detection(self) -> bool:
        """
        Detect whether we are on the same position as the fruit
        TODO : fix what entity you're colliding against, poison mechanic would be nice
        @return - bool
        """

        if self.fruit is None:
            return False

        return dataclasses.astuple(self.snake.head) == dataclasses.astuple(
            self.fruit.instance.position
        )

    def handle_fruit_generation(self, has_collided: bool) -> None:
        """
        Fruit needs to correctly generate anywhere on the grid and cannot
        spawn a new one until the currnt one has been found
        @param has_collided : have we hit the current fruit
        """

        if not self.has_spawned_fruit or self.fruit is None:
            self.fruit = Fruit()
            x, y = dataclasses.astuple(self.fruit.instance.position)
            self.grid.grid[x][y].state = self.fruit.instance.state
            self.has_spawned_fruit = True

        if has_collided:
            x, y = dataclasses.astuple(self.fruit.instance.position)
            self.grid.grid[x][y].state = pygame.Color("white")
            self.has_spawned_fruit = False

    def remove_duplicate_parts(self):
        """
        Removing duplicate elements from the snake
        There is a fundamental bug in the logic in the game loop so
        I Jerry rigged this solution
        """

        self.snake.body = [
            i
            for n, i in enumerate(self.snake.body)
            if i not in self.snake.body[n + 1:]
        ]

    def draw(self) -> int:
        """
        Main game logic contained here
        Will return the current score obtained so it can pas it to the high score screen
        @return - int
        """

        draw_loop, collided = True, False

        pygame.time.set_timer(self.GENFRUIT, 1500)
        change_to = Direction.EAST.name
        direction = Direction.EAST.name

        while draw_loop:

            # snake goes off the board
            """
            position = (14, 13)
            lambda   = (False, False)
                     = False
            """
            if any(map(lambda x: x < 0, dataclasses.astuple(self.snake.head))):
                draw_loop = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = Direction.NORTH.name
                    if event.key == pygame.K_DOWN:
                        change_to = Direction.SOUTH.name
                    if event.key == pygame.K_LEFT:
                        change_to = Direction.WEST.name
                    if event.key == pygame.K_RIGHT:
                        change_to = Direction.EAST.name
                elif event.type == self.GENFRUIT:
                    self.handle_fruit_generation(collided)

            if (
                (
                    change_to == Direction.NORTH.name
                    and direction != Direction.SOUTH.name
                )
                or (
                    change_to == Direction.SOUTH.name
                    and direction != Direction.NORTH.name
                )
                or (
                    change_to == Direction.EAST.name
                    and direction != Direction.WEST.name
                )
                or (
                    change_to == Direction.WEST.name
                    and direction != Direction.EAST.name
                )
            ):
                direction = change_to
            prev_x, prev_y = dataclasses.astuple(self.snake.tail)
            self.transform_snake(direction)
            x, y = dataclasses.astuple(self.snake.head)

            self.snake.body.insert(0, Point(x, y))

            if self.collision_detection() and not collided:
                self.has_spawned_fruit = False
                self.fruit = None
                self.score += 1
                collided = True

                if direction == Direction.WEST.name:
                    x += 1
                if direction == Direction.EAST.name:
                    x -= 1
                if direction == Direction.NORTH.name:
                    y -= 1
                if direction == Direction.SOUTH.name:
                    y += 1

                # for some reason we need to do this? collision detection does
                # not work properly
                self.remove_duplicate_parts()
                self.snake.body.append(Point(x, y))
            else:
                collided = False
                self.snake.body.pop()
            self.grid.grid[prev_x][prev_y].state = pygame.Color("white")

            self.clear_text()

            self.write_text(
                f"Score: {self.score}",
                self.score_board_position,
                pygame.font.SysFont(None, 30),
            )

            # Snake componets
            try:
                # If for whatever reason one of our body parts
                # goes off screen, we need to catch this and end the game loop
                for part in self.snake.body:
                    x, y = dataclasses.astuple(part)
                    self.grid.grid[x][y].state = pygame.Color("blue")
            except IndexError:
                draw_loop = False

            self.grid.draw(self._display_surface)

            pygame.display.update()
            self.fps_meter.tick(self.difficulty)

            # is the head touching any part of the body other than itself?
            if any(map(lambda x: x == self.snake.head, self.snake.body[2:])):
                draw_loop = False

        return self.score

    def transform_snake(self, direction: Direction) -> None:
        """
        Move all componets of the snake correctly
        according to their direction in space
        @param direction - cardinal direction we need to move in
        """

        x, y = dataclasses.astuple(self.snake.head)

        if direction == Direction.NORTH.name:
            self.snake.head.y -= 1
        if direction == Direction.SOUTH.name:
            self.snake.head.y += 1
        if direction == Direction.EAST.name:
            self.snake.head.x += 1
        if direction == Direction.WEST.name:
            self.snake.head.x -= 1

        self.grid.grid[x][y].state = pygame.Color("white")


class HighScoreDisplay(Display):
    """
    Class that represents the high score display
    """

    def __init__(self, current_score: int, username: str):
        super().__init__()
        self.title_position = Point(250, 45)
        self.logo_position = Point(575, 435)
        self.break_from_draw = False
        self.back_button = Button(
            self._display_surface,
            Point(10, 575),
            300,
            50,
            "Quit",
            functools.partial(self.terminate_intro),
        )
        self.scoreboard_file = pathlib.Path("scores/scoreboard.json")
        self.scores = self.obtain_high_score_list(self.scoreboard_file)
        self.scores.append(
            Player(username, current_score,
                   datetime.now().strftime("%m/%d/%Y %H:%M"))
        )
        self.scores = sorted(self.scores, reverse=True)

    def obtain_high_score_list(self, path: pathlib.Path) -> typing.List[Player]:
        """
        Read in high score list found in a json file
        that is then loaded and sorted by the score obtained
        by a given player
        @param path - path to JSON file
        @return - typing.List[Player]
        """

        with open(path, "r") as fp:
            contents = json.load(fp)

        return [Player(**element) for element in contents["players"]]

    def terminate_intro(self):
        """
        This terminates the current scene
        """

        self.break_from_draw = True
        self._display_surface.fill(self.background_color)
        master = {"players": []}
        for score in self.scores:
            master["players"].append(dataclasses.asdict(score))

        with open(self.scoreboard_file, "w") as fp:
            json.dump(master, fp)

        pygame.quit()
        sys.exit()

    def draw(self):
        """
        Draw all the high scores in a row like
        manner
        """

        draw_loop = True
        snake_logo = pygame.image.load("assets/snake_trans.png")

        while draw_loop and not self.break_from_draw:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate_intro()

            self.draw_image(snake_logo, self.logo_position)
            self.write_text(
                f"HIGH SCORES", self.title_position, pygame.font.SysFont(
                    None, 50)
            )

            self.write_text(
                self.back_button.contents,
                self.back_button.center(),
                pygame.font.SysFont(None, 30),
            )
            self.back_button.draw()

            for i, score in enumerate(self.scores[0:5]):
                x, y = dataclasses.astuple(self.center())
                self.write_text(
                    score.name,
                    Point((x - 50), y + i * 50),
                    pygame.font.SysFont(None, 33),
                )
                self.write_text(
                    str(score.score),
                    Point((x - 50) + 200, y + i * 50),
                    pygame.font.SysFont(None, 33),
                )

                self.write_text(
                    score.tod,
                    Point((x - 50) + 400, y + i * 50),
                    pygame.font.SysFont(None, 33),
                )
            pygame.display.flip()


class IntroDisplay(Display):
    """
    First scene the user sees
    """

    def __init__(self):
        super().__init__()
        self.title_position = Point(250, 45)
        self.logo_position = Point(275, 100)
        self.break_from_draw = False
        self.buttons = [
            Button(
                self._display_surface,
                Point(250, 400),
                300,
                50,
                "Start",
                functools.partial(self.terminate_intro),
            ),
        ]

    def terminate_intro(self):
        """
        Kill the current window
        """

        self.break_from_draw = True

    def draw(self) -> Difficulty:
        """
        Draw the current instance
        """
        draw_loop = True
        snake_logo = pygame.image.load("assets/snake_trans.png")

        while draw_loop and not self.break_from_draw:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_image(snake_logo, self.logo_position)
            self.write_text(
                f"SNAKEY SNAKE", self.title_position, pygame.font.SysFont(
                    None, 50)
            )
            for button in self.buttons:
                self.write_text(
                    button.contents, button.center(), pygame.font.SysFont(None, 30)
                )
                button.draw()
            pygame.display.flip()
        return Difficulty.EASY.value
