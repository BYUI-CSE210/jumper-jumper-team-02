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
        self.leedle = ""


    def something(self):
      self.leedle = ""
    
    
    # def print_parachute(self):
    #     """print parachute picture string"""

    #     self._terminal_service.write_text(self, self.parachute)

