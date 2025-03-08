"""jsonify package here is to convert our python objects (such as list) to JSON format.
Also change the content type in our HTTP response to application/json"""
from flask import Flask, jsonify, request

"""HTTPStatus enum is imported which includes different HTTP statuses:
For instance, we will have HTTPStatus.CREATED (201) and HTTPStatus.NOT_FOUND(404)."""

from http import HTTPStatus

"""Create an instance of the Flask class"""

app = Flask(__name__)

"""Define the recipes list. We store two recipes in the list. They are stored in the memory"""

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },
    {
        'id': 2,
        'name': 'Tomato Pasta',
        'description': 'This is lovely tomato pasta recipe'
    }
]


"""Use route decorator to tell Flask that the /recipes route will route to the get_recipes function.
And the methods = ['GET'] argument to specify that the route decorator will only respond to GET requests."""

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Use jsonify function to convert the list of recipes to JSON format and respond to client."""
    return jsonify({'data': recipes})

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

"""Next we will create recipe function, which creates recipe in memory.
Use the /recipes route to the create_recipe function and the methods = POST argument to specify 
that the route decorator will only respond to POST requests."""

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')

    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }

    recipes.append(recipe)

    return jsonify(recipe), HTTPStatus.CREATED

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    recipe.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )

    return jsonify(recipe)


if __name__ == "__main__":
    app.run()


