import arcade

arcade.open_window(1280, 720, "Prueba")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()


def little_person(x, y):
    arcade.draw_rectangle_filled(x, y, 15, 30, arcade.color.BLACK)  # Boddy + head
    arcade.draw_rectangle_filled(x, y, 24, 12, arcade.color.BLACK)  # shoulder
    arcade.draw_rectangle_filled(x + 5, y - 20, 5, 15, arcade.color.BLACK)  # right leg
    arcade.draw_rectangle_filled(x - 5, y - 20, 5, 15, arcade.color.BLACK)  # left leg
    arcade.draw_rectangle_filled(x + 11, y - 4, 5, 20, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x - 11, y - 4, 5, 20, arcade.color.BLACK)


print(little_person(300, 300))
arcade.finish_render()
arcade.run()
