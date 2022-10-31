# Guess the number 
import random # when we call random it calls the package random that comes with python and makes the function of this package accesible to us

# User guess
# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0

#     while (guess!= random_number):
#         guess = int(input(f"Enter your guess between 1 and {x}: "))
#         print(guess)
#         if guess > random_number:
#             print("Lower number please :>")
#         elif guess < random_number:
#             print("higher number please")

#     print(f"You guessed the number! The number was {random_number}.")
    

# guess(100)

# Computer guess
def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if  low != high:
            guess = random.randint(low , high)
        else :
            guess = low  # coud also be high as low == high
        feedback  = input (f'Is {guess} too high (H), too low (L) or correct(C) ? ').lower()
        if feedback == 'h':
            high = guess  - 1
        elif feedback == 'l':
            low = guess  + 1
    print(f"The computer guessed the number {guess} :> ")

comp_guess(100)






