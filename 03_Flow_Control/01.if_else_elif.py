""" 
Simple file for introduction of IF ELSE ELIF
"""

my_variable: int = 18

# --------------------------------
# If / Else Statements
# --------------------------------

if my_variable < 18:
    print("Your variable is less than 18")
else:
    print("Your variable is more than 18")

# if we re-asign a value to the variable: 

my_variable = 15

# and re-write same code woth print functuion. Here we as an example
# we will also remove "else" block - should still work properly but 
# remember to pull the next line one Tab back!

if my_variable < 18:
    print("Your variable is less than 18")

print("Your variable is more than 18")

# --------------------------------
# ELIF
# --------------------------------


if my_variable < 18:
    print("Your variable is less than 18")

elif my_variable >= 40:
    print("Your varible is too big of a number.")
else: 
    print("Your variable is more than 18")
