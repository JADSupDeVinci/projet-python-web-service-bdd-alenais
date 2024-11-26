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
    def get_random_ingredients_by_type(cls) -> dict:
        with Session(Engine.getEngine()) as session:
            type_ingredients = session.execute(select(cls.id_typeingredient).distinct()).scalars().all()
            random_ingredients = {}
            for type_id in type_ingredients:
                ingredients_of_type = session.query(cls).filter_by(id_typeingredient=type_id).all()
                if ingredients_of_type:
                    random_ingredient = random.choice(ingredients_of_type)
                    random_ingredients[type_id] = (random_ingredient.get_ingredient())

            return random_ingredients
