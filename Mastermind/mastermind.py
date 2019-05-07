"""Game of Mastermind, challenging the user to guess a four item
code from a simple scoring system."""
# from random import choices


def score(code, guess):
    """Return list of black and white pegs for correctly coloured pegs in
    the correct location (black) or incorrect location (white)"""
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
    return list('b' * black + 'w' * white)
