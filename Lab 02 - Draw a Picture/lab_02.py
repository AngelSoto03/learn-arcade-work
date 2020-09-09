import arcade

arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.BABY_BLUE)

# get ready to draw
arcade.start_render()

# draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 250, 0, arcade.color.AO)

# draw the clouds
arcade.draw_ellipse_filled(100, 550, 300, 100, arcade.color.WHITE_SMOKE)
arcade.draw_ellipse_outline(100, 550, 300, 100, arcade.color.GRAY)
arcade.draw_ellipse_filled(300, 530, 300, 120, arcade.color.WHITE_SMOKE)
arcade.draw_ellipse_outline(300, 530, 300, 120, arcade.color.GRAY)

# draw the sun
arcade.draw_circle_filled(700, 520, 60, arcade.color.YELLOW)

# draw the street
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 50, arcade.color.GRAY)

# draw the tree
arcade.draw_lrtb_rectangle_filled(100, 140, 310, 215, arcade.color.BROWN)
arcade.draw_circle_filled(120, 360, 65, arcade.color.AO)

# draw the base of the car
arcade.draw_lrtb_rectangle_filled(490, 740, 160, 90, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(530, 690, 210, 130, arcade.color.RED)
arcade.draw_triangle_filled(690, 210, 690, 130, 740, 160, arcade.color.RED)

# draw the windows
arcade.draw_lrtb_rectangle_filled(530, 600, 200, 165, arcade.color.SKY_BLUE)
arcade.draw_lrtb_rectangle_filled(620, 684, 200, 165, arcade.color.SKY_BLUE)

# draw the door handle
arcade.draw_lrtb_rectangle_filled(590, 600, 150, 145, (175, 175, 175))

# draw the wheels of the car
arcade.draw_circle_filled(540, 90, 32, arcade.color.BLACK)
arcade.draw_circle_filled(540, 90, 22, arcade.color.WHITE)
arcade.draw_line(518, 90, 562, 90, (175, 175, 175), 10)
arcade.draw_line(540, 112, 540, 68, (175, 175, 175), 10)
arcade.draw_circle_filled(540, 90, 5, arcade.color.BLACK)

arcade.draw_circle_filled(690, 90, 32, arcade.color.BLACK)
arcade.draw_circle_filled(690, 90, 22, arcade.color.WHITE)
arcade.draw_line(668, 90, 712, 90, (175, 175, 175), 10)
arcade.draw_line(690, 112, 690, 68, (175, 175, 175), 10)
arcade.draw_circle_filled(690, 90, 5, arcade.color.BLACK)

# draw the car´s defenses
arcade.draw_lrtb_rectangle_filled(480, 500, 120, 85, (173, 173, 173))
arcade.draw_lrtb_rectangle_filled(730, 750, 120, 85, (173, 173, 173))
arcade.draw_lrtb_rectangle_filled(480, 500, 130, 110, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(730, 750, 130, 110, (156, 10, 0))
arcade.draw_lrtb_rectangle_filled(575, 655, 100, 85, (173, 173, 173))

# draw the sign
arcade.draw_lrtb_rectangle_filled(300, 310, 320, 160, (173, 173, 173))
arcade.draw_lrtb_rectangle_filled(230, 380, 310, 235, arcade.color.RED_DEVIL)
arcade.draw_text("WELCOME TO",
                 250, 280,
                 arcade.color.YELLOW_ORANGE, 15)
arcade.draw_text("SIMPSON",
                 265, 259,
                 arcade.color.YELLOW_ORANGE, 17)
arcade.draw_text("COLLEGE",
                 268, 239,
                 arcade.color.YELLOW_ORANGE, 17)

arcade.finish_render()

arcade.run()
