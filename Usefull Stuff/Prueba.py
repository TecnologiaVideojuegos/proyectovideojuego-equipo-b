import arcade

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
MOVEMENT_SPEED = 5

class Dibujos:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

    def little_person(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 15, 30, arcade.color.BLACK)  # Boddy + head
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 24, 12, arcade.color.BLACK)  # shoulder
        arcade.draw_rectangle_filled(self.position_x + 5, self.position_y - 20, 5, 15, arcade.color.BLACK)  # right leg
        arcade.draw_rectangle_filled(self.position_x - 5, self.position_y - 20, 5, 15, arcade.color.BLACK)  # left leg
        arcade.draw_rectangle_filled(self.position_x + 11, self.position_y - 4, 5, 20, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x - 11, self.position_y - 4, 5, 20, arcade.color.BLACK)

class MyGame(arcade.Window):
    """ Initializer """

    # Call the parent class initializer
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Prueba")

        arcade.set_background_color(arcade.color.BLUE_GRAY)

        self.jugador = Dibujos(250, 270, 0, 0, 15)

    def on_draw(self):
        arcade.start_render()
        self.jugador.little_person()

    def update(self, delta_time):
        self.jugador.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if arcade.key.LEFT == key:
            self.jugador.change_x = -MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.jugador.change_x = MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.jugador.change_y = MOVEMENT_SPEED
        if key == arcade.key.DOWN:
            self.jugador.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.jugador.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.jugador.change_y = 0

def main():
    window = MyGame()
    arcade.run()

main()


