from game.casting.actor import Actor
from game.shared.color import Color

class Laser():
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self, player):
        self._color = player.get_color()
        self._player_position = player.get_position()
        self._player_direction = player.get_direction()

    def shoot(self):
        # find the players location and direction
        # generate a new actor object with one of the two characters (either _vertical or _sideways)
        laser = Actor()
        laser.set_text("o")
        laser.set_font_size(15)
        laser.set_color(Color(255, 0, 0))
        laser.set_position(self._player_position)
        laser.set_velocity(self._player_direction)

        return laser
