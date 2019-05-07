"""Game of Mastermind, challenging the user to guess a four item
code from a simple scoring system."""
import random
MAX_GUESSES = 10

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
    will see one 'black' peg. For the correct colour in the wrong place, 
    a 'white' peg. 
    """)

def print_history(guesses, marks):
    """Prints the history of the guesses and the associated marks."""
    print('\n================\n  guess marks')
    for attempt, (g, m) in enumerate(zip(guesses, marks)):
        print(attempt + 1, g, m)


def main():
    colours = list("roygbv")
    guesses = []
    marks = []
    show_instructions()
    code = "".join(random.choices(colours, k=4))
    for attempt in range(MAX_GUESSES):
        guess = input("\nNext guess: ")
        mark = score(code, guess)
        marks.append(mark)
        guesses.append(guess)
        print_history(guesses, marks)
        if mark == "bbbb":
            print("Well done, you win!")
            break
    else: 
        print("The code was:", code)


if __name__ == '__main__':
    main()
