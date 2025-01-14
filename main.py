"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Dessiner avec Arcade
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Mercury"


def generate_dust(x_min, x_max, y_min, y_max, color):
    for i in range(10):
        radius = random.randint(5, 15)

        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)

        arcade.draw_circle_filled(x, y, radius, color)


def center_dust():
    generate_dust(350, 450, 50, 200, arcade.color.ASH_GREY)


def dark_center_dust():
    for i in range(10):
        radius = random.randint(5, 15)

        x = random.randint(350, 450)
        y = random.randint(50, 200)

        arcade.draw_circle_filled(x, y, radius, arcade.color.ASH_GREY)


class MyGame(arcade.Window):
    """
    La classe principale de l'application
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

    def on_draw(self):
        """
        Crée une image représentent la fusé Mercury
        """
        self.clear()

        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 50, arcade.color.BATTLESHIP_GREY)
        center_dust()

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()