from random import randint

class StudentFighter(object):

	
	def __init__(self, strength, health, name):
		self.strength = strength
		self.name = name
		self.health = health

	def attack(self, opponent):
		multiplier = randint(1, 4)
		damage = multiplier * self.strength
		opponent.health -= damage

		message_one = "A successful attack!"
		if multiplier >2:
			message_one += " Critical Damage!"

		if opponent.health > 0:	
			message_two = "\n{} has {} health points remaining".format(opponent.name, opponent.health)
		else:
			message_two = "\n{} has fainted. {} wins!".format(opponent.name, self.name)

		print(message_one, message_two)


kalu = StudentFighter(strength=10, health=100, name="Kalu")
david = StudentFighter(strength=15, health=100, name="David")

while david.health > 0 and kalu.health > 0:
	attacker = input()
	defenser = input()
	if attacker == "kalu":
		kalu.attack(david)
	else:
		david.attack(kalu)
