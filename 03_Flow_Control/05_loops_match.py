""" 
'match' is a new operator introduced in Python 3.10
"""

# issue with matching str case!
# can be tackeld in 3 places: 

fav_color: str = input("Please enter your favorite color: ").lower()
# (1) fav_color = input("Please enter your favorite color: ").lower()

# (2) fav_color = fav_color.lower() 

match fav_color:
# (3) match fav_color.lower():
    case "blue":
        print("Blueberry")
    case "green":
        print("Celery")
    case "yellow":
        print("Lemon")
    case "orange":
        print("Orange")
    case "red":
        print("Strawberry")
    case _:     # this "_" means in case NO match!!
        print("No match")

