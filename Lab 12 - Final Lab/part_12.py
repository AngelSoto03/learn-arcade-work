"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Zombie Slasher"

character_direction = 0

# Constants used to scale our sprites from their original size
PLAYER_SCALING = 0.2
ZOMBIE_SCALING = 0.35
TILE_SCALING = 0.5
BULLET_SPRITE_SCALING = 0.2
BULLET_SPEED = 15
SPRITE_PIXEL_SIZE = 128

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

RIGHT_FACING = 0
LEFT_FACING = 1

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 200
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 64
PLAYER_START_Y = 117


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


class InstructionView(arcade.View):

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("title_screen.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_show(self):
        """ This is run once when we switch to this view """

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = SecInstructionView()
        self.window.show_view(game_view)


class SecInstructionView(arcade.View):

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()

        self.texture = arcade.load_texture("intructions_screen.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = MyGame()
        game_view.setup(level=1)
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("game_over.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = MyGame()
        game_view.setup(level=1)
        self.window.show_view(game_view)


class PlayerCharacter(arcade.Sprite):
    """ Player Sprite"""
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = PLAYER_SCALING

        # Track our state
        self.jumping = False

        # Character Textures from Open Game Art
        # Load textures for idle standing
        self.idle_textures = []
        for i in range(10):
            texture = load_texture_pair(f"01-Idle/JK_P_Gun__Idle_{i:03}.png")
            self.idle_textures.append(texture)

        self.jump_texture_pair = load_texture_pair("05-Jump/JK_P_Gun__Jump_000.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(10):
            texture = load_texture_pair(f"02-Run/JK_P_Gun__Run_{i:03}.png")
            self.walk_textures.append(texture)

        self.jump_textures = []
        texture = load_texture_pair(f"05-Jump/JK_P_Gun__Jump_000.png")
        self.walk_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_textures[0][0]

        # Hit box will be set based on the first image used. If you want to specify
        # a different hit box, you can do it like the code below.
        # self.set_hit_box([[-22, -64], [22, -64], [22, 28], [-22, 28]])
        self.set_hit_box(self.texture.hit_box_points)

    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Jumping animation
        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return

        # Idle animation
        if self.change_x == 0:
            self.cur_texture += 1
            if self.cur_texture > 9:
                self.cur_texture = 0
            self.texture = self.idle_textures[self.cur_texture][self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]


class ZombieCharacter(arcade.Sprite):
    """ Player Sprite"""
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = ZOMBIE_SCALING

        # Track our state
        self.jumping = False

        # Character Textures from Open Game Art
        # Load textures for idle standing
        self.idle_textures = []
        for i in range(1, 7):
            texture = load_texture_pair(f"idle/idle_{i}.png")
            self.idle_textures.append(texture)

        # Load textures for walking
        self.walk_textures = []
        for i in range(1, 11):
            texture = load_texture_pair(f"walk/go_{i}.png")
            self.walk_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_textures[0][0]

        # Hit box will be set based on the first image used. If you want to specify
        # a different hit box, you can do it like the code below.
        # self.set_hit_box([[-22, -64], [22, -64], [22, 28], [-22, 28]])
        self.set_hit_box(self.texture.hit_box_points)

    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_x > 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING

        # Idle animation
        if self.change_x == 0:
            self.cur_texture += 1
            if self.cur_texture > 9:
                self.cur_texture = 0
            self.texture = self.idle_textures[self.cur_texture][self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]


class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.background_list = None
        self.damage_list = None
        self.player_list = None
        self.zombie_list = None
        self.bullet_list = None
        self.coin_list = None
        self.next_level_list = None
        self.final_list = None

        # Load sounds
        # Sounds from Salami Sound
        self.jump_sound = arcade.load_sound("JumpSound.mp3")
        self.shot_sound = arcade.load_sound("gunshot.mp3")

        # Sounds from Bible Sound
        self.zombie_dies_sound = arcade.load_sound("zombiedies.mp3")
        self.coin_sound = arcade.load_sound("positiveblip.mp3")
        self.game_over_sound = arcade.load_sound("game_over.mp3")
        self.zombie_bite_sound = arcade.load_sound("Bite.mp3")

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.zombie_sprite = None

        # Our physics engine
        self.physics_engine = None
        self.character_direction = 0

        self.game_over = False

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.level = 1

        # Keep track of the score
        self.score = 0
        self.lives = 3

    def setup(self, level):

        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.damage_list = arcade.SpriteList()
        self.zombie_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.next_level_list = arcade.SpriteList()
        self.final_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        # self.player_sprite = arcade.Sprite("hero.png", PLAYER_SCALING)
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        texture_list = []
        for texture_pair in self.player_sprite.walk_textures:
            texture_list.append(texture_pair[0])
            texture_list.append(texture_pair[1])

        for texture_pair in self.player_sprite.idle_textures:
            texture_list.append(texture_pair[0])
            texture_list.append(texture_pair[1])
        self.player_list.preload_textures(texture_list)

        for texture_pair in self.player_sprite.jump_textures:
            texture_list.append(texture_pair[0])
            texture_list.append(texture_pair[1])
        self.player_list.preload_textures(texture_list)

        # Create zombies
        if self.level == 1:
            self.zombie_sprite = ZombieCharacter()
            self.zombie_sprite.center_x = PLAYER_START_X + 1000
            self.zombie_sprite.center_y = PLAYER_START_Y + 1
            self.zombie_sprite.change_x = 2
            self.zombie_sprite.boundary_right = self.zombie_sprite.center_x + 500
            self.zombie_sprite.boundary_left = self.zombie_sprite.center_x - 500
            self.zombie_list.append(self.zombie_sprite)

            self.zombie_sprite = ZombieCharacter()
            self.zombie_sprite.center_x = PLAYER_START_X + 1000
            self.zombie_sprite.center_y = PLAYER_START_Y + 642
            self.zombie_sprite.change_x = 2
            self.zombie_sprite.boundary_right = self.zombie_sprite.center_x + 200
            self.zombie_sprite.boundary_left = self.zombie_sprite.center_x - 200
            self.zombie_list.append(self.zombie_sprite)

            self.zombie_sprite = ZombieCharacter()
            self.zombie_sprite.center_x = PLAYER_START_X + 2180
            self.zombie_sprite.center_y = PLAYER_START_Y + 258
            self.zombie_sprite.change_x = 2
            self.zombie_sprite.boundary_right = self.zombie_sprite.center_x + 150
            self.zombie_sprite.boundary_left = self.zombie_sprite.center_x - 150
            self.zombie_list.append(self.zombie_sprite)

        if self.level == 2:
            self.zombie_sprite = ZombieCharacter()
            self.zombie_sprite.center_x = PLAYER_START_X + 800
            self.zombie_sprite.center_y = PLAYER_START_Y + 260
            self.zombie_sprite.change_x = 2
            self.zombie_sprite.boundary_right = self.zombie_sprite.center_x + 200
            self.zombie_sprite.boundary_left = self.zombie_sprite.center_x - 200
            self.zombie_list.append(self.zombie_sprite)

            self.zombie_sprite = ZombieCharacter()
            self.zombie_sprite.center_x = PLAYER_START_X + 2100
            self.zombie_sprite.center_y = PLAYER_START_Y + 455
            self.zombie_sprite.change_x = 2
            self.zombie_sprite.boundary_right = self.zombie_sprite.center_x + 176
            self.zombie_sprite.boundary_left = self.zombie_sprite.center_x - 180
            self.zombie_list.append(self.zombie_sprite)

        texture_list = []
        for texture_pair in self.zombie_sprite.walk_textures:
            texture_list.append(texture_pair[0])
            texture_list.append(texture_pair[1])

        for texture_pair in self.zombie_sprite.idle_textures:
            texture_list.append(texture_pair[0])
            texture_list.append(texture_pair[1])
        self.zombie_list.preload_textures(texture_list)

        # Read the map

        my_map = arcade.tilemap.read_tmx(f"map1_level_{level}.tmx")
        self.wall_list = arcade.tilemap.process_layer(my_map, 'platforms', TILE_SCALING)
        self.background_list = arcade.tilemap.process_layer(my_map, 'background', TILE_SCALING)
        self.damage_list = arcade.tilemap.process_layer(my_map, 'damage', TILE_SCALING)
        self.coin_list = arcade.tilemap.process_layer(my_map, 'coins', TILE_SCALING)
        self.next_level_list = arcade.tilemap.process_layer(my_map, 'next_level', TILE_SCALING)
        self.final_list = arcade.tilemap.process_layer(my_map, 'final', TILE_SCALING)

        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.background_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.damage_list.draw()
        self.next_level_list.draw()
        self.final_list.draw()
        self.zombie_list.draw()

        arcade.set_background_color(arcade.color.GRAY_BLUE)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10 + self.view_left, 60 + self.view_bottom, arcade.color.WHITE, 30)

        output_2 = f"Lives left: {self.lives}"
        arcade.draw_text(output_2, 10 + self.view_left, 20 + self.view_bottom, arcade.color.WHITE, 30)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.character_direction = 1
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.character_direction = 0

        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("Bullet.png", BULLET_SPRITE_SCALING)
            arcade.play_sound(self.shot_sound)

            if self.character_direction == 0:
                # Give the bullet a speed
                bullet.change_x = BULLET_SPEED
                # Position the bullet
                bullet_position_y = self.player_sprite.center_y - 18
                bullet.center_x = self.player_sprite.center_x + 40
                bullet.center_y = bullet_position_y

            elif self.character_direction == 1:
                bullet.change_x = -BULLET_SPEED
                bullet_position_y = self.player_sprite.center_y - 18
                bullet.center_x = self.player_sprite.center_x - 40
                bullet.center_y = bullet_position_y

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):

        """ Movement and game logic """
        if not self.game_over:
            # Move the player with the physics engine
            self.physics_engine.update()
            self.zombie_list.update()
            self.bullet_list.update()
            self.player_sprite.update_animation(delta_time)
            self.zombie_list.update_animation(delta_time)

        for zombie in self.zombie_list:
            # If the enemy hit a wall, reverse
            if len(arcade.check_for_collision_with_list(zombie, self.wall_list)) > 0:
                zombie.change_x *= -1
            # If the enemy hit the left boundary, reverse
            elif zombie.boundary_left is not None and zombie.left < zombie.boundary_left and zombie.change_x < 0:
                zombie.change_x *= -1
            # If the enemy hit the right boundary, reverse
            elif zombie.boundary_right is not None and zombie.right > zombie.boundary_right and zombie.change_x > 0:
                zombie.change_x *= -1

            hit_list = arcade.check_for_collision_with_list(zombie, self.bullet_list)
            for bullet in hit_list:
                bullet.remove_from_sprite_lists()
                zombie.remove_from_sprite_lists()
                arcade.play_sound(self.zombie_dies_sound)
                self.score += 5

        for wall in self.wall_list:
            hit_list = arcade.check_for_collision_with_list(wall, self.bullet_list)
            for bullet in hit_list:
                bullet.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for i in hit_list:
            i.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        changed_viewport = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed_viewport = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed_viewport = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed_viewport = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed_viewport = True

        if changed_viewport:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        if len(arcade.check_for_collision_with_list(self.player_sprite, self.zombie_list)) > 0:
            self.lives -= 1
            arcade.play_sound(self.zombie_bite_sound)
            self.setup(self.level)

        if len(arcade.check_for_collision_with_list(self.player_sprite, self.damage_list)) > 0:
            self.lives -= 1
            arcade.play_sound(self.zombie_bite_sound)
            self.setup(self.level)

        if self.lives == 0:
            self.game_over = True
            arcade.play_sound(self.game_over_sound)

        if len(arcade.check_for_collision_with_list(self.player_sprite, self.next_level_list)) > 0:
            self.level += 1
            self.setup(self.level)

        if len(arcade.check_for_collision_with_list(self.player_sprite, self.final_list)) > 0:
            self.lives = 0

        if self.lives == 0:
            view = GameOverView()
            self.window.show_view(view)

def main():
    """ Main method """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()