# main.py
from requests import request

from flask import Flask, render_template

from api_call import ingredient_search

app = Flask(__name__)


# @app.route('/')
# def recipes_site():
#     return render_template('index.html')
#
# app.run(debug=True)


# ingredient_name = input('What ingredient? ')
#
# recipes = ingredient_search(ingredient_name)
#
# pprint(recipes)



@app.route('/send', methods=["GET", "POST"])
def send():
    if request.method == "POST":
        ingredient = request.form["ingredient"]

        recipes = ingredient_search(ingredient)

        return render_template("ingredient.html", ingredient=ingredient, recipes=recipes)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
