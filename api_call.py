import requests
from meat import veggie


def ingredient_search(ingredient_name):
    key = "2a20358de222d2f754818608a79013ad&"

    url = 'https://www.food2fork.com/api/search?key={}q={}'.format(key, ingredient_name)

    response = requests.get(url)

    recipe = response.json()

    return recipe["recipes"]


print(ingredient_search('tomato'))


# for item in ingredient_search('potato'):
#     if not veggie(item['title']):
#         ingredient_search('potato').remove(item)