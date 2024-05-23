import pygame as pg


WIDTH = 1280
HEIGHT = 720

test = []


class Card:
    def __init__(self, name, mana_cost, attack, health):
        self.name = name
        self.mana_cost = mana_cost
        self.attack = attack
        self.health = health

    def __str__(self):
        return f"{self.name} (Mana: {self.mana_cost}, Attack: {self.attack}, Health: {self.health})"


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.health = 30
        self.mana = 0

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            print(f"{self.name} drew {card.name}")
        else:
            print(f"{self.name} has no more cards to draw!")

    def play_card(self, card_name):
        for card in self.hand:
            if card.name == card_name and card.mana_cost <= self.mana:
                self.hand.remove(card)
                self.mana -= card.mana_cost
                print(f"{self.name} played {card.name}")
                return card
        print(f"{self.name} cannot play {card_name}")

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Mana: {self.mana})"


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.turn = 0

    def start(self):
        for player in self.players:
            player.draw_card()
            player.draw_card()
            player.draw_card()
        self.game_loop()

    def game_loop(self):
        while all(player.health > 0 for player in self.players):
            current_player = self.players[self.turn % 2]
            print(f"\n{current_player.name}'s turn (Mana: {current_player.mana})")
            current_player.mana += 1
            current_player.draw_card()
            print(f"Hand: {[str(card) for card in current_player.hand]}")
            action = input(f"{current_player.name}, choose a card to play: ")
            if action:
                current_player.play_card(action)
            self.turn += 1
            self.check_winner()

    def check_winner(self):
        for player in self.players:
            if player.health <= 0:
                print(f"{player.name} has been defeated!")
                exit()


def play_console():
    # Create sample cards
    card1 = Card("Fireball", 4, 6, 0)
    card2 = Card("Water Elemental", 3, 3, 6)
    card3 = Card("Frostbolt", 2, 3, 0)
    deck1 = [card1, card2, card3, card1, card2, card3]
    deck2 = [card1, card2, card3, card1, card2, card3]

    # Create players
    player1 = Player("Alice", deck1)
    player2 = Player("Bob", deck2)

    # Start game
    game = Game(player1, player2)
    game.start()


# def run():
#     pg.init()
#     screen = pg.display.set_mode((WIDTH, HEIGHT))
#     clock = pg.time.Clock()
#     running = True
#
#     test.append("hello")
#
#     # surface testing
#
#     while running:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 running = False
#
#             current_player = game.turn_counter % 2
#             other_player = (game.turn_counter + 1) % 2
#
#             players[current_player].mana = 0
#             current_mana = 1 + (game.turn_counter / 2)
#             players[current_player].mana = current_mana if current_mana < 10 else 10
#
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     players[current_player].hand.cards_on_hand[0].use(other_player)
#                     game.next_turn()
#
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 if event.button == 3:
#                     players[current_player].draw()
#                     game.next_turn()
#
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 if event.button == 4:
#                     players[current_player].draw()
#                     game.next_turn()
#
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 if event.button == 5:
#                     players[current_player].draw()
#                     game.next_turn()
#
#         screen.fill("yellow")
#
#         # render player hp
#
#         hp = render_hp(players=players, size=(screen.get_width(), screen.get_height()))
#         screen.blit(hp, (0, 0))
#
#         font = pg.font.Font(None, 64)
#         text = font.render(str(40), True, (10, 10, 10))
#         textpos = text.get_rect(centerx=400, y=300)
#         screen.blit(text, textpos)

# render players decks

# for i in range(len(player1.hand.cards_on_hand)):
#     test = pygame.Rect(i * (100 + 15), 100, 100, 100)
#     # print(f" i is {i} and len player1 deck is {len(player1.deck.cards)}")
#     pygame.draw.rect(screen, player1.hand.cards_on_hand[i].color, test)
#     # pygame.draw.rect(screen, "black", test)

# for i in range(len(player2.hand.cards_on_hand)):
#     test = pygame.Rect(i * (100 + 15), screen.get_height() - 150, 100, 100)
#     pygame.draw.rect(screen, player2.hand.cards_on_hand[i].color, test)
#     # pygame.draw.rect(screen, "black", test)

# render current players turn

# pg.draw.circle(
#     screen,
#     "green",
#     (screen.get_width() * 3 / 4, 100 + (current_player * 500)),
#     60,
# )
#
# pg.display.flip()
# clock.tick(60)


if __name__ == "__main__":
    play_console()
