import arcade

PLAYER_SCALE = 0.2
ZOMBIE_SCALE = 0.3
MOVEMENT_SPEED = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Zombie Slash"

SPRITE_SCALING = 0.8

VIEWPOINT_MARGIN = 200

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.zombie_sprite = None

        self.lives_list = None
        self.floor_list = None
        self.wall_list = None
        self.zombies_list = None

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
        self.lives_list = arcade.SpriteList()
        self.zombies_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()

        # Hero Sprite
        # Sprite from: Segel @ Open Game Art
        self.player_sprite = arcade.Sprite("Hero.png", PLAYER_SCALE)
        self.player_sprite.center_x = SCREEN_WIDTH / 5
        self.player_sprite.center_y = SCREEN_HEIGHT / 4
        self.player_list.append(self.player_sprite)

        # Zombie Sprite
        # Sprite from: irmirx @ Open Game Art
        self.zombie_sprite = arcade.Sprite("zombie.png", ZOMBIE_SCALE)
        self.zombie_sprite.center_x = (SCREEN_WIDTH / 5) + 200
        self.zombie_sprite.center_y = SCREEN_HEIGHT / 4
        self.zombies_list.append(self.zombie_sprite)

        # Walls
        for x in range(0, 1000, 100):
            for y in range(100, 180, 100):
                wall = arcade.Sprite("wall128x128.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Floor
        """for x in range(100, 800, 100):
            for y in range(100, 1000, 20):
                floor = arcade.Sprite("flagstone1.jpg", SPRITE_SCALING)
                floor.center_x = x
                floor.center_y = y
                self.floor_list.append(wall)
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)"""

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.floor_list.draw()
        self.player_list.draw()
        self.zombies_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10 + self.view_left, 45 + self.view_bottom, arcade.color.WHITE, 25)

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

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()