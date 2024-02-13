import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # Remove after testing
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))
index = 0

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("You got it right!")
        break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    elif guess == 0:
        print("Quitting game, goodbye!")
        break
    else:
        print("Invalid input, please input an int between 1 and 10")
        exit(1)
    index += 1

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

