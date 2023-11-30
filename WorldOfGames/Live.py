def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
welcome(input("Please enter your name:"))

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    def game_number(gameChosen):
        if gameChosen > 3 or gameChosen == 0:
            print("Number should be in between 1-3, please try again.")
            gameChosen = int(input("enter the number again here:"))
            if gameChosen > 3 or gameChosen == 0:
                print("Number should be in between 1-3, please try again.")
                load_game()
        else:
            print(f"you choose game number {gameChosen}.")

    game_number(int(input("")))

    def game_diff(diffculityLevel):
        if diffculityLevel > 5 or diffculityLevel == 0:
            print("Number should be in between 1-5, please try again.")
            diffculityLevel = int(input("Please choose game difficulty from 1 to 5:"))
            if diffculityLevel > 5 or diffculityLevel == 0:
                print("Number should be in between 1=5, please try again.")
                game_diff(int(input("Please choose game difficulty from 1 to 5:")))
        else:
            print(f"you choose diffculity level {diffculityLevel}")

    game_diff(int(input("Please choose game difficulty from 1 to 5:")))

load_game()