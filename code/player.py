import game

class player:
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """

    def __init__(self, name: str, game_id: game):
        self.name = name
        self.current_wordlist = []
        self.bad_wordlist = []
        self.game = game_id
        self.score = 0

    def GuessWord(self, guess_word: str):
        # Validate word
        if self.game.Validate_word(guess_word=guess_word, guess_player=self):
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
