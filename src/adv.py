from room import Room

# Declare all the rooms

global room
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

from player import Player

global player
player = Player(room['foyer'])

def update():
    print('\n')
    print(player)

def playerChoice(rooms):
    possibileRooms = []
    for room in rooms:
        if(rooms[room].name != player.currentRoom.name):
            possibileRooms.append(room)
    return possibileRooms

i=-1
while i < 0:
    update()
    print('You can currently move to the following rooms.')
    currentRooms = playerChoice(room)
    print(currentRooms)
    choice = input('Please choose a direction to go. (n, e, s, w): ')
    if(choice == 'n'):
        player.currentRoom = room[currentRooms[0]]
    elif(choice == 'e'):
        player.currentRoom = room[currentRooms[1]]
    elif(choice == 's'):
        player.currentRoom = room[currentRooms[2]]
    elif(choice == 'w'):
        player.currentRoom = room[currentRooms[3]]