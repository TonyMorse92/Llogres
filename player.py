# Player Character.
# Might make a generic character and have the PC be a 
# subclass

from Item import Item


# Do I want the standard DND attributes? I do like the Mount and Blade: Warband 10.
# Also very likely that the Mount and Blade influence will be dropping off, I don't 
# Think it will be feasible to balance a game where a player can cheese combat.
class Player:
	def __init__(self, size: float, health: int, ):
		pass

	def attack(self, weapon: Item):
