# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
    
    def __str__(self):
        return f"The player is currently in Room:"
