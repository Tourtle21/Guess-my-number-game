from os import system
from random import randint
ls = [0]
scores = [0]
def say(something):
    system ('say "%s"' % something)

def highOrLevels(max_number, guesses, begin, hl, hc, points):
    first_line = "Guess a number between 1 and %d" % max_number
    high_score = "Your high score is %d" % hl
    print (begin)
    say(high_score)
    say(first_line)
    number = randint(1, max_number)

    print (points)

    print (points)
    while guesses > -788:
        answer = number
        guess = raw_input("?")
        guessNumber = "You know have %d guesses" % guesses
        
        hi = any(char.isdigit() for char in guess)
        if guess == "close":
            main(points)
        if hi == False:
            say ("You didn't even guess a number")
        if guesses == 0:
            say("you are a failure")
            global scores
            scores = sum(ls)
            global ls 
            ls = []
            levels()
        if hi == True:
            if answer > int(guess):
                say(guessNumber)
                say("You guessed too low")
                guesses -= 1
            elif answer < int(guess):
                say(guessNumber)
                say("You guessed too high")
                guesses -= 1
            elif answer == int(guess):
                say("You are pro")
                points = guesses * 10
                ls.append(points)
                break
def highOrLow(max_number, guesses):
    first_line = "Guess a number between 1 and %d" % max_number
    say(first_line)
    number = randint(1, max_number)
    while guesses > -788:
        answer = number
        guess = raw_input("?")
        guessNumber = "You know have %d guesses" % guesses
        say(guessNumber)
        hi = any(char.isdigit() for char in guess)
        if guess == "close":
            main(points)
        if hi == False:
            say ("You didn't even guess a number")
        if guesses == 0:
            say("you are a failure")
            newGame()
        if hi == True:
            if answer > int(guess):
                say("You guessed too low")
                guesses -= 1
            elif answer < int(guess):
                say("You guessed too high")
                guesses -= 1
            elif answer == int(guess):
                say("You are pro")
                newGame()
def hotOrCold(max_number, guesses, first, smart):
    first_line = "Guess a number between 1 and %d" % max_number
    say(first_line)
    number = randint(1, max_number)
    while guesses > -54:
        guess = raw_input("?")
        guessNumber = "You know have %d guesses" % guesses
        say(guessNumber)
        hi = any(char.isdigit() for char in guess)
        if guess == "close":
            main(points)
        if hi == False:
            say ("You didn't even guess a number")
        if guesses == 0:
            say("you are a failure")
            newGame()
        if hi == True:
            if int(guess) == number:
                say ("you are pro")
                guesses -=1
                main(points)
            elif guesses == smart:
                guesses -= 1
                say("nice first guess but you are wrong")
                first = int(guess)
            elif abs(number - first) > abs(number - int(guess)):
                guesses -= 1
                say("you are hotter")
                first = int(guess)
            elif abs(number - first) < abs(number - int(guess)):
                guesses -= 1
                say("you are colder")
                first = int(guess)
            elif abs(number - first) == abs(number - int(guess)):
                guesses -= 1
                say("You guessed the same distance apart")
                first = int(guess)

def freePlay():
    print ("FREEPLAY")
    start()
    game = raw_input("Type h for highest to lowest, c for hot and cold, and main for Main menu:")
    if game == "h":
        say("What do you want the max number to be")
        max_number = input("Type here:")
        say("How many guesses do you want")
        guesses = input("Type here:")
        guesses -= 1
        highOrLow(max_number, guesses)
    elif game == "c":
        say("What do you want the max number to be")
        max_number = input("Type here:")
        say("How many guesses do you want")
        guesses = input("Type here:")
        guesses -= 1
        first = 0
        smart = guesses
        hotOrCold(max_number, guesses, first, smart)
    elif game == "main":
        main(points)
def levels(points):
    hl = 0
    hc = 0
    print ("LEVELS")
    print ("HIGH SCORES")
    print ("Higher and Lower = %d" % max(scores))
    print ("Hotter and Colder = %d" % hc)
    start()
    say ("You will increase levels each time you win")
    game = raw_input("Type h for highest to lowest, c for hot and cold, and main for Main menu:")
    if game == "h":
        max_number = 100
        guesses = 10
        begin = "This is level 1"
        highOrLevels(max_number, guesses, begin, hl, hc, points)
        hl = sum(ls)
        begin = "This is level 2"
        guesses = 8
        highOrLevels(max_number, guesses, begin, hl, hc, points)
        hl = sum(ls)
        begin = "This is level 3"
        guesses = 5
        highOrLevels(max_number, guesses, begin, hl, hc, points)
        hl = sum(ls)
        begin = "this is level 4"
        guesses = 3
        highOrLevels(max_number, guesses, begin, hl, hc, points)
        hl = sum(ls)
        begin = "this is level 5"
        guesses = 1
        highOrLevels(max_number, guesses, begin, hl, hc, points)
        
def main(points):
    print ("MAIN MENU")
    print ("HIGH SCORES")
    print ("Higher and Lower = %d" % max(scores))
    say("Do you want to play freeplay or try to beat your high score on levels")
    name = raw_input("Type freeplay or levels here or to exit type exit:")
    if name == "freeplay":
        freePlay()
    elif name == "levels":
        levels(points)
    elif name == "exit":
        exit
        exit
def start():
    say("If you want to play guess the number with higher and lower type h if you want to play hotter or colder type c to go to main menu type main")
    say("type close to exit at anytime during a game")
def newGame():
    say("Would you like to play again type yes or no")
    restart = raw_input("Type here:")
    if restart == "yes":
        main(points)
    elif restart == "no":
        exit
    else:
        newGame()



points = 0

print (points)
main(points)
