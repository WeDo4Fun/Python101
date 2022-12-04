""" 
We can use tripple quotes for formating as well as creating
strings. 
If used by itself it becomces comment without function similar
to lines starting with #
"""

# -------------------
# Variable Declration
# -------------------

my_variable1: str = "WeDo4Fun"
my_variable2: str = "Mehmet Ugur"
my_variable3: int = 159
my_variable4: float = 3.1415
my_variable5: bool = True
my_variable6: bool = False

# -------------------
# Print Alternative I
# -------------------

print(f"This educational Python series are brought to you by {my_variable1}.")
print(f"The typing and GitHub updates by {my_variable2} ")
print(f"An example for integer is {my_variable3}")
print(f"An example for float is {my_variable4}")
print(f"The first assigend boolian is {my_variable5}")
print(f"The second assigned boolian is {my_variable6}")
print(f"Using print function line by line makes it difficult to format the output in a niet way.")

# -------------------
# Print Alternative 2
# -------------------

combined_variable: str = f"""
This educational Python series are brought to you by {my_variable1}.
The typing and GitHub updates by                     {my_variable2} 
An example for integer is                            {my_variable3}
An example for float is                              {my_variable4}
The first assigend boolian is                        {my_variable5}
The second assigned boolian is                       {my_variable6}
This way, using a variable to combine all in make formating neater!
"""
print(combined_variable)

# -------------------
# Print Alternative 3
# -------------------

# We can also use print function without allocating all text into a string varibale;

print(f"""
This educational Python series are brought to you by {my_variable1}.
The typing and GitHub updates by                     {my_variable2} 
An example for integer is                            {my_variable3}
An example for float is                              {my_variable4}
The first assigend boolian is                        {my_variable5}
The second assigned boolian is                       {my_variable6}
This way, using a variable to combine all in make formating neater!
""")
