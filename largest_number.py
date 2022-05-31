#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the largest number out of random numbers

import random


def largest_number(random_numbers):
    val1 = random_numbers[0]
    for loop_counter in range(10):
        if val1 < random_numbers[loop_counter]:
            val1 = random_numbers[loop_counter]

    return val1


def main():
    # this function creates the array

    random_numbers = []

    # process
    for loop_counter in range(10):
        number = random.randint(0, 100)
        random_numbers.append(number)
        print("Random number {0} is: {1}".format(loop_counter, number))
    print("")

    largest = largest_number(random_numbers)

    print("The largest number is {}".format(largest))


if __name__ == "__main__":
    main()
