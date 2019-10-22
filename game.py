# import random package so that we can generate a random choice
from random import randint 

print("sumpin")

# choices is an array => an array is a container that can hold multiple values
choices =["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0,2)]

#set up the game loop so that we don't have to restart all the time
player = False
while player = False:
	#set player to true
	player = input("choose rock,paper,scissor\n")

	print("computer choose", computer, "\n")
	print("player chose", player, "\n")

	if computer == player:
		print("tie! no one wins, play again")
	elif player == "quit":
		exit()

	# need to check all of our conditions before checking for a tie.
	player = false
	computer = choices[randint(0,2)]