import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    print()

    # Variables

    my_position = 0
    natives_position = -10
    thirst = 0
    camel_tiredness = 0
    drinks_canteen = 3

    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()

        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            print("You quitter.")
            done = True
            if random.randrange(1, 21) == 3:
                print("You found an oasis! Your canteen has been refilled.")
                drinks_canteen = 3

        elif user_choice.upper() == "E":
            print("Miles traveled: ", my_position)
            print("Drinks in canteen: ", drinks_canteen)
            print("The natives are", my_position - natives_position, "miles behind you")

        elif user_choice.upper() == "D":
            print("Your camel is happy!")
            natives_position += random.randrange(7, 15)
            camel_tiredness = 0

        elif user_choice.upper() == "C":
            my_position += random.randrange(10, 21)
            print("You traveled", my_position, "miles!")
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives_position += random.randrange(7, 15)
            if random.randrange(1, 21) == 3:
                print("You found an oasis! Your canteen has been refilled.")
                drinks_canteen = 3

        elif user_choice.upper() == "B":
            my_position += random.randrange(5, 12)
            print("You traveled", my_position, "miles!")
            thirst += 1
            camel_tiredness += 1
            natives_position += random.randrange(7, 15)
            if random.randrange(1, 21) == 3:
                print("You found an oasis! Your canteen has been refilled.")
                drinks_canteen = 3

        elif user_choice.upper() == "A":
            if drinks_canteen >= 1:
                drinks_canteen -= 1
                thirst = 0

            elif drinks_canteen <= 0:
                print("You have no drinks left!")

        if thirst > 6:
            print("You died of thirst!")
            done = True

        elif thirst > 4 and not done:
            print("You are thirsty.")

        if camel_tiredness > 8:
            print("Your camel is dead!")
            print("You got lost in the desert.")
            done = True

        elif camel_tiredness > 5 and not done:
            print("Your camel is getting tired.")

        if natives_position >= my_position:
            print("The natives caught you! You are dead.")
            done = True

        elif my_position - natives_position < 15 and not done:
            print("The natives are getting close!")

        if my_position >= 200:
            print("You won!")
            done = True


main()
