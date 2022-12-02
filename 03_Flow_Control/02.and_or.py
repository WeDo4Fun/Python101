"""
Expanding if / elif / else with and/or
"""
my_int_variable: int = 20
my_str_variable: str = "String"

# --------------------------------
# And / Or Statements
# --------------------------------

if my_int_variable == 20 and my_str_variable == "String":
    print("Both conditions are met")
elif my_int_variable < 20 or my_str_variable == "String":
    print("One of the conditions are met")

time_on_video: str = "1:06:22"
