from abc import ABC, abstractmethod
class Elf(ABC):
    def __init__(self, name, mus_instrument, fav_song):
        self.name = name
        self.mus_instrument = mus_instrument
        self.fav_song = fav_song

    def play_song(self):
        print(f"Elf {self.name} plaing {self.fav_song}"
              f"on {self.mus_instrument}")

    @abstractmethod
    def fight(self):
        pass


class ElsRanger(Elf):
    def __init__(self, name, mus_instrument, fav_song, bow: dict):
        super().__init__(name, mus_instrument, fav_song)
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def fight(self):
        print(f"Elf {self.name} kills his opponent with {self.bow}")

bob = ElsRanger("Bob", "lute", "bad Romance",
                {"name":"M249", "damage": 999})
bob.play_song()
bob.fight()