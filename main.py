"""
Mini LED Matrix Heartbeat Project for Valentine's Day

A MicroPython script to drive a MAX7219 8x8 LED matrix
using the Raspberry Pi Pico to display with custom animations,
heartbeats, and a terminal-based command interface.

Usage:
- Runs a main animation loop by default.
- Break loop (Ctrl+C) to enter terminal command mode.

Copyright (c) 2026 Austin Driggs
"""



from time import sleep
from machine import Pin, SPI

import max7219
import hearts
import drawings
import alphabet



# initialize spi
spi0_sck = Pin(2)
spi0_tx = Pin(3)
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=spi0_sck, mosi=spi0_tx, miso=None)
spi0_csn = Pin(1, Pin.OUT)

# initialize matrix
num_of_panels = 1
display = max7219.Matrix8x8(spi, spi0_csn, num_of_panels)

## initialize buttons
button_love = Pin(10, Pin.IN, Pin.PULL_DOWN)
button_heart = Pin(11, Pin.IN, Pin.PULL_DOWN)



# command dictionary for terminal use
commands = {
    "hello": drawings.hello_world,
    "blink": drawings.blink_heartbeat,
    "cycle": drawings.hearbeat,
    "abet": drawings.cycle_alphabet,
    "emma": drawings.emma,
    "love": drawings.love,
    "vday": drawings.valentine
}



# def love_isr():
#     global love_pressed
#     love_pressed = True

# def heart_isr():
#     global heart_pressed
#     heart_pressed = True

def init_message():
    display.fill(0)
    drawings.hello_world(display)
    drawings.valentine(display)



if __name__ == "__main__":
    init_message()

    # button_love.irq(trigger=Pin.IRQ_RISING,handler=love_isr)
    # button_heart.irq(trigger=Pin.IRQ_RISING,handler=heart_isr)

    while True:
        # loop through main message
        try:
            drawings.hearbeat(display)
            drawings.love(display)
            drawings.emma(display)
            drawings.hearbeat(display)
        
        # options for developing and debugging
        except KeyboardInterrupt:
            print(f"list of commands: {list(commands.keys())}")
            while True:
                selection = input("enter a command: ")
                if selection in commands:
                    commands[selection](display)
                elif selection == "quit" or selection == "exit":
                    break
                else:
                    print(f"invalid command: {list(commands.keys())}")
