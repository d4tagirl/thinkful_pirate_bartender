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

import random

# ASK QUESTION

def style_questioning (questions):
  preferences = {}
  for i in questions:
    choosing_style = input(questions[i])
    if choosing_style == 'y' or choosing_style == 'yes':
      preferences[i] = True
    else:
      preferences[i] = False
  return preferences

# style_questioning(questions)



# FIND RECIPE


def recipe(preferences):
  drink = []
  for i in ingredients:
    if preferences[i] == True:
      drink.append(ingredients[i])
  return random.choice(drink)

# recipe(preferences)



# MAIN FUNCTION - only 1 drink
#
# def main(questions):
#   preferences = style_questioning(questions)
#   return recipe(preferences)
#
# if __name__ == '__main__':
#   print(main(questions))

# # MAIN FUNCTION - with more than 1 recipe
# def main(questions):
#   preferences = style_questioning(questions)
#   while True:
#     other_drink = input("Would you like another drink? ")
#     if other_drink == 'y' or other_drink == 'yes':
#       next_drink = recipe(preferences)
#       print(next_drink)
#     else:
#       break
#
# if __name__ == '__main__':
#   print(main(questions))


# # MAIN FUNCTION - with more than 1 recipe and name of client
# def main(questions):
#   customers_preferences = {}
#   while True:
#     customer = input("What is your name? ")
#     if customer in customers_preferences:
#       preferences = customers_preferences[customer]
#     else:
#       preferences = style_questioning(questions)
#       customers_preferences[customer] = preferences
#     print(recipe(preferences))
#     #
#     # while True:
#     #   other_drink = input("Would you like another drink? ")
#     #   if other_drink == 'y' or other_drink == 'yes':
#     #     next_drink = recipe(preferences)
#     #     print(next_drink)
#     #   else:
#     #     print("See you next time " + customer + "!")
#     #     break

# Stock control:
# You could add a stock count for each ingredient which decreases whenever the bartender makes a drink.
# The bartender could restock the ingredients when supplies are low.

# create stock
stock_count = {}
for i in ingredients:
  for j in ingredients[i]:
    stock_count[j] = random.randint(3, 10)


# MAIN FUNCTION - with stock control
def main(questions):
  customers_preferences = {}
  while True:
    customer = input("What is your name? ")
    if customer in customers_preferences:
      preferences = customers_preferences[customer]
    else:
      preferences = style_questioning(questions)
      customers_preferences[customer] = preferences
    printed_recipe = recipe(preferences)
    print(printed_recipe)
    for i in printed_recipe:
      stock_count[i] = stock_count[i] - 1
      if stock_count[i] < 3 :
        print("we are running out of " + i + ", we only have " + str(stock_count[i]))

if __name__ == '__main__':
  main(questions)


NAMING DRINK

def naming_drink(ingredients):
  adjectives = ["brave", "calm", "delightful", "eager", "gentle", "happy"]
  nouns = ["cat", "sock", "ship", "hero", "monkey", "match"]
  name_drink = {}
  for i in ingredients:
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    adjectives.remove(adj)
    nouns.remove(noun)
    name_drink[i] = '%s %s' % (adj, noun)
  print(name_drink)

naming_drink(ingredients)
  


