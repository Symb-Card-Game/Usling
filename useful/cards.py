from enum import Enum

class Targets(Enum, int):
    ENEMY = 0
    FRIENDLY = 1
    ENEMY_HERO = 2
    FRIENDLY_HERO = 3

class SpellType(Enum):
    SHIELD = 0
    BLOCK = 1
    BUFF = 2

class Card:
    def __init__(self, description, name, target) -> None:
        self.description = description
        self.name = name
        self.has_block = False
        self.has_buff = False
        self.target: Targets = target

    def play():
        pass

class MinionCard(Card):
    def __init__(self, hp: int, dmg: int) -> None:
        self.color = "red"
        self.hp = hp
        self.dmg = dmg 


class SpellCard(Card):
    def __init__(self, spelltype) -> None:
        self.color = "blue"
        self.type: SpellType = spelltype