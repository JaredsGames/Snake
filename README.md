# Snake Game

In this exercise, we shall write a [snake game](https://en.wikipedia.org/wiki/Snake_(video_game_genre)). The original game concept comes from the 1976 arcade game [Blockade](https://en.wikipedia.org/wiki/Blockade_(video_game)). We are starting with this well worn game concept because it is a fun game to play, introduces us to a number of key ideas in writing game software, and there exists a wealth of examples to help us get our creativity jump started.

Remember, this assignment is an individual assignment where you are creating your own snake game clone.

In Blockade, the game is played by two players and each player has a character which navigates a planar world leaving a visible, impenetrable trail behind. The object of the game is to survive longer than the opposing player by not intersecting your player with your opponents trail or your own.

Since 1976, many variations of the game exist. If you have never played a snake game before, you can try it out on the [web](https://playsnake.org/), on [iOS](https://theappstore.org/search.php?search=snake&platform=software), or on [Android](https://play.google.com/store/search?q=snake&c=apps&hl=en_US&gl=US). On Linux, you can try install a snake game with `apt install nsnake`.

Our snake game shall have the following rules or requirements:

* The game must be written in Python using Pygame.

* The game must use object oriented design using the same principles from previous programming assignments. Projects which disregard this requirement will not be graded.

* The game must be graphical (not a text-based or text console game).

* The game must have at least one player (multi-player is at your discretion).

* The game may be controlled from the keyboard, mouse, or joystick.

* If using a joystick, there must be an option to fallback to a keyboard.

* The objective of the game is to score the highest score possible. Scores are increased by the amount of time the game has been played and by having the player's character eat food.

* The player's character dies when the player's character touches itself, another player, a boundary, or a hazard. When the player's character dies, the game ends.

* A game board may have tunnels or passageways which allow a player's character to enter one location in the game world and appear elsewhere in the game world. Tunnels and passageways are optional. Bonuses or penalties may be assigned for using passageways and tunnels.

* A boundary is defined as the limits of the game board and may not be touched or crossed by a player. Food may not appear on a boundary.

* Food appears on the game board at regular intervals. Eating the food elongates the player's character. There must be a minimum of one food type. There may be other food types which increase the player character's size, shape, color, etc. Eating food scores points.

* The player may move their character in four orthogonal directions (up, down, left, right). The player's character behaves like a train which follows the same path until it reaches a point on the game board where a direction was changed. (See https://playsnake.org/ for a visual example of how the snake moves.)

* The player has only one life. Should the player's game end, the player must start over.

* The player accrues points for every 3 seconds of game play. You may determine the number of points and if there are bonus points should a player reach in-game milestones.

* The game presents a start up screen which summarizes the rules and controls. From the start up screen a player may start a new game. Other optional game play options may be presented on the start up screen such as the high score leaderboard, settings, etc.

* The player's points are displayed somewhere on the screen and the display must not interfere with game play.

* The date, the total time played, and the score is saved to a JSON or Pickle file at the end of every game.

* A leaderboard of high scores is presented at the end of every game.

* The option to play again is given at the end of every game.

* A soundtrack and sound effects are optional. You are encouraged to incorporate music and effects into your game.

* The main function must be called from the file named `snake.py`.

* You must conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/). Use [pylint](https://www.pylint.org/) and [pycodestyle](https://pypi.org/project/pycodestyle/) to conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/).

Since this is the first time we are using Pygame, remember that there are a number of excellent resources available to you.

The first is the Pygame documentation and the Pygame source code. Within the Pygame source code is a directory of examples which can illustrate fundamental Pygame features and how to use them. Learning to navigate the source code and the system's documentation is an invaluable skill to develop.

The second is [Al Sweigart's](https://alsweigart.com/) book [Making Games with Python & Pygame](https://inventwithpython.com/pygame/). The full text of the book is available online at no cost and available for purchase through retailers. The book is very brief and focuses on building one game per chapter. [Chapter 6 builds a snake clone named Wormy.py](https://inventwithpython.com/pygame/chapter6.html). The source code for all the games in the book are available from GitHub.

You are encouraged to read through the source code by Mr. Sweigart and others who have written excellent snake game clones. Be warned that you are tasked with creating your own game. Copying and pasting or starting from someone else's game is not ethical and strictly forbidden.

Start from scratch. Make your own game. Make something you'll be proud to share with family and friends.

# Rubric

* Functionality (6 points): Your submission shall be assessed for the appropriate constructs and strategies to address the exercise. A program the passes the instructor's tests completely receives full marks. A program that partially passes the instructors tests receives partial-marks. A program that fails the majority or all the tests receives no marks.

* Format & Readability (4 point): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is. Failure to include a header forfeits all marks.

# Linux Commands

- `convert assets/snake.png -resize 200x200 -transparent white assets/snake_trans.png`: remove all white spaces and make it transparent
- `convert dont.png -opaque "rgb(255,255,0)" result.png`: remove all yellow from the image

# Link to External Resources

- [Don't Step on Snek](https://www.deviantart.com/sharktopus23/art/Don-t-Tread-on-Me-314647647)
