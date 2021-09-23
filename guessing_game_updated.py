#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to guess a number between 0 - 9

import random


def main():
    # this tells the user if they picked the right number

    # input
    number_as_string = input("Enter a number between 0 - 9 : ")
    random_as_number = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    try:
        integer_as_number = int(number_as_string)

        if random_as_number == number_as_string:
            print("You guessed the number correctly!")

        else:
            print("You guessed the number incorrectly :(")

    except Exception:
        print("This is not a number!")

    finally:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
