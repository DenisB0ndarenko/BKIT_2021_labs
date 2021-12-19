from __future__ import annotations
from abc import ABC, abstractmethod


class TwixFactory(ABC):

    @abstractmethod
    def create_biscuit(self) -> AbstractBiscuit:
        pass

    @abstractmethod
    def create_caramel(self) -> AbstractCaramel:
        pass

    @abstractmethod
    def create_stick(self) -> AbstractStick:
        pass


class LeftFactory(TwixFactory):

    def create_biscuit(self) -> AbstractBiscuit:
        return LeftBiscuit()

    def create_caramel(self) -> AbstractCaramel:
        return LeftCaramel()

    def create_stick(self) -> AbstractStick:
        return LeftStick()


class RightFactory(TwixFactory):

    def create_biscuit(self) -> AbstractBiscuit:
        return RightBiscuit()

    def create_caramel(self) -> AbstractCaramel:
        return RightCaramel()

    def create_stick(self) -> AbstractStick:
        return RightStick()


class AbstractBiscuit(ABC):

    @abstractmethod
    def i_biscuit(self) -> str:
        pass


class LeftBiscuit(AbstractBiscuit):
    def i_biscuit(self) -> str:
        return "Left biscuit."


class RightBiscuit(AbstractBiscuit):
    def i_biscuit(self) -> str:
        return "Right biscuit."


class AbstractCaramel(ABC):

    @abstractmethod
    def i_caramel(self) -> None:
        pass

    @abstractmethod
    def side(self) -> None:
        pass

    @abstractmethod
    def on_the_biscuit(self, collaborator: AbstractBiscuit) -> None:

        pass


class LeftCaramel(AbstractCaramel):
    def i_caramel(self) -> str:
        return "Left caramel."

    def side(self) -> str:
        return "Left"

    def on_the_biscuit(self, collaborator: AbstractBiscuit) -> str:
        if isinstance(collaborator, RightBiscuit):
            return f"We are not the same."
        result = collaborator.i_biscuit()
        return f"Left caramel on the {result} We are the same."


class RightCaramel(AbstractCaramel):
    def i_caramel(self) -> str:
        return "Right caramel."

    def side(self) -> str:
        return "Right"

    def on_the_biscuit(self, collaborator: AbstractBiscuit):
        if isinstance(collaborator, LeftBiscuit):
            return f"We are not the same."
        result = collaborator.i_biscuit()
        return f"Right caramel on the {result} We are the same."


class AbstractStick(ABC):

    @abstractmethod
    def i_stick(self) -> str:
        pass

    def made_of(self):
        pass


class LeftStick(AbstractStick):
    def __init__(self):
        self.biscuit = LeftBiscuit()
        self.caramel = LeftCaramel()

    def i_stick(self) -> str:
        return f"{self.caramel.side()} stick."

    def made_of(self):
        return f"I'm {self.i_stick()} I'm made of {self.caramel.on_the_biscuit(self.biscuit)}"


class RightStick(AbstractStick):
    def __init__(self):
        self.biscuit = RightBiscuit()
        self.caramel = RightCaramel()

    def i_stick(self) -> str:
        return f"{self.caramel.side()} stick."

    def made_of(self):
        return f"I'm {self.i_stick()} I'm made of {self.caramel.on_the_biscuit(self.biscuit)}"


"""
def create_stick(biscuit, caramel):
    stick = [biscuit, caramel]
    return stick
"""


def client_code(factory: TwixFactory) -> None:

    biscuit = factory.create_biscuit()
    caramel = factory.create_caramel()
    stick = factory.create_stick()

    print(f"{biscuit.i_biscuit()}")
    print(f"{caramel.i_caramel()}")
    print(f"{caramel.on_the_biscuit(biscuit)}", end="\n")
    print(f"{stick.made_of()}", end="")


if __name__ == "__main__":

    print("Client: Testing client code with the left factory:")
    client_code(LeftFactory())

    print("\n")

    print("Client: Testing the same client code with the right factory:")
    client_code(RightFactory())

    print("\n")

    print("Testing the wrong components combination:")
    RB = RightBiscuit()
    LC = LeftCaramel()
    print(f"{LC.on_the_biscuit(RB)}", end="")
