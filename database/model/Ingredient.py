# Ingredient.py
import random
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, Session
from sqlalchemy import select
from database.model.AbstractEntity import AbstractEntity
from database.Engine import Engine
from database.model.TypeIngredient import TypeIngredient


class Ingredient(AbstractEntity):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    label: Mapped[str] = mapped_column(String(100))
    label_commercial: Mapped[str] = mapped_column(String(100))
    id_typeingredient: Mapped[int] = mapped_column(ForeignKey("typeingredient.id"))
    type_ingredient = relationship("TypeIngredient")

    @property
    def Id(self) -> int:
        return self.id

    @property
    def Label(self) -> str:
        return self.label

    @property
    def LabelCommercial(self) -> str:
        return self.label_commercial

    @property
    def IdTypeIngredient(self) -> int:
        return self.id_typeingredient

    def get_ingredient(self) -> dict:
        return {
            "id": self.id,
            "label": self.label,
            "label_commercial": self.label_commercial,
            "id_typeingredient": self.id_typeingredient
        }

    @classmethod
    def get_random_ingredients(cls, nb_ingredients_type2: int) -> dict:
        with Session(Engine.getEngine()) as session:
            random_ingredients = {}
            ingredient_type_1 = session.query(cls).filter_by(id_typeingredient=1).all()
            if ingredient_type_1:
                random_ingredients["type_1"] = random.choice(ingredient_type_1).get_ingredient()
            else:
                random_ingredients["type_1"] = None
            ingredients_type_2 = session.query(cls).filter_by(id_typeingredient=2).all()
            if ingredients_type_2:
                selected_ingredients = random.sample(
                    ingredients_type_2,
                    min(nb_ingredients_type2, len(ingredients_type_2))
                )
                random_ingredients["type_2"] = [ingredient.get_ingredient() for ingredient in selected_ingredients]
            else:
                random_ingredients["type_2"] = []
            return random_ingredients


