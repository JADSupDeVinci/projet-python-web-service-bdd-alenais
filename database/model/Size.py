from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Session

from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity


class Size(AbstractEntity):
    __tablename__ = "size"
    id:Mapped[int] = mapped_column(primary_key=True)
    label:Mapped[str] = mapped_column(String(100))

    @property
    def Id(self) -> int:
        return self.id

    @property
    def Label(self) -> str:
        return self.label

    @classmethod
    def get_size(cls, id: int):
        with Session(Engine.getEngine()) as session:
            size = session.query(cls).filter_by(id=id).first()
            if size:
                return size.Label
            else:
                return None