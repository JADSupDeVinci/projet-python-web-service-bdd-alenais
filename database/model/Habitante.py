import random

from sqlalchemy import String
from sqlalchemy.orm import Session, Mapped, mapped_column

from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity


class Habitante(AbstractEntity):
    __tablename__ = "habitante"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(100))

    @property
    def Id(self) -> int:
        return self.id

    @property
    def Label(self) -> str:
        return self.label

    @classmethod
    def get_habitante(cls, id: int):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).filter_by(id=id).first()

    def __str__(self):
        return f"Habitante(id={self.id}, label='{self.label}')"

    @classmethod
    def random_habitante(cls):
        with Session(Engine.getEngine()) as session:
            habitantes = session.query(cls).all()
            if habitantes:
                selected_habitante = random.choice(habitantes)
                return selected_habitante
            else:
                return None



    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label
        }