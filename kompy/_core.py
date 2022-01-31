from sqlalchemy import create_engine

# from ._orm import *
from ._settings import KompySettings


class Kompy(object):
    """
    """
    
    __slots__ = ('_engine', )

    def __init__(self, settings: KompySettings) -> None:
        self._engine = create_engine(settings.to_database_uri())
