from english_words import english_words_lower_alpha_set

class player:
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """

    def __init__(self, name: str):
        self.name = name
        self.current_wordlist = []
        self.bad_wordlist = []
        self.score = 0

    def Validate_word(self, word: str, letters: str):
        # Validate user input word
        ## Validate it is a word
        result = True
        isWord = word.lower() in english_words_lower_alpha_set

        # Validate word uses letters found
        if isWord:
            # Create list of letters
            self.choosen_letters = letters
            # Itterate over the word
            for aLetter in word.lower():
                if aLetter in self.choosen_letters:
                    self.choosen_letters.remove(aLetter)
                else:   
                    return False
        else:
            print("Not a valid word")
            return False

        print(f"Is Valid: {result}")
        return result

    def GuessWord(self, guess_word: str, letters: str):
        # Validate word
        if self.Validate_word(word=guess_word,letters=letters):
            self.current_wordlist.append(guess_word)
            return True
        else:
            self.bad_wordlist.append(guess_word)
            return False

    def ScorePoints(self, points: int = 0):
        self.score += points;
        self.current_wordlist = []

    def LongestGuess(self):
        if len(self.current_wordlist) == 0:
            return ""
        else:
            return max(self.current_wordlist, key=len)

    def NextRound(self):
        self.score = 0
        self.current_wordlist = []
