from abc import ABCMeta, abstractmethod


class IServiceable(metaclass = ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass
