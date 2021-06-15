from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits



class Inicjator():
    """
    Inicjator zaweira ważne stany, które mogą ulec zmianie z biegiem czasu.
    Definiuje on również metodę zapisywania stanu w memento, a także metodę
    odzyskiwania tegoż stanu z memento.
    """

    _state = None
    """
    W celu uproszczenia, stan Inicjatora jest przechowywany w pojedynczej zmiennej.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Inicjator: Moj stan poczatkowy to: {self._state}")

    def do_something(self) -> None:
        """
        Działanie Inicjatora może mieć wpływ na jego wewnętrzny stan,
        dlatego też powinien on zostać *zbackupowany* poprzez save() zanim
        uruchomione zostanie działanie zmieniające stan.
        """
        print("Inicjator: Pracuje...")
        self._state = self._generate_random_string(30)
        print(f"Inicjator: moj stan zostal zmieniony: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Zapisuje obecny stan w memento
        :return:
        """
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Przywraca stan inicjatora z memento
        :param memento:
        :return:
        """
        self._state = memento.get_state()
        print(f"Inicjator: moj stan zostal zmieniony: {self._state}")


class Memento(ABC):
    """
    Interfejs Memento zapewnia sposoby odzyskania danych szczególnych memento,
    takich jak data utworzenia czy nazwa. Mimo to nie ujawania on stanu Inicjatora.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        Inicjator używa tej metody gdy przywraca jakiś stan.
        :return:
        """
        return self._state
    def get_name(self) -> str:
        """
        Reszta metod jest używana przez Opiekuna by wyświetlić szczegóły.
        :return:
        """
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Opiekun():
    """
    Opiekun nie polega na klasie Concrete Memento. Dlatego nie musi mieć dostępu
    do stanu Inicjatora przechowywanego w memento. Działa ze wszystkimi memento poprzez
    podstawowy interferjs Memento.
    """
    def __init__(self, inicjator: Inicjator) -> None:
        self._mementos = []
        self._inicjator = inicjator

    def backup(self) -> None:
        print("\nOpiekun: Zapisuje stan Inicjatora...")
        self._mementos.append(self._inicjator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Opiekun: Przywracam stan do: {memento.get_name()}")
        try:
            self._inicjator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Opiekun: Oto lista zapisanych Memento:")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":

    inicjator = Inicjator("Lorem ipsum dolor sit posuere.")
    opiekun = Opiekun(inicjator)


opiekun.backup()
inicjator.do_something()

opiekun.backup()
inicjator.do_something()

opiekun.backup()
inicjator.do_something()

print()
opiekun.show_history()

print("\nCTRL+Z\n")
opiekun.undo()

print("\nCTRL+Z\n")
opiekun.undo()

print("\nCTRL+Z\n")
opiekun.undo()