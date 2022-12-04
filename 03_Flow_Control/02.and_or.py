"""
Expanding if / elif / else with and/or
"""

inp_number: int = int(input("Please enter a number between 0-30: "))
inp_string: str = input("Please choose a color Reg / Green / Blue (R/G/B): ")
color_choice=""

# --------------------------------
# And / Or Statements
# --------------------------------

if inp_string.lower() == "r":
    color_choice="RED"
elif inp_string.lower() == "g":
    color_choice = "GREEN"
elif inp_string.lower == "b":
    color_choice = "BLUE"
elif inp_string.lower != "r" or "g" or "b":
    color_choice = ("Unknown")

if inp_number == 20:
    print(f"Your number is 20, color is {color_choice}")
elif inp_number < 20 and inp_number >= 0:
    print(f"Your number is smaller than 20, color is {color_choice}")
elif inp_number > 20 and inp_number < 30:
    print(f"Your number is bigger than 20, color is {color_choice}")
else:
    print (f"the number you chose is in not betwen 0 and 30!, color is {color_choice}.")
# time_on_video: str = "1:06:22"