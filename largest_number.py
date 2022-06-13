#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the largest number out of random numbers

import random


def largest_number(random_numbers, amount_of_numbers):
    maximum = random_numbers[0]
    for loop_counter in range(amount_of_numbers):
        if maximum < random_numbers[loop_counter]:
            maximum = random_numbers[loop_counter]

    return maximum


def main():
    # this function creates the array
    amount_of_numbers = 10

    random_numbers = []

    # process
    for loop_counter in range(amount_of_numbers):
        number = random.randint(0, 100)
        random_numbers.append(number)
        print("Random number {0} is: {1}".format(loop_counter + 1, number))
    print("")

    largest = largest_number(random_numbers, amount_of_numbers)

    print("The largest number is {}".format(largest))


if __name__ == "__main__":
    main()
