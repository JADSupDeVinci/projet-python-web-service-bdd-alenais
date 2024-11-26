# TypeIngredient.py
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, Session

from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity

class TypeIngredient(AbstractEntity):
    __tablename__ = "typeingredient"  # Assurez-vous que le nom est correct

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    label: Mapped[str] = mapped_column(String(100))

    @property
    def Id(self) -> int:
        return self.id

    @property
    def Label(self) -> str:
        return self.label

    def __str__(self):
        return f"TypeIngredient(id={self.id}, label='{self.label}')"

    @classmethod
    def get_typeingredient(self) -> dict:
        return {
            "id": self.id,
            "label": self.label
        }

    @classmethod
    def getTypeIngredientById(cls, id: int):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).filter_by(id=id).first()
