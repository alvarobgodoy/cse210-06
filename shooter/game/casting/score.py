from game.casting.actor import Actor

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()

    def set_controls(self, controls):
        """Adds the given controls to the text.
        
        Args:
            points (int): The points to add.
        """
        text = self.get_text()
        self.set_text(f"{text} {controls}")