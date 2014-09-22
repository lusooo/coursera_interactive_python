# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    number = -1
    if (name == "rock"):
     number = 0
    elif (name == "Spock"):
     number = 1
    elif (name == "paper"):
     number = 2
    elif (name == "lizard"):
     number = 3
    elif (name == "scissors"):
     number = 4
    else:
        print "The name %s is not valid, please try again" % name

    return number

def number_to_name(number):
    name = ""
    if (number == 0):
     name = "rock"
    elif (number == 1):
     name = "Spock"
    elif (number == 2):
     name = "paper"
    elif (number == 3):
     name = "lizard"
    elif (number == 4):
     name = "scissors"
    else:
        print "The number %d is not valid, please try again" % number

    return name
    

def rpsls(player_choice): 

    print ""
    print "Player chooses %s" % player_choice

    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses %s" % comp_choice

    diff = (player_number - comp_number) % 5
    if ((diff == 1) or (diff == 2)):
        print "Player wins!!"
    elif ((diff == 3) or (diff == 4)):
        print "Computer wins!!"
    else:
        print "It's a tie!!"    


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")