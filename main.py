# main.py
from sqlalchemy.orm import sessionmaker
from torchvision.transforms.v2.functional import get_size

from database.Engine import Engine
from database.model.Ingredient import Ingredient
from database.model.Habitante import Habitante
#from database.model.Ingredient import Ingredient
#from database.model.Size import Size
from database.model.TypeIngredient import TypeIngredient

random_ingredients = Ingredient.get_random_ingredients(3)
print("Ingrédients aléatoires par type :",  random_ingredients )
random_habitante = Habitante.random_habitante()
print("Habitante aléatoire :", random_habitante)
#size = Size.get_size(3)
#print("Taille :", size)


