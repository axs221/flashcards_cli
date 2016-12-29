import sys
import os
import pickle

def load():
    path = "flashcards.pkl"
    default = list()

    if os.path.isfile(path):
        with open(path, "rb") as f:
            try:
                return pickle.load(f)
            except StandardError:
                pass
    with open(path, "wb") as f:
        pickle.dump(default, f)
    return default

def save(flashcards):
    pickle.dump( flashcards, open( "flashcards.pkl", "wb" ) )

def add_new(flashcards):
    front = raw_input("Front of card?")
    back = raw_input("Back of card?")

    flashcards.append((front, back))

    save(flashcards)

def quiz(flashcards):
    if len(flashcards) == 0:
        print "No flashcards were found, exiting..."
        sys.exit()

    for card in flashcards:
        print
        print card[0]
        print
        raw_input()
        print
        print card[1]
        print
        print "---------------------"
        print
        print "Type 'q' to quit, or press enter to continue"
        answer = raw_input()

        if answer == 'q':
            return

def main():
    flashcards = load()
    answer = None

    while answer != 'quit':
        if len(flashcards) == 0:
            answer = "a"
        else:
            print "Would you like to [q]uiz yourself, or [a]dd new cards, or [quit]?"
            answer = raw_input()

        if answer == "q" or answer == "quiz":
            quiz(flashcards)
        elif answer == "a" or answer == "add":
            add_new(flashcards)


main()
