from .battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date.year - self.last_service_date.year > 4