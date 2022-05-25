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
        self._win = True
        self._terminal_service = TerminalService()
        self._parachute = Parachute()
        self._guess = ""

        self._word = Word()
        self._word._difficulty = input("Choose your difficulty: [easy/hard]")
        while self._word._difficulty not in ["easy", "hard"]:
            self._word._difficulty = input("Choose your difficulty: [easy/hard]")

        self._word.generate_word()
        
        

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        for i in self._word._solved:
            print(f"{i} ", end = "") 

        if self._win == True:
            print("\n\nCongratulations! You win!")
        else:
            print("\n\nYou lose!")

    def _get_inputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """


        
        print(self._word._hidden)#comment these out
        for i in self._word._solved:
            print(f"{i} ", end = "")  
    

        #get input from user
        #input validation [only letters a-z]

        self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        while not (self._guess.isalpha()) or (len(self._guess) != 1):
            self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        
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
            #adds to the lose counter

        if self._guess in self._word._hidden:
            for i in self._word._hidden:
                if i == self._guess:
                   index = self._word._hidden.index(i)
                   self._word._solved[index] = i
                   self._word._hidden[index] = ""
        else:
                #CHANGE THIS TO FIT SYNTAX
            self._parachute._drawing.pop(0)
            self._parachute._counter += 1

        pass

    def _do_outputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """

        #print out the current state of the parachute

        #print out the current solved portion of the word.

            #CHANGE THIS TO FIT SYNTAX
        for i in self._parachute._drawing:
            print(i)

        #Check to see if we lost or won the game

            #check to see if the word is solved by checking word.hidden for letters
        self._is_playing = False
        for i in self._word._hidden:
            if i != "":
                self._is_playing = True

            #check to see if we ran out of parachute
        if self._is_playing == True:
            if self._parachute._counter == self._parachute._death:
                self._is_playing = False
                self._win = False

        pass
