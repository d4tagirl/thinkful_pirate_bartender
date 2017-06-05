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

def style_questioning (questions):
  preferences = {}
  for i in questions:
    choosing_style = input(questions[i])
    if choosing_style == 'y' or choosing_style == 'yes':
      preferences[i] = True
    else:
      preferences[i] = False
  return preferences

# preferences = style_questioning(questions)



import random

def recipe(preferences):
  drink = []
  for i in ingredients:
    if preferences[i] == True:
      drink.append(ingredients[i])
  return random.choice(drink)

# recipe(preferences)




def main(questions):
  preferences = style_questioning(questions)
  return recipe(preferences)

if __name__ == '__main__':
  print(main(questions))
