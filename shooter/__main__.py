import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Space Shooter"
WHITE = Color(255, 255, 255)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)


def main():
    
    # create the cast
    cast = Cast()
    
    # Scores
    cast.add_actor("scores", Actor())
    cast.add_actor("scores", Actor())

    scores = cast.get_actors('scores')
    # Player one
    scores[0].set_text('Player one: W, A, S, D, X')
    scores[0].set_color(BLUE)
    scores[0].set_position(Point(15, 0))
    # Player two
    scores[1].set_text('Player two: I, J, K, L, M')
    scores[1].set_color(GREEN)
    scores[1].set_position(Point(730, 0))
    
    # player one
    x = int(MAX_X / 3)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    player_one = Actor()
    player_one.set_text("#")
    player_one.set_font_size(FONT_SIZE)
    player_one.set_color(BLUE)
    player_one.set_position(position)
    cast.add_actor("ships", player_one)
    
    # player two
    x = int((MAX_X / 3) * 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    player_two = Actor()
    player_two.set_text("#")
    player_two.set_font_size(FONT_SIZE)
    player_two.set_color(GREEN)
    player_two.set_position(position)
    cast.add_actor("ships", player_two)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()