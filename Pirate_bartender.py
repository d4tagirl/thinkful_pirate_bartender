questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def style_questioning (questions, style_choice = {}):
    for i in questions:
        choosing_style = input(questions[i])
        if choosing_style == 'y' or choosing_style == 'yes':
            style_choice[i] = True
        else:
            style_choice[i] = False
    return style_choice

style_questioning(questions)

# Write a function to construct a drink
# The function should take the preferences dictionary created in the first function as a parameter. Inside the function you should create an empty list to represent the drink. For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink. Finally the function should return the drink.
#
# To choose an ingredient from one of the ingredient lists you can use the random.choice function. This selects a random item from a list, for example:
#
# import random
#
# beatles = ["John", "Paul", "George", "Ringo"]
# # Print the name of a random Beatle
# print(random.choice(beatles))
