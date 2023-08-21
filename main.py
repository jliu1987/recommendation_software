from list import *
from greeting import *

greeting()

my_food_list=types
my_restaurant_list=[]

selected_food_type=''

# Write code for user interaction here
while len(selected_food_type) == 0:
    user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here.\n")).lower()
    print("Your selected food type is: "+ user_input)
    selected_food_type=user_input


# Search for user_input in food types data structure here
matching_types = []
for type in my_food_list:
    if type.startswith(user_input):
        matching_types.append(type)


# print list of matching food types
for type in matching_types:
    print(type)

# Check if only one type of restaurant was found, ask user if they would like to select this type
if len(matching_types) == 1:
    select_type = str(input(
        "\nThe only matching type for the specified input is " + matching_types[0] + ". \nDo you want to look at " +
        matching_types[0] + " restaurants? Enter y for yes and n for no\n")).lower()

    # After finding food type write code for retrieving restaurant data here
    if select_type == 'y':
        selected_food_type = matching_types[0]
        print("Selected Food Type: " + selected_food_type)
        my_restaurant_list=list[selected_food_type]
        while my_restaurant_list is not None:
           for restaurant in my_restaurant_list:
                    print("--------------------------")
                    print("Name: " + restaurant[1])
                    print("Price: " + restaurant[2] + "/5")
                    print("Rating: " + restaurant[3] + "/5")
                    print("Address: " + restaurant[4])
                    print("--------------------------\n")

        # Ask user if they would like to search for other types of restaurants
        repeat_loop = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
        if repeat_loop == 'y':
            selected_food_type = ""