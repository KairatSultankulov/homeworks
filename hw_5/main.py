from email.policy import default

from decouple import config
from logic import make_bet, is_game_over

def main():
    min_num = config("min_num", cast=int, default=1)
    max_num = config("max_num", cast=int, default=11)
    num_attempts = config("num_attempts", cast=int, default=10)
    start_capital = config("start_capital", cast=int, default=100)
    capital = start_capital

    print(f"Start capital: {capital}, attempts: {num_attempts}")

    while not is_game_over(num_attempts,capital):
        print(f"Enter your bet and number from {min_num} to {max_num}")

        try:
            player_capital, player_num = map(int, input().split())

            if player_capital > capital:
                print("You dont have enough money!")
                continue

            if player_capital <= 0 or player_num < min_num or player_num > max_num:
                print(f"Invalid bet! Bet must be positive, and number must be between {min_num} and {max_num}.")
                continue

        except ValueError:
            print("Invalid, only integers are accepted!")
            continue

        capital, won = make_bet(player_capital, player_num, capital, min_num, max_num)

        num_attempts -= 1

        print(f"Capital: {capital}, attempts: {num_attempts}")
        if won:
            print("You won!")
            print()

    print("Game over!")

if __name__ == "__main__":
    main()

