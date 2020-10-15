""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.35
SPRITE_SCALING_BONE = 0.15
BONE_COUNT = 50
BUG_COUNT = 50

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class Bone(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Bug(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Move the bug
        self.center_y -= 1

        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.good_sound = arcade.load_sound("dogbite.mp3")
        self.bad_sound = arcade.load_sound("dogbark.mp3")
        self.player_list = None
        self.bone_list = None
        self.bug_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BABY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bone_list = arcade.SpriteList()
        self.bug_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("dogsprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(BONE_COUNT):

            # Create the bone instance
            # bone image from Share Icon . Net
            bone = Bone("boneicon.png", SPRITE_SCALING_BONE)

            # Position the bone
            bone.center_x = random.randrange(SCREEN_WIDTH)
            bone.center_y = random.randrange(SCREEN_HEIGHT)
            bone.change_x = random.randrange(-3, 4)
            bone.change_y = random.randrange(-3, 4)

            # Add the bone to the lists
            self.bone_list.append(bone)

        for i in range(BUG_COUNT):

            bug = Bug("bugicon.png", SPRITE_SCALING_BONE)

            bug.center_x = random.randrange(SCREEN_WIDTH)
            bug.center_y = random.randrange(SCREEN_HEIGHT)
            bug.change_x = random.randrange(-3, 4)
            bug.change_y = random.randrange(-3, 4)

            self.bug_list.append(bug)


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.bone_list.draw()
        self.player_list.draw()
        self.bug_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_list.update()
        self.bone_list.update()
        self.bug_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bone_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for bone in hit_list:
            bone.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bug_list)

        for bug in hit_list:
            bug.remove_from_sprite_lists()
            arcade.play_sound(self.bad_sound)
            self.score -= 1

        if self.score == 0:
            

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()