import random

class Word:
    """The word that's trying to be solved 
    
    The responsibility of Word is to generate the random word, and keep track of what has been solved and left unsolved.
    
    Attributes:
        _master_list (List[str]): A list of possible words to choose from
        _hidden_word (str): The hidden portion of the word.
        _solved_word (str): The solved portion of the word.
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """
        self._master_list = 'wipe square death magnificent calculator famous marble petite aware paddle brave zoo tan bushes fine huge waiting confess overjoyed shocking picayune hushed hilarious female shame stimulating bore dinner doctor obsequious corn scribble pump year heartbreaking rabid haunt arrive serious confused loud educated pack oafish nation shy sticky helpful reading recognise'.split() #come up with list of words
        #could draw from a txt document if we really care
        self._hidden = []
        self._solved =[]
        

    def generate_word(self):
      """Picks a word from the list

      Args:
        self (Word): An instance of Word.
      """

      choice = random.choice(self._master_list)
      self._hidden = list(choice)
      for _ in range(len(self._hidden)):
        self._solved.append("_")

    #method that generates a random word from the list
      #sets that as hidden_word
      #sets an empty array the length of hidden_word as solved_word


      #random.choice(self._master_list)

    
    #method that takes a letter as an argument
      #if its in hidden_word, removes each of those letters that match and adds those letters to the correct spots on solved_word