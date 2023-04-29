import random

def food_choice(**args):
    choice =random.choice(list(args.keys()))
    print(f"WHAT YOU WILL EAT TODAY {args[choice]}")

food_choice(a ="Alo Gobhi" , b="Shawarma" , c="Briyani" ,d="Pizza" ,e="Burger" , f="Bread Omlet" ,g="Choclate Sandwich" ,h="Andakadhi" ,i="Dal Chawal" ,j="Pavbhaji" ,k=" Spicy Chicken " ,l="KadhiChawal" , m="Pulav" , n="Fruit Salad" )