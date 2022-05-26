import random

class Word:
    """The word that's trying to be solved 
    
    The responsibility of Word is to generate the random word, and keep track of what has been solved and left unsolved.
    
    Attributes:
        _easy_list (List[str]): A list of possible easy words to choose from
        _medium_list (List[str]): A list of possible medium words to choose from
        _hard_list (List[str]): A list of possible hard words to choose from
        _hidden_word (str): The hidden portion of the word.
        _solved_word (str): The solved portion of the word.
        _difficulty (str): Which list to pick our word from
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """
        self._easy_list = 'daddy water baby sir mango juice road joy python brave song sky heart mouth life fish shoe school shop man dinner doctor car sun song sing serious moon educated sea water wind toe toy size'.split() # easy list of words
        self._medium_list = 'square death magnificent calculator famous marble petite aware paddle brave bushes waiting confess overjoyed shocking hushed hilarious female shame stimulating dinner doctor scribble heartbreaking rabid haunt arrive serious confused educated oafish nation sticky helpful reading recognise'.split() # medium list of words
        self._hard_list = 'floccinaucinihilipilification incomprehensibility trichotillomania xenotransplantation tergiversation uncopyrightable hippopotomonstrosesquippedaliophobia archetypal  circumlocution  worcestershire bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm heartbreaking boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt cycle disavow dizzying duplex dwarves embezzle equip espionage exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachts yippee yoked youthful yummy zigzag zilch zipper zodiac zombie'.split()
        
        #could draw from a txt document if we really care
        self._hidden = []
        self._solved =[]
        self._difficulty = ""
        

    def generate_word(self):
      """Picks a word from the list

      Args:
        self (Word): An instance of Word.
      """

      #method that generates a random word from the list
      # assign the guess list according to the level of difficulty
      if self._difficulty.lower() == "easy":
        choice = random.choice(self._easy_list)
      elif self._difficulty.lower() == "medium":
        choice = random.choice(self._medium_list)
      else:
        choice = random.choice(self._hard_list)

      #sets that as hidden_word
      #sets an empty array the length of hidden_word as solved_word
      self._hidden = list(choice)
      
      for _ in range(len(self._hidden)):
        self._solved.append("_")


      #random.choice(self._master_list)

    
    #method that takes a letter as an argument
      #if its in hidden_word, removes each of those letters that match and adds those letters to the correct spots on solved_word

