import random
import arcade
import os

SPRITE_SCALING = 0.17
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 300

PENCIL_LIST = 50
ERASER_LIST = 50
MOVEMENT_SPEED = 3


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        self.good_sound = arcade.load_sound("positiveblip.mp3")
        self.bad_sound = arcade.load_sound("negativeblip.mp3")
        self.pencil_list = None
        self.wall_list = None

        self.score = 0

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.pencil_list = arcade.SpriteList()
        self.eraser_list = arcade.SpriteList()

        # Set up the player
        #Stickman png from vexels.com
        self.player_sprite = arcade.Sprite("stickman.png", 0.2)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # SIDES
        for x in range(-800, 869, 1635):
            for y in range(0, 2069, 68):
                wall = arcade.Sprite("wallblock.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # TOP AND BOTTOM
        for x in range(-732, 801, 68):
            for y in range(0, 2069, 2040):
                    wall = arcade.Sprite("wallblock.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
                    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Blocks and walls
        for x in range(-732, 801, 68):
            for y in range(0, 2001, 204):
                if random.randrange(5) > 0:
                    block = arcade.Sprite("wallblock.png", SPRITE_SCALING)
                    block.center_x = x
                    block.center_y = y
                    self.wall_list.append(block)
                    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Pencil icon from iconspedia.com
        for i in range(PENCIL_LIST):
            pencil = arcade.Sprite("pencil.png", SPRITE_SCALING)
            pencil.center_x = x
            pencil.center_y = y

            pencil_placed_successfully = False

            while not pencil_placed_successfully:
                pencil.center_x = random.randrange(-800, 869)
                pencil.center_y = random.randrange(0, 2097)

                wall_hit_list = arcade.check_for_collision_with_list(pencil, self.wall_list)
                pencil_hit_list = arcade.check_for_collision_with_list(pencil, self.wall_list)

                if len(wall_hit_list) == 0 and len(pencil_hit_list) == 0:
                    pencil_placed_successfully = True

            self.pencil_list.append(pencil)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Eraser png from softexia.com
        for i in range(ERASER_LIST):
            eraser = arcade.Sprite("eraser.png", SPRITE_SCALING)
            eraser.center_x = x
            eraser.center_y = y

            eraser_placed_successfully = False

            while not eraser_placed_successfully:
                eraser.center_x = random.randrange(-800, 869)
                eraser.center_y = random.randrange(0, 2097)

                wall_hit_list = arcade.check_for_collision_with_list(eraser, self.wall_list)
                eraser_hit_list = arcade.check_for_collision_with_list(eraser, self.wall_list)

                if len(wall_hit_list) == 0 and len(eraser_hit_list) == 0:
                    eraser_placed_successfully = True

            self.eraser_list.append(eraser)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        # Randomly skip a box so the player can find a way through

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.pencil_list.draw()
        self.eraser_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 45, arcade.color.WHITE, 25)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()
        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        self.player_list.update()
        self.pencil_list.update()
        self.eraser_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.pencil_list)

        for pencil in hit_list:
            pencil.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.score += 1


        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.eraser_list)

        for eraser in hit_list:
            eraser.remove_from_sprite_lists()
            arcade.play_sound(self.bad_sound)
            self.score -= 1

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()