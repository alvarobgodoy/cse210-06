from game.services.laser import Laser
from game.shared.point import Point
from game.shared.color import Color

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        ships = cast.get_actors("ships")
        player_one = ships[0]
        player_two = ships[1]

        velocity1 = self._keyboard_service.get_direction('one')
        velocity2 = self._keyboard_service.get_direction('two')
        
        # player_one.icon_direction(velocity1)
        # player_two.icon_direction(velocity2)

        if not velocity1.equals(Point(0, 0)):
            player_one.set_direction(velocity1)
        if not velocity2.equals(Point(0, 0)):
            player_two.set_direction(velocity2)

        player_one.set_velocity(velocity1)        
        player_two.set_velocity(velocity2)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        if self._keyboard_service.is_shooting('one'):
            laser = Laser(player_one).shoot()
            cast.add_actor("lasers", laser)
            laser.move_next(max_x, max_y)
        if self._keyboard_service.is_shooting('two'):
            laser = Laser(player_two).shoot()
            cast.add_actor("lasers", laser)
            laser.move_next(max_x, max_y)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        ships = cast.get_actors("ships")
        player_one = ships[0]
        player_two = ships[1]

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player_one.move_next(max_x, max_y) 
        player_two.move_next(max_x, max_y)

        for laser in cast.get_actors('lasers'):
            laser.move_next(max_x, max_y)
            laser_position = laser.get_position()
            position1 = player_one.get_position()
            position2 = player_two.get_position()
            if laser_position.equals(position1):
                player_one.set_color(Color(255, 255, 255))
            if laser_position.equals(position2):
                player_two.set_color(Color(255, 255, 255))
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()