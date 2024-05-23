from useful.cards import Card

class Stack:
    def __init__(self, x: list[Card] = []) -> None:
        self.x: list[Card] = x
    def push(self, input: Card):
        self.x.append(input)
    def pop(self) -> Card:
        return self.x.pop()
    def peek(self, amount: int) -> list[Card]:
        for i in range(amount):
            result = []
            result.append(self.x[-i])
        return result
    def isEmpty(self):
        return True if self.x.count() == 0 else False
    
class DiscardPile(Stack):
    def __init__(self) -> None:
        super().__init__()

class DrawPile(Stack):
    def __init__(self, x) -> None:
        super().__init__(x)

class Hand:
    def __init__(self) -> None:
        self.cards_on_hand: list[Card] = []

class player:
    def __init__(self) -> None:
        # self.drawpile = DrawPile()
        # self.discardpile = DiscardPile()
        # self.deck = 
        self.mana = 0
        self.hand = Hand()
        self.hp = 20
        self.shield = 0

    def draw(self):
        print("draw called")
        if len(self.hand.cards_on_hand) >= 10:
            print("over max in hand")
            return
        card = self.drawpile.pop()
        self.hand.cards_on_hand.append(card)
        print(f"hand is now {len(self.hand.cards_on_hand)}, and drawpile is now {len(self.drawpile.x)}")

    def take_dmg(self, dmg):
        if self.shield:
            if dmg > self.shield:
                dmg -= self.shield
                self.shield = 0
            self.shield -= dmg
        self.hp -= dmg
    def add_shield(self, shield):
        self.shield += shield