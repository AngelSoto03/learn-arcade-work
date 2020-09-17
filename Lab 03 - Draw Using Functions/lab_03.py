import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_grass():
    """Draw the grass"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.AO)

def draw_tree(x, y):
    """Draw a tree"""
    arcade.draw_lrtb_rectangle_filled(x, x + 40, y + 120, y, arcade.color.BROWN)
    arcade.draw_circle_filled(x + 20, y + 170, 80, arcade.color.AO)
    arcade.draw_circle_outline(x + 20, y + 170, 80, arcade.color.FOREST_GREEN, 10)
    arcade.draw_line(x, y + 60, x - 40, y + 70, arcade.color.BROWN, 10)
    arcade.draw_line(x + 40, y + 35, x + 80, y + 45, arcade.color.BROWN, 10)

def draw_flower(x, y):
    """Draw a flower"""
    arcade.draw_line(x, y - 10, x, y + 45, arcade.color.APPLE_GREEN, 10)
    arcade.draw_ellipse_filled(x, y + 55, 65, 20, arcade.color.ORANGE_RED)
    arcade.draw_ellipse_filled(x, y + 55, 20, 65, arcade.color.ORANGE_RED)
    arcade.draw_circle_filled(x, y + 55, 15, arcade.color.YELLOW)

def draw_moon(x, y):
    """ Draw a moon"""
    arcade.draw_circle_filled(x, y, 80, arcade.color.DARK_GRAY)
    arcade.draw_circle_outline(x, y, 80, arcade.color.GRAY, 10)
    arcade.draw_circle_filled(x - 20, y - 30, 20, arcade.color.GRAY)
    arcade.draw_circle_filled(x - 20, y + 15, 10, arcade.color.GRAY)
    arcade.draw_circle_filled(x - 50, y + 7, 10, arcade.color.GRAY)

def draw_star(x, y):
    """Draw a star"""
    arcade.draw_circle_filled(x, y, 10, arcade.color.YELLOW)
    arcade.draw_line(x - 20, y, x + 20, y, arcade.color.YELLOW, 5)
    arcade.draw_line(x, y + 20, x, y - 20, arcade.color.YELLOW, 5)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_tree(100, 180)
    draw_tree(330, 200)
    draw_tree(570, 190)
    draw_flower(100, 20)
    draw_flower(200, 60)
    draw_flower(300, 40)
    draw_flower(400, 80)
    draw_flower(530, 60)
    draw_flower(650, 40)
    draw_moon(720, 520)
    draw_star(150, 550)
    draw_star(300, 520)
    draw_star(430, 490)
    draw_star(580, 540)

    #Finish and Run
    arcade.finish_render()
    arcade.run()

main()
