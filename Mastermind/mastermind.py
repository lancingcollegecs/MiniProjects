"""Game of Mastermind, challenging the user to guess a four item
code from a simple scoring system."""
import random


def score(code, guess):
    """Return list of black and white pegs for correctly coloured pegs in
    the correct location (black) or incorrect location (white)"""
    code, guess = list(code), list(guess)
    # check guesses in the right place
    black = 0
    for c, g in zip(code, guess):
        if c == g:
            black += 1
    white = 0
    for c in guess:
        if c in code:
            code.remove(c)
            white += 1
    white = white - black     # remove duplicates
    return "".join(list('b' * black + 'w' * white))

def show_instructions():
    """Print game instructions"""
    print("""Mastermind

    Guess the code. The computer will make a four colour code that you
    cat try to guess. For each colour you get in the right location, you 
    will see one 'black' peg. For the correct colour in the wron place, 
    a 'white' peg. 
    """)


def main():
    colours = list("roygbv")
    show_instructions()
    code = random.choices(colours, k=4)
    print(code)

if __name__ == '__main__':
    main()
