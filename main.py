import pygame as pg

from gameloop.gameloop import Game
from renderer.numbers import render_hp
from useful.player import player

WIDTH = 1280
HEIGHT = 720

test = []


def run():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    running = True

    test.append("hello")

    game = Game()

    players = (player(), player())

    # surface testing

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            current_player = game.turn_counter % 2
            other_player = (game.turn_counter + 1) % 2

            players[current_player].mana = 0
            current_mana = 1 + (game.turn_counter / 2)
            players[current_player].mana = current_mana if current_mana < 10 else 10

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    players[current_player].hand.cards_on_hand[0].use(other_player)
                    game.next_turn()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    players[current_player].draw()
                    game.next_turn()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    players[current_player].draw()
                    game.next_turn()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 5:
                    players[current_player].draw()
                    game.next_turn()

        screen.fill("yellow")

        # render player hp

        hp = render_hp(players=players, size=(screen.get_width(), screen.get_height()))
        screen.blit(hp, (0, 0))

        font = pg.font.Font(None, 64)
        text = font.render(str(40), True, (10, 10, 10))
        textpos = text.get_rect(centerx=400, y=300)
        screen.blit(text, textpos)

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

        pg.draw.circle(
            screen,
            "green",
            (screen.get_width() * 3 / 4, 100 + (current_player * 500)),
            60,
        )

        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
