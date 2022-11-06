# ----------------------------
# Bug refers to a coding error
# ----------------------------

box = "balloons"

print(f"Box contain: {box}")

box = 99

print (f"Box contains: {box}")

#-------------------------------------------------------------------
# Type Hinting - Optinal Static Type Checking in Python Using 'Mypy'
#-------------------------------------------------------------------

food = "Coke"
food: str = "Coke"  # we can use as line above but if we add "": str" we assign the food variable to be only a string!! 

print(f"John likes drinking {food}")

food = "Eggs"

print(f"John is going to eat {food}")

# now if we try to assign a non string virabale to 'food' we will get an error.. 

food = False        # this is a bug.. 'False' is not somethign edible!
                    # so, food, once declared a 'str' shoud not take a boolean 
                    # value! is we install mypy in code here it should RED 
                    # udenrline it! 

print(f"John thinks he made a {food} comment")
