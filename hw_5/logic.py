import random

def make_bet(player_capital, player_number, capital, min_num, max_num):
    number_to_guess = random.randint(min_num, max_num)
    if player_number == number_to_guess:
        capital += player_capital
        return capital, True
    else:
        capital -= player_capital
        return capital, False

def is_game_over(num_attempts, capital):
    return num_attempts <= 0 or capital <= 0
