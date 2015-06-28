import random
import simplegui


# Define globals.
secret_number = 0
game_range = 100
guess_limit = 7


# helper function to start and restart the game
def new_game():
    global secret_number
    global game_range
    secret_number = random.randint(0, game_range - 1)
    print 'secret number is: ', secret_number
    # print 'range limit is: ', game_range


# define event handlers for control panel
def range100():
    global game_range
    global guess_limit
    game_range = 100
    guess_limit = 7
    new_game()
    print "Restart the game with new range = 100"


def range1000():
    global game_range
    global guess_limit
    game_range = 1000
    guess_limit = 10
    new_game()
    print "Restart the game with new range = 1000"


def input_guess(guess):
    global guess_limit
    global game_range
    guess = int(guess)

    if guess_limit > 0:
        print "Guess was: ", guess
        if guess > secret_number:
            guess_limit -= 1
            print "Lower"
        elif guess < secret_number:
            guess_limit -= 1
            print "Higher"
        else:
            print "Correct!"
            if game_range == 100:
                range100()
            elif game_range == 1000:
                range1000()
    else:
        print "The game is over, limit overdrafted."
        print "Secret number was: ", secret_number


# create frame
frame = simplegui.create_frame("Guess the number", 100, 200)
range100_button = frame.add_button("Range 100", range100)
range1000_button = frame.add_button("Range 1000", range1000)
frame.add_input("Your number:", input_guess, 100)
frame.start()

# call new_game
new_game()
print "You're in the game. Default range is 100."
