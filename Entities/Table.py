from abc import ABC, abstractmethod


class Table(ABC):

    @abstractmethod
    def getCreateQuery(self):
        pass
