from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, text

db = SQLAlchemy()
from database.model.Ingredient import Ingredient
from database.model.Habitante import Habitante

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/pizza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/get-pizza', methods=['GET'])
def getPizza():
        ingredients = Ingredient.get_random_ingredients(3)
        return jsonify(ingredients)

@app.route('/random-habitante', methods=['GET'])
def get_random_habitante():
        habitante = Habitante.random_habitante()
        return jsonify(habitante.to_dict())

db.init_app(app)


from sqlalchemy import text

@app.route('/add-habitante', methods=['POST'])
def add_habitante():
    data = request.json
    label = data.get('label')

    try:
        sql = text("CALL AddHabitante(:label)")
        db.session.execute(sql, {'label': label})
        db.session.commit()

        return jsonify({
            'message': f"Habitante avec le label '{label}' a été ajoutée",
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500



@app.route('/add-type-ingredient', methods=['POST'])
def add_type_ingredient():
    data = request.json
    label = data.get('label')

    if not label:
        return jsonify({'error': 'Tous les champs sont requis'}), 400

    try:
        # Utilisation de text() pour exécuter la procédure stockée
        sql = text("CALL AddTypeIngredient(:label)")
        db.session.execute(sql, {'label': label})
        db.session.commit()

        return jsonify({
            'message': f'Type Ingrédient avec le nom "{label}" a été ajouté',
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/add-ingredient', methods=['POST'])
def add_ingredient():
    data = request.json
    label = data.get('label')
    label_commercial = data.get('label_commercial')
    id_typeingredient = data.get('id_typeingredient')

    if not label or not label_commercial or not id_typeingredient:
        return jsonify({'error': 'Tous les champs sont requis'}), 400

    try:
        # Utilisation de text() pour exécuter la procédure stockée
        sql = text("CALL AddIngredient(:label, :label_commercial, :id_typeingredient)")
        db.session.execute(sql, {'label': label, 'label_commercial': label_commercial, 'id_typeingredient': id_typeingredient})
        db.session.commit()

        return jsonify({
            'message': f'Ingrédient avec le nom "{label}" a été ajouté',
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/update-ingredient/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id):
    data = request.json
    label_commercial = data.get('label_commercial')

    if not label_commercial:
        return jsonify({'error': 'Tous les champs sont requis'}), 400

    try:
        # Utilisation de text() pour exécuter la procédure stockée
        sql = text("CALL UpdateIngredient(:label_com, :ingredient_id)")
        db.session.execute(sql, {'label_com': label_commercial, 'ingredient_id': ingredient_id})
        db.session.commit()

        return jsonify({
            'message': f'Ingrédient avec le nom "{label_commercial}" a été modifié',
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


from sqlalchemy import text

@app.route('/delete-ingredient/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    try:
        sql = text("CALL DeleteIngredient(:ingredient_id)")
        db.session.execute(sql, {'ingredient_id': ingredient_id})
        db.session.commit()

        return jsonify({'message': f'Ingredient avec ID {ingredient_id} a été supprimé'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
