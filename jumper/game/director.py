from game.terminal_service import TerminalService
from game.word import Word
from game.parachute import Parachute

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
        word: The word being played.
        guess: The current guessed letter
    """
        #the word being guessed

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._word = Word()
        self._word.generate_word()
        self._guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """

        print(self._word._hidden)#comment this out
        print(self._word._solved)#keep this  

        #get input from user
        #input validation [only letters a-z]

        self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        while not (self._guess.isalpha()) or (len(self._guess) != 1):
            self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        #print("Good")#comment out
        
        pass


    def _do_updates(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """

        #check the letter against the characters in the word.

        #if letter in word:
            #add letter to the solved portion of the word
            #remove letter from the array of the hidden word
        #else:
            #remove a line from the parachute



        if self._guess in self._word._hidden:
            for i in self._word._hidden:
                if i == self._guess:
                   index = self._word._hidden.index(i)
                   self._word._solved[index] = i
                   self._word._hidden[index] = ""
        #else:
            
            #remove a line from the parachute



        

        pass

    def _do_outputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """

        #print out the current state of the parachute

        #print out the current solved portion of the word.

        pass
