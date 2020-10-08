class Room:
    def __init__(self):
        self.description = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0

def main():

    room_list = []

    # Outside
    room = Room()
    room.north = 1
    room.south = None
    room.east = None
    room.west = None
    room.description = "You are outside a black house, to your north is a half-open door that looks kinda creepy,\n" \
                       "but there is nowhere else to go, so might as well go in."
    room_list.append(room)

    # Lobby room
    room = Room()
    room.north = 2
    room.south = 0
    room.east = None
    room.west = None
    room.description = "You are now in the lobby room. To your south stands the cold and scary outside\n" \
                       "and to your north stands a brown wooden door that looks way fancier than the first one."
    room_list.append(room)

    # South Hall
    room = Room()
    room.north = 6
    room.south = 1
    room.east = 3
    room.west = 4
    room.description = "You are in the south section of the Hall, to your north is the north section of the hall\n" \
                       "to your west is a mysterious storage room, and to your east is the living room. \n" \
                       "Lastly, to your south is the lobby room."
    room_list.append(room)

    # Storage room
    room = Room()
    room.north = None
    room.south = None
    room.east = 2
    room.west = None
    room.description = "You are now in the storage room, it looks quite empty but there might\n" \
                       "be stuff that you can use later.\n" \
                       "The door out is to your east."
    room_list.append(room)

    # Living room
    room = Room()
    room.north = 5
    room.south = None
    room.east = None
    room.west = 2
    room.description = "You are in the living room, to your north is the kitchen\n" \
                       "and to your west the door back to the hall."
    room_list.append(room)

    # Kitchen
    room = Room()
    room.north = None
    room.south = 3
    room.east = None
    room.west = 6
    room.description = "You are now in the kitchen. It looks like there is a whole mess,\n" \
                       "everything looks out of order. To your West is a door that leads to\n" \
                       "the north section of the hall and to your south is the door that leads\n" \
                       "to the living room."
    room_list.append(room)

    # North hall
    room = Room()
    room.north = 8
    room.south = 2
    room.east = 5
    room.west = 7
    room.description = "You are in the north section of the hall. To your north are some stairs\n" \
                       "to go upstairs. To your east is a door that leads to the kitchen and to\n" \
                       "your west a door that leads to the dining room.\n"
    room_list.append(room)

    # Dining room
    room = Room()
    room.north = None
    room.south = None
    room.east = 6
    room.west = None
    room.description = "You are in a nice dining room with a squared table that has 4 chairs\n" \
                       "around it. Everything looks very fancy and it looks like someone might\n" \
                       "have been here before. To your east is the door out of the Dining room.\n"
    room_list.append(room)

    # Stairs
    room = Room()
    room.north = 9
    room.south = 6
    room.east = None
    room.west = None
    room.description = "You are half way through the stairs and to the north is the upper hall,\n" \
                       "to your south is the way back of the stairs."
    room_list.append(room)

    # Upper Hall
    room = Room()
    room.north = None
    room.south = 8
    room.east = 10
    room.west = 11
    room.description = "You are now in the upper hall. On a wall in front of you is hanging\n" \
                       "a painting of a mysterious man. He looks kind of edgy. To your east is\n" \
                       "the eastern bedroom, and to your west is the western bedroom."
    room_list.append(room)

    # West Bedroom
    room = Room()
    room.north = None
    room.south = None
    room.east = 9
    room.west = None
    room.description = "You are in the western bedroom and sadly there is no cowboy material, but there\n" \
                       "is a bed and more pictures of the edgy man hanging on the walls. To your east stands\n" \
                       "the door to go back to the upper hall."
    room_list.append(room)

    #East bedroom
    room = Room()
    room.north = None
    room.south = None
    room.east = None
    room.west = 9
    room.description = "You are now in the eastern bedroom and there is only another bed and more\n" \
                       "pictures of the edgy man laying around the room. \n"
    room_list.append(room)


    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)

        user_choice = input("What do you want to do? ")
        print()
        if user_choice.upper() == "N" or user_choice.upper() == "NORTH":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "S" or user_choice.upper() == "SOUTH":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "E" or user_choice.upper() == "EAST":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "W" or user_choice.upper() == "WEST":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
            print("Well, the mystery stays unsolved.")
            done = True

        else:
            print("I can't understand that")


main()