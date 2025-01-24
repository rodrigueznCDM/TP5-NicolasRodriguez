"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Dessiner avec Arcade
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Mercury - Redstone 2"
rocket_color = arcade.color.ANTIQUE_WHITE


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

    def dust(self):
        self.generate_circles(18, 370, 430, 50, 160, arcade.color.ASH_GREY)

    def floor_dust(self):
        self.generate_circles(12, 340, 460, 50, 70, arcade.color.ASH_GREY)

    def dark_dust(self):
        self.generate_circles(6, 390, 410, 50, 140, arcade.color.TROLLEY_GREY)

    def engine_fire_yellow(self):
        self.generate_circles(18, 370, 430, 120, 200, arcade.color.SCHOOL_BUS_YELLOW)

    def engine_fire_orange(self):
        self.generate_circles(6, 390, 410, 100, 200, arcade.color.BURNT_ORANGE)

    def on_draw(self):
        """
        Crée une image représentent la fusé Redstone 2 du Projet Mercury
        """
        self.clear()

        # Poussière du moteur
        self.dust()
        self.floor_dust()
        self.dark_dust()
        self.engine_fire_yellow()
        self.engine_fire_orange()

        # Le sol va par-dessus les cercles pour faire comme si la fumée touche le sol
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 50, arcade.color.BATTLESHIP_GREY)

        # Formes autour du moteur
        arcade.draw_lrbt_rectangle_filled(330, 470, 200, 220, rocket_color)
        arcade.draw_lrbt_rectangle_filled(350, 450, 220, 235, rocket_color)
        arcade.draw_triangle_filled(350, 235, 450, 235, 400, 280, rocket_color)

        # Sortie du moteur
        arcade.draw_ellipse_filled(400, 210, 70, 18, arcade.color.SMOKY_BLACK)

        # Corps de la fusée
        arcade.draw_lrbt_rectangle_filled(375, 425, 250, 500, rocket_color)
        arcade.draw_line(375, 330, 425, 330, arcade.color.SMOKY_BLACK, 5)
        arcade.draw_line(375, 420, 425, 420, arcade.color.SMOKY_BLACK, 5)

        # Écriture sur la fusée
        arcade.draw_text()

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
