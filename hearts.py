"""
Mini LED Matrix Heart Assets

A collection of bitmask frames for heart animations on an 8x8 LED matrix.
Includes four sizes (small to huge) to facilitate heartbeat "pulsing" effects.
"""



small = [
    0b00000000,
    0b00000000,
    0b00000000,
    0b00100100,
    0b00111100,
    0b00011000,
    0b00000000,
    0b00000000 
]

regular = [
    0b00000000,
    0b01100110,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000,
    0b00000000 
]

large = [
    0b01100110,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000 
]

huge = [
    0b11100111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100 
]
