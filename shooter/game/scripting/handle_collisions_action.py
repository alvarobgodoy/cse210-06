import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ''

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, False)
        else:
            self._handle_game_over(cast, True)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # Get snakes list
        snakes = cast.get_actors('snakes')

        # Assign the 2 snakes to variables
        snake1 = snakes[0]
        snake2 = snakes[1]

        # Get their heads
        snake1_head = snake1.get_segments()[0]
        snake2_head = snake2.get_segments()[0]

        # Get their segments
        snake1_segments = snake1.get_segments()[1:]
        snake2_segments = snake2.get_segments()[1:]
        
        # Check for collision with itself, snake 1
        for segment in snake1_segments:
            if snake1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 'Player two'
                
            # Collision with the opponent 
            for segment2 in snake2_segments:
                if snake1_head.get_position().equals(segment2.get_position()):
                    self._is_game_over = True
                    self._winner = 'Player two'

        # Check for collision with itself, snake 2
        for segment in snake2_segments:
            if snake2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 'Player one'
            # Collision with the opponent 
            for segment1 in snake1_segments:
                if snake2_head.get_position().equals(segment1.get_position()):
                    self._is_game_over = True
                    self._winner = 'Player one'
                
        

    def _handle_game_over(self, cast, already_over):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            # Get snakes list
            snakes = cast.get_actors("snakes")

            # Get their segments
            snake1_segments = snakes[0].get_segments()
            snake2_segments = snakes[1].get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()

            # Snake 1
            for segment in snake1_segments:
                segment.set_color(constants.WHITE)
                
            # Snake 2
            for segment in snake2_segments:
                segment.set_color(constants.WHITE)
            
            if not already_over:
                # Set different colors for the final message 
                if self._winner == 'Player one':
                    message.set_color(constants.RED)
                else: 
                    message.set_color(constants.GREEN)

                message.set_text(f"Game Over! {self._winner} won!")
                message.set_position(position)
                cast.add_actor("messages", message)