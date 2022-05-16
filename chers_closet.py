# Depencies
import random

# Lists
tops = [
    "brown and white selburose vest with a blue button down shirt",
    "yellow and dark green plaid jacket",
    "white blazer with with gold embroidered trim",
    "yellow cashmere cardigan",
    "blue chiffon chemise with white lapels and cuffs",
    "black and silver striped jacket with a white button down shirt"
]

bottoms = [
    "black mini skirt",
    "red and black plaid mini skirt",
    "yellow and dark green plaid mini skirt",
    "brown corduroy mini skirt with white buttons down the front",
    "two-tone white and black skirt",
    "grey diamond patterned mini skirt"
]

shoes = [
    "red kitten heels",
    "burnt orange heels",
    "black wedges",
    "burnt orange flats",
    "white thigh high boots",
    "silver mary janes"
]

accessories = [
    "red clutch",
    "burgundy headband",
    "white feather backpack",
    "black beret",
    "double golden cross necklace",
    "white thigh high socks",
]

# Variables
random_top = random.choice(tops)
random_bottom = random.choice(bottoms)
random_shoes = random.choice(shoes)
random_accessory = random.choice(accessories)

# Print Statement
print(f"Good morning, Cher.  Today, try out a {random_top}, a {random_bottom}, with {random_shoes} and a {random_accessory} to finish the look.")