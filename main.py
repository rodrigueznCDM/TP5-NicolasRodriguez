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


class MyGame(arcade.Window):
    """
    La classe principale de l'application
    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

    @staticmethod
    def generate_circles(num, x_min, x_max, y_min, y_max, color):
        for i in range(num):
            radius = random.randint(5, 10)

            x = random.randint(x_min, x_max)
            y = random.randint(y_min, y_max)

            arcade.draw_circle_filled(x, y, radius, color)

    def center_dust(self):
        self.generate_circles(24, 350, 450, 60, 190, arcade.color.ASH_GREY)

    def dark_center_dust(self):
        self.generate_circles(10, 380, 420, 60, 190, arcade.color.TROLLEY_GREY)

    def engine_fire_yellow(self):
        self.generate_circles(12, 350, 450, 140, 240, arcade.color.SCHOOL_BUS_YELLOW)

    def engine_fire_orange(self):
        self.generate_circles(8, 350, 450, 180, 230, arcade.color.BURNT_ORANGE)

    def on_draw(self):
        """
        Crée une image représentent la fusé Mercury
        """
        self.clear()

        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 50, arcade.color.BATTLESHIP_GREY)
        self.center_dust()
        self.dark_center_dust()
        self.engine_fire_yellow()
        self.engine_fire_orange()

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