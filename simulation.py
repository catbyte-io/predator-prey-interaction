import sys
import random
import math


def main():
    # initialize a list to similate the pool of other predators, prey, and producers
    pool = []

    # set number of draws
    draws = 20

    # ask how many generations and cast to an integer
    rounds = input("How many generations?: ")
    rounds = int(rounds)

    # ask how many producers, prey, and predators
    producers = input("How many producers?: ")
    prey = input("How many prey?: ")
    other_predator = input("How many other predators?: ")

    # For the number of each chosen, add them that many times to the list
    for i in range(int(producers)):
        pool.append("producer")

    for j in range(int(prey)):
        pool.append("prey")

    for k in range(int(other_predator)):
        pool.append("other_predator")

    # track generations
    generation = 1

    while generation <= rounds:
        # ititialize producers/prey/predators drawn at 0
        num_producers = 0
        num_prey = 0
        num_predator = 0

        # set count equal to draws so it loops to draw from the pool that number of times
        count = draws

        while count > 0:
            # randomly draw from the habitat pool
            choice = random.choice(pool)

            # count draws
            if choice == 'producer':
                num_producers += 1
            elif choice == 'prey':
                num_prey += 1
            else:
                num_predator += 1

            # iterate
            count -= 1

        # print results
        print(f"\nGeneration: {generation}\nMain Predator: {
              draws}\nHabitat/Producers: {num_producers}\nPrey: {num_prey}\nOther Predator: {num_predator}")

        # increment generation
        generation += 1

        # calculate draws (round down)
        draws += math.floor(num_prey / 2)
        draws -= math.floor(num_producers / 3)
        draws -= num_predator

        # remove 1 if draws is not even
        if draws % 2 != 0:
            draws -= 1

    # exit program
    sys.exit()


main()
