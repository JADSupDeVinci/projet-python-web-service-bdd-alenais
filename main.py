# main.py
from sqlalchemy.orm import sessionmaker
from database.Engine import Engine
from database.model.Habitante import Habitante
from database.model.Ingredient import Ingredient
from database.model.TypeIngredient import TypeIngredient

random_ingredients = Ingredient.get_random_ingredients_by_type()
print("Ingrédients aléatoires par type :", random_ingredients)
random_habitante = Habitante.random_habitante()
print("Habitante aléatoire :", random_habitante)

