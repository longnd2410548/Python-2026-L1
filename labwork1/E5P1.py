color_list = ["blue", "yellow", "orange", "red", "purple"]

favorite_color = input("What is your favorite color? ")

if favorite_color in color_list:
    index = color_list.index(favorite_color)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")