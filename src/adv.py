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

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

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
player = Player('outside')

def update():
    print('\n')
    print(player)
    print(room[player.currentRoom])

def playerChoice(rooms, possibleRooms = []):
    possibleRooms.clear()
    notRoom = False
    try:
        possibleRooms.append(
            rooms[player.currentRoom].n_to
        )
    except:
        notRoom = True
        pass
    if(notRoom) :
        possibleRooms.append(
            'None'
        )
        notRoom = False
    try:
        possibleRooms.append(
            rooms[player.currentRoom].e_to
        )
    except:
        notRoom = True
        pass
    if(notRoom) :
        possibleRooms.append(
            'None'
        )
        notRoom = False
    try:
        possibleRooms.append(
           rooms[player.currentRoom].s_to
        )
    except:
        notRoom = True
        pass
    if(notRoom) :
        possibleRooms.append(
            'None'
        )
        notRoom = False
    try:
        possibleRooms.append(
            rooms[player.currentRoom].w_to
        )
    except:
        notRoom = True
        pass
    if(notRoom) :
        possibleRooms.append(
            'None'
        )
        notRoom = False
    return possibleRooms

i=-1
while i < 0:
    update()
    print('You can currently move to the following rooms. \n')
    currentRooms = playerChoice(room)
    print(f' North: {currentRooms[0]} \n East: {currentRooms[1]} \n South: {currentRooms[2]} \n West: {currentRooms[3]}')
    choice = input('\nPlease choose a direction to go. (n, e, s, w): ')
    if(choice == 'n'):
        if(currentRooms[0] != 'None'):
            player.currentRoom = currentRooms[0]
        else:
            print('You cannot go here!')
    elif(choice == 'e'):
        if(currentRooms[1] != 'None'):
            player.currentRoom = currentRooms[1]
        else:
            print('You cannot go here!')
    elif(choice == 's'):
        if(currentRooms[2] != 'None'):
            player.currentRoom = currentRooms[2]
        else:
            print('You cannot go here!')
    elif(choice == 'w'):
        if(currentRooms[3] != 'None'):
            player.currentRoom = currentRooms[3]
        else:
            print('You cannot go here!')