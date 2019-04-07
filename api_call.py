import requests


def ingredient_search(ingredient_name):
    key = "3caf4c461472986be1f4344d71103e2b&"

    url = 'https://www.food2fork.com/api/search?key={}q={}'.format(key, ingredient_name)

    response = requests.get(url)

    recipe = response.json()

    return recipe["recipes"]


