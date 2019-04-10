import requests

def ingredient_search(ingredient_name):
    key = "e1235990de7f65160fd351d7e118209a&"

    url = 'https://www.food2fork.com/api/search?key={}q={}'.format(key, ingredient_name)

    response = requests.get(url)

    recipe = response.json()
    return recipe["recipes"]


 