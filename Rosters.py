"""Rosters - this file contains the roster class and the player class that the teams will be made up of.
Within a League dictionary, each team will have a value of a roster object that contains the player 
objects. These players will be initiated with their name and their number, which consists of all bio 
and attribute values."""

class Roster:
    def __init__(self, city, name, players=[]):
        self.city = city
        self.name = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

        # Set values from number
        self.team = None
        self.position = None
        self.speed = 0
        self.strength = 0
        self.finesse = 0
        self.behavior = 0


league = {}

# Create the teams
#league["AZ"] = Roster("Arizona", "Cardinals", [Player()])