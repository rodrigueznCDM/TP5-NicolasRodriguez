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

    def engine_exhaust(self):
        self.generate_circles(18, 370, 430, 50, 160, arcade.color.ASH_GREY)
        self.generate_circles(12, 340, 460, 50, 70, arcade.color.ASH_GREY)
        self.generate_circles(6, 390, 410, 50, 140, arcade.color.TROLLEY_GREY)
        self.generate_circles(18, 370, 430, 120, 200, arcade.color.SCHOOL_BUS_YELLOW)
        self.generate_circles(6, 390, 410, 100, 200, arcade.color.BURNT_ORANGE)

    @staticmethod
    def floor():
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 50, arcade.color.BATTLESHIP_GREY)

    @staticmethod
    def rocket_body():
        arcade.draw_lrbt_rectangle_filled(375, 425, 250, 500, rocket_color)
        arcade.draw_line(375, 340, 425, 340, arcade.color.SMOKY_BLACK, 5)
        arcade.draw_line(375, 420, 425, 420, arcade.color.SMOKY_BLACK, 5)

    @staticmethod
    def engine():
        arcade.draw_lrbt_rectangle_filled(330, 470, 200, 220, rocket_color)
        arcade.draw_lrbt_rectangle_filled(350, 450, 220, 235, rocket_color)
        arcade.draw_triangle_filled(350, 235, 450, 235, 400, 280, rocket_color)
        trapeze_points = [(359, 237), (441, 237), (420, 257), (380, 257)]
        arcade.draw_polygon_filled(trapeze_points, arcade.color.SMOKY_BLACK)
        arcade.draw_ellipse_filled(400, 210, 70, 18, arcade.color.SMOKY_BLACK)

    @staticmethod
    def vertical_writing():
        red = arcade.color.RED
        size = 10
        x = 395

        arcade.draw_text("U", x, 400, red, size)
        arcade.draw_text("N", x, 390, red, size)
        arcade.draw_text("I", x, 380, red, size)
        arcade.draw_text("T", x, 370, red, size)
        arcade.draw_text("E", x, 360, red, size)
        arcade.draw_text("D", x, 350, red, size)
        arcade.draw_text("S", x, 320, red, size)
        arcade.draw_text("T", x, 310, red, size)
        arcade.draw_text("A", x, 300, red, size)
        arcade.draw_text("T", x, 290, red, size)
        arcade.draw_text("E", x, 280, red, size)
        arcade.draw_text("S", x, 270, red, size)

    @staticmethod
    def stripes():
        arcade.draw_arc_filled(400, 500, 50, 10, arcade.color.SMOKY_BLACK, 0, 180)

    @staticmethod
    def rocket_nose():
        pass

    def on_draw(self):
        """
        Crée une image représentent la fusé Redstone 2 du Projet Mercury
        """
        self.clear()

        # Poussière du moteur
        self.engine_exhaust()

        # Le sol va par-dessus les cercles pour faire comme si la fumée touche le sol
        self.floor()

        # Corps de la fusée
        self.rocket_body()

        # Moteur
        self.engine()

        # Écriture sur la fusée
        self.vertical_writing()

        # Traits noirs
        self.stripes()

        # Nez de la fusée
        self.rocket_nose()

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
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
