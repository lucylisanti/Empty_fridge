import requests


def ingredient_search(ingredient_name):
    key = "9b6153cb33143e8ec7ab80c6c9a93eb2&"

    url = 'https://www.food2fork.com/api/search?key={}q={}'.format(key, ingredient_name)

    response = requests.get(url)

    recipe = response.json()

    return recipe["recipes"]

