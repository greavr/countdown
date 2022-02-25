from game import game
from player import player
import random

player_rick = player(name="rick")
player_ping = player(name="ping")

player_list = [player_ping,player_rick]

this_game = game(players=player_list)

while len(this_game.current_letters) < this_game.max_characters:
    this_game.get_random_char(character_type=random.choice(list(this_game.character_type)))

print(f"Letters: {this_game.current_letters}")

player_rick.GuessWord(guess_word=input(f"Enter {player_rick.name} Word: "),letters=this_game.current_letters[:])
player_ping.GuessWord(guess_word=input(f"Enter {player_ping.name} Word: "),letters=this_game.current_letters[:])

this_game.calc_points()

this_game.end_Round()

while len(this_game.current_numbers) < this_game.max_numbers:
    this_game.get_random_int(number_type=this_game.number_type.big)
    this_game.get_random_int(number_type=this_game.number_type.little)
    this_game.get_random_int(number_type=this_game.number_type.little)

print(f"Numbers: {this_game.current_numbers}")
print(f"Target Number: {this_game.target_number}")

this_game.end_Round()

this_game.get_angram()
print(f"Hint: {this_game.current_anagram['hint']}, Puzzle: {this_game.current_anagram['puzzle']}")

found = False
while not found:
    found = this_game.guess_anagram(guess_word=input(f"Enter {player_rick.name} Word: "),guess_player=player_rick)

this_game.calc_points()