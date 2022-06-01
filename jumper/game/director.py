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
        win (boolean): Have we lost or won the game?
        terminal_service: For getting and displaying information on the terminal.
        parachute: An instance of Parachute Class
        word: An instance of the Word Class
        solved: the solved portion of the word.
        hidden: the hidden portion of the word.
        guess: The current guessed letter
        final_answer: the originally chosen word, in full.
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
        self._final_answer = ""
        self._hidden = ""
        self._solved = ""

        self._opening_moves()
        
    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        for i in self._solved:
            print(f"{i} ", end = "") 

        if self._win == True:
            print("\n\nCongratulations! You win!")
        else:
            print("\n\nSorry! You lose!")
        self._word.reveal_answer()


    def _get_inputs(self):
        """Receives the new guessed letter from the user

        Args:
            self (Director): An instance of Director.
        """

        # Print hidden word
        #print(self._word._hidden) #comment this out

        for i in self._solved:
            print(f"{i} ", end = "")  

        #get input from user
        #input validation [only letters a-z]

        self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        while not (self._guess.isalpha()) or (len(self._guess) != 1):
            #print("Invalid entry!")
            self._terminal_service.write_text("Invalid entry!") # print an error message
            self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        pass


    def _do_updates(self):
        """Check the guessed letter, update the word, update the parachute

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

        if self._guess in self._hidden:
            for i in self._hidden:
                if i == self._guess:
                   index = self._hidden.index(i)
                   self._solved[index] = i
                   self._hidden[index] = ""
        else:
            self._parachute._drawing.pop(0)
            self._parachute._counter += 1
        pass

    def _do_outputs(self):
        """Prints the current state of the parachute, and checks to see if we've won or lost the game

        Args:
            self (Director): An instance of Director.
        """

        #Check to see if we lost or won the game

            #check to see if the word is solved by checking word.hidden for letters
        self._is_playing = False
        for i in self._hidden:
            if i != "":
                self._is_playing = True

            #check to see if we ran out of parachute
        if self._is_playing == True:
            if self._parachute._counter == self._parachute._death:
                self._parachute._dead_head()
                self._is_playing = False
                self._win = False

        #print out the current state of the parachute
        self._parachute._print_parachute()

        pass


    def _opening_moves(self):
        """Prints opening speil and gets difficulty

        Args:
            self (Director): An instance of Director.
        """

        self._terminal_service.welcome_text() # print the welcome text using the terminal_service class

        #create the word to be guessed
        self._word._generate_word()
        self._hidden = self._word.get_hidden()
        self._solved = self._word.get_solved()