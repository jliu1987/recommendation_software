from restaurantData import *

list={}

for type in types:
    list[type]=[]
    for restaurant in restaurant_data:
        if restaurant[0]==type:
            list[type].append(restaurant)

