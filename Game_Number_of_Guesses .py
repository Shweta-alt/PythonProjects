

import random          # random inbuilt function that choose a random integer
import math           # math inbuilt function where all mathematical formulas are predefined


start = int(input("Enter the starting number of range"))

end = int(input("Enter the last number of range"))



# generate random number between the range given by user

x = random.randint(start,end)
print("\n \t You have only " , round(math.log(end - start +1 , 2)), " chances to guess the number! \n")

# Intialize integer to count total number of guesses
guesses = 0


# for calculation of minimum number of guesses depends upon range
while guesses < math.log(end - start + 1 , 2):
    guesses += 1

    guessed = int(input("Guess a number:-  "))

    if x == guessed:
        print("Congratulations you did it ! And Your total number of guesses are " ,guesses )

        break
    elif x > guessed :
        print("Oh you guessed too small number!")
    elif x < guessed:
        print("Oh you guessed too large number")


if guesses >= math.log(end - start + 1 , 2):
    print("\nThe number is %d" %x)
    print("\tBetter Luck Next time!")














