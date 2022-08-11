from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from car import Car

class carFactory:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on

    def create_calliope(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_glissade(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_palindrome(self):
        engine = SternmanEngine(self.warning_light_is_on)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_rorschach(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_thovex(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)