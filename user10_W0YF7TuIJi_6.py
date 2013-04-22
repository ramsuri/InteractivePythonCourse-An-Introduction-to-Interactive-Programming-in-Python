# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    if number == 0:
        retName = "rock"
    elif number == 1:
        retName = "Spock"
    elif number == 2:
        retName = "paper"
    elif number == 3:
        retName = "lizard"
    else:
        retName = "scissors"
    # don't forget to return the result!
    return retName
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    if name == "rock":
        retVal = 0
    elif name == "Spock":
        retVal = 1
    elif name == "paper":
        retVal = 2
    elif name == "lizard":
        retVal = 3
    else:
        retVal = 4
    # don't forget to return the result!
    return retVal

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4,1)

    # compute difference of player_number and comp_number modulo five
    difference = player_number - (comp_number % 5)
    # use if/elif/else to determine winner
    if difference > 0:
        winner = "Player wins!"
    elif difference < 0:
        winner = "Computer wins!"
    else:
        winner = "Player and computer Tie!"
    # convert comp_number to name using number_to_name
    computerChoosenName = number_to_name(comp_number)
    
    # print results
    print "Player chooses", name
    print "Computer chooses", computerChoosenName
    print winner
    print
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


