import random

def name_to_number(name):
    if name == 'rock':
      result = 0
    elif name == 'Spock':
      result = 1
    elif name == 'paper':
      result = 2
    elif name == 'lizard':
      result = 3
    elif name == 'scissors':
      result = 4
    else:
      result = -1

    return result


def number_to_name(number):
    if number == 0:
      result = 'rock'
    elif number == 1:
      result = 'Spock'
    elif number == 2:
      result = 'paper'
    elif number == 3:
      result = 'lizard'
    elif number == 4:
      result = scissors
    else:
      result = ''

    return result


def rpsls(player_choice):
    print ''
    print 'Player chooses ' + player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)

    print 'Computer chooses ' + comp_choice

    result = (comp_number - player_number) % 5
    if result == 0:
      print 'Player and computer tie!'
    elif result <= 2 :
      print 'Player wins!'
    elif result >= 3:
      print 'Computer wins!'


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
