"""
Transportation Example from Lab 5.2 - With Factory Pattern
"""

import pathlib
from abc import ABC, abstractmethod


class Transport(ABC):
    """Representation of Transporting activity"""

    @abstractmethod
    def load(self):
        """Handles Loading of Products"""

    @abstractmethod
    def deliver(self):
        """Handles Delivery of Products"""


class Truck(Transport):
    """Delivery by truck"""

    def load(self):
        print("Load Products to Truck")
        pass

    def deliver(self):
        print("Delivered by Truck")
        pass


class Ship(Transport):
    """Delivery by Ship"""

    def load(self):
        print("Load Products to Ship")
        pass

    def deliver(self):
        print("Delivered by Ship")
        pass


class Flight(Transport):
    """Delivery by Flight"""

    def load(self):
        print("Load Products to Flight")
        pass

    def deliver(self):
        print("Delivered by Flight")
        pass


class TransporterFactory:
    @staticmethod
    def getTransporterObject(transport_preference):
        if transport_preference == "flight":
            return Flight()
        elif transport_preference == "ship":
            return Ship()
        else:
            # default transporter - truck
            return Truck()


def main() -> None:
    """Main function - Your Logistic business logic is here
    Logistic is responsible fo planing, packing and sending"""

    # get transportation choice from the user
    transport_preference = input("Enter preferred transportation type[truck, ship, flight]: ")
    factory = TransporterFactory()
    transporter = factory.getTransporterObject(transport_preference)

    # load product to transporter
    transporter.load()

    # deliver product via transporter
    transporter.deliver()


if __name__ == "__main__":
    main()
