from game.terminal_service import TerminalService

class Parachute:
    """The parachute that's tracking how close to losing the player is. 
    
    The responsibility of parachute is to keep track of how many incorrect guesses the player has made, and print out the current diagram of the player and their parachute after each guess
    
    Attributes:
        
    """

    def __init__(self):
        """Constructs a new parachute.

        Args:
            self (parachute): An instance of parachute.
        """
        self._drawing = ["  _____", " /_____\\", " \     /", "  \   /", "   \ /", "    0", "   /|\\", "   / \\", "", "^^^^^^^^^^"]
        self._counter = 0
        self._death = 5



    
      
    
    
