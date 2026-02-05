"""
Mini LED Matrix Animation Library

A collection of high-level animation functions for an 8x8 LED matrix.
Handles text rendering, heart animations, and custom message sequences.
"""



import max7219
from time import sleep
import hearts
import alphabet



def print_word(display, word, length, delay):
    display.fill(0)
    display.show()

    for char in word:
        display.bitmap(char)
        sleep(length)
        display.fill(0)
        display.show()

    display.fill(0)
    display.show()
    sleep(delay)


def hello_world(display):
    hello = [alphabet.letter['H'], alphabet.letter['E'], alphabet.letter['L'], alphabet.letter['L'], alphabet.letter['O']]
    print_word(display, hello, 0.5, 0.5)


def blink_heartbeat(display):
    for i in range(3):
        display.bitmap(hearts.regular)
        display.show()
        sleep(1)
        display.fill(0)
        display.show()
        sleep(0.1)
        display.bitmap(hearts.regular)
        display.show()
        sleep(0.5)
        display.fill(0)
        display.show()
        sleep(0.1)


def hearbeat(display):
    display.fill(0)
    display.show()

    for i in range(3):
        frames = [hearts.small, hearts.regular, hearts.large, hearts.huge]

        for frame in frames:
            display.bitmap(frame)
            sleep(0.1)

        for frame in reversed(frames):
            display.bitmap(frame)
            sleep(0.1)

    display.fill(0)
    display.show()


def cycle_alphabet(display):
    for char in sorted(alphabet.letter.keys()):
        bitmap = alphabet.letter[char]
        
        display.bitmap(bitmap)
        sleep(0.5)
    
    display.fill(0)
    display.show()


def love(display):
    love = [alphabet.letter['I'], hearts.regular, alphabet.letter['U']]
    print_word(display, love, 0.5, 0.3)


def emma(display):
    emma = [alphabet.letter['E'], alphabet.letter['M'], alphabet.letter['M'], alphabet.letter['A']]
    print_word(display, emma, 0.5, 0.2)


def valentine(display):
    happy = [alphabet.letter['H'], alphabet.letter['A'], alphabet.letter['P'], alphabet.letter['P'], alphabet.letter['Y']]
    valentines = [alphabet.letter['V'], alphabet.letter['A'], alphabet.letter['L'], alphabet.letter['E'], alphabet.letter['N'],
                    alphabet.letter['T'], alphabet.letter['I'], alphabet.letter['N'], alphabet.letter['E'], alphabet.letter['S']]
    day = [alphabet.letter['D'], alphabet.letter['A'], alphabet.letter['Y']]

    print_word(display, happy, 0.5, 0.2)
    print_word(display, valentines, 0.5, 0.2)
    print_word(display, day, 0.5, 0.5)
