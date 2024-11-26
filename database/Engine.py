from abc import ABC
from sqlalchemy import create_engine, URL, text

class Engine(ABC):
    __engine = None

    @classmethod
    def getEngine(cls):
        if cls.__engine is None:
            urlObject = URL.create(
                "mysql+pymysql",
                username="root",
                password="root",
                host="localhost",
                database="pizza"              )
            cls.__engine = create_engine(urlObject)
        return cls.__engine
