import random

def guess_street_game():
    print("Welcome to the Guess Street Game!")
    print("Left street = 0, Right street = 1")
    start = input("Click 'S' to start the game: ")

    if start.lower() == 's':
        for round in range(1, 11):
            print(f"Round {round}: 0 or 1")
            correct_choice = random.randint(0,1)
            user_choice = int(input("Which way do you want: "))

            if user_choice == correct_choice:
                print("That's right 💯")
            elif user_choice != correct_choice:
                print("You lost 😞")
                break
        else:print("Congratulations! You completed all 10 rounds successfully you win 👏🏻!")
    else:
        print("You did not start the game. You lost 😞")

guess_street_game()