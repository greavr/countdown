import random
from enum import Enum
import json, os
import player

class game:
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """

    class number_type(Enum):
        big = 1
        little = 2

    class character_type(Enum):
        vowel = 1
        consonant = 2

    def __init__(self, players: player.player = [], seed: int = None,):
        # Setup game random seed
        if seed:
            self.random_seed = seed
        else:
            self.random_seed = random.randint(100,200000)

        random.seed(self.random_seed)

        # Class Variables
        self.players = players
        self.vowels = ["a","e","i","o","u"]
        self.consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
        self.big_numbers = [25,50,75,100]
        self.available_big_numbers = self.big_numbers
        self.little_numbers = [1,2,3,4,5,6,7,8,9,10]
        self.current_letters = []
        self.current_numbers = []
        self.target_number = None
        self.anagrams = {}
        self.current_anagram = {}
        self.max_characters = 9
        self.max_numbers = 6
        self.anagrams_guesses = []

        # Seed the random
        self.id = random.randint(1, 1000)
        # Load Anagrams
        self.load_anagrams()
    
    def get_random_char(self, character_type: character_type):
        # Validate Length of letters
        if len(self.current_letters) >= self.max_characters:
            return None
        
        # Choose from word list
        choosen = None
        if character_type == character_type.vowel:
            choosen = random.choice(self.vowels)
        else:
            choosen = random.choice(self.consonants)
        
        self.current_letters.append(choosen)

        return choosen

    def get_random_int(self, number_type: number_type):
        # Validate Length of Numbers
        if len(self.current_numbers) >= self.max_numbers:
            return None

        # Return valid number
        choosen = None
        if number_type == number_type.big:
            # Check big numbers left
            if len(self.available_big_numbers) > 0:
                choosen = random.choice(self.available_big_numbers)
                # Big numbers can only come out once per game
                self.available_big_numbers.remove(choosen)
                self.current_numbers.append(choosen)
        else:
            choosen = random.choice(self.little_numbers)
            self.current_numbers.append(choosen)

        # If got all numbers generate random number
        if len(self.current_numbers) == self.max_numbers:
            self.get_random_target()

        return choosen

    def get_random_target(self):
        self.target_number = random.randint(100,999)
        return self.target_number

    def end_Round(self):
        # Reset the values
        self.current_letters = []
        self.available_big_numbers = self.big_numbers
        self.current_numbers = []
        self.target_number = None
        self.current_anagram = {}

    def calc_points(self):
        # Count Points for each player
        for aPlayer in self.players:
            this_round_points = len(aPlayer.LongestGuess())
            aPlayer.ScorePoints(points=this_round_points)
            print(f"Player: {aPlayer.name} Scored: {this_round_points}, Total Points: {aPlayer.score}")

    def load_anagrams(self):
        # Load anagrams from file
        ## Default to local file if not environment file
        ## If file error use one default
        json_path = os.getenv("anagram_path",os.path.join(os.path.dirname(__file__),"anagrams.json"))
        print(f"Loading Angrams from File: {json_path}")

        # Check file exists 
        if os.path.exists(json_path):
            print(f"Anagrams file found: {json_path}")
            # Happy Path
            f = open(json_path)
            self.anagrams = json.load(f)
            f.close()
        else:
            # Default value
            self.anagrams = [{"hint": "My favourite way to relax", "puzzle": "IDLEPOOS", "solution":"POOLSIDE"}]

    def guess_anagram(self,guess_word: str, guess_player: player):
        # Guess word
        ## Log Guess
        self.anagrams_guesses.append([guess_word.lower(),guess_player.name])

        # Correct
        if guess_word.lower() == self.current_anagram["solution"].lower():
            guess_player.score += 10
            return True
        else:
            return False

    def get_angram(self):
        # Get random anagram from available list
        random_index = random.randint(0, len(self.anagrams)-1)
        self.current_anagram = self.anagrams[random_index]
        return self.current_anagram