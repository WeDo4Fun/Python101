"""
Creating Loops using 'for'

We can create loops using 'while' where the loop runs indefinetely until boolean is wrong
"""

# -----------------
# Variables
# -----------------

correct_guess: bool = False  
choosen_number: int = 7

# -----------------------------------
# Option 1
# -----------------------------------

# while correct_guess is not True:
#     guess: int = int(input("Please guess my number (0 to 9)"))

#     if guess == choosen_number:
#         print(f"Correct, {guess} was correct guess!!")
#         correct_guess = True
#     else:
#         print(f"Sorry, {guess} was wrong guess.")

# -----------------------------------
# Option 2
# -----------------------------------

# Instead of a nominating a variable (i.e. 'correct_guess'), we can say "while True":

while True:
    guess: int = int(input("Please guess my number (0 to 9)"))

    if guess == choosen_number:
        print(f"Correct, {guess} was correct guess!!")
        break
    else:
        print(f"Sorry, {guess} was wrong guess.")
