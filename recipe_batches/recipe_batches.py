#!/usr/bin/python

import math





def recipe_batches(recipe, ingredients):

  batches = 0
  toggle = True

  if recipe.keys() == ingredients.keys():

    while toggle:

      for i in ingredients.values():
        print('------')
        print(i, 'remaining ing values')
        print('------')
        if i < 0:
          toggle = False

      ingredients = {key: ingredients[key] - recipe.get(key, 0) for key in ingredients.keys()}
      batches += 1
      print('=======')
      print(ingredients, 'ingredients remaining')
      print(batches, 'batches')
      print('=======')

    return batches - 2

  else:
    return 0



print(recipe_batches({'milk': 5, 'eggs': 2, 'sugar': 2}, {'milk': 12, 'eggs': 6, 'sugar': 10}))

















# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))