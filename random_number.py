import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
    
        if guess < random_number:
            print("guess again. too low")
        elif guess > random_number:
            print("guess again. too high")

    print(f"Congrats, you got the number, which was {random_number}.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    
    while feedback != 'c':
        # Computers guess
        if low != high:
            guess = int(random.randint(low, high))
        else:
            guess = low # can also be high

        # Provide feedback
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??\n').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    
    print(f"The computer guessed the number {guess} correctly!")

    
# guess(10)
val = random.randint(1,5000)
print(f'the value is {val}')
computer_guess(val)