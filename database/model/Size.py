from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

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