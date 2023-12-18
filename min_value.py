#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 18, 2023
# This program display the minimum of 10 values

import random
import constants


def min_value(list_of_int):
    min = 100
    # use a for loop when counter < ARRAY_SIZE
    for rand_num in list_of_int:
        # if list_of_counter[] is greater than min, make list_of_int_counter the min
        if rand_num < min:
            min = rand_num
    # return the min
    return min


def main():
    # set random_numbers to [] and min to 0
    random_numbers = []
    min = 0

    # tell the user what the program does
    print("This program display the minimum value of the following values :")

    # use a for loop when counter < ARRAY_SIZE
    for counter in range(0, constants.ARRAY_SIZE):
        # generate a random number
        rand_num = random.randint(constants.MIN, constants.MAX)

        # append random_numbers  to the random number
        random_numbers.append(rand_num)

        # display random_numbers[counter]
        print(random_numbers[counter])

    # call the min_value function
    min = min_value(random_numbers)

    # display the min value
    print("The min is {}.".format(min))


if __name__ == "__main__":
    main()
