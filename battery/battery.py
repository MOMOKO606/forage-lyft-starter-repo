from abc import ABC,abstractmethod
import datetime

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass