from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT) # Ensuring that the correct pin is selected for the LED

# Defining the length of dot, dash and spaces 
dot = 0.2
dash = dot * 3
space = dot * 7

# Defining the duration for dot and dash based on the characters
duration = {"." : dot, "-" : dash}

# Creating the morse code dictionary
MORSE_CODE_DICT = {
    "a" : ".-",   "b" : "-...",  "c" : "-.-.",
    "d" : "-..",  "e" : ".",     "f" : "..-.",
    "g" : "--.",  "h" : "....",  "i" : "..",
    "j" : ".---", "k" : "-.-",   "l" : ".-..",
    "m" : "--",   "n" : "-.",    "o" : "---",
    "p" : ".--.", "q" : "--.-",  "r" : ".-.",
    "s" : "...",  "t" : "-",     "u" : "..-",
    "v" : "...-", "w" : ".--",   "x" : "-..-",
    "y" : "-.--", "z" : "--.."
}

def blink(dotdash):
    if dotdash == '.':
        delay = dot
    else:
        delay = dash
    led.on()
    sleep(delay)
    led.off()
    sleep(delay)

def send_morse(character):
    if character == ' ':
        sleep(space)
    else:
        dots_an_dashes = MORSE_CODE_DICT.get(character.lower())
        if dots_an_dashes:
            print(character + " " + dots_an_dashes)
            for pulse in dots_an_dashes:
                blink(pulse)
            sleep(dash)
        else:
            print("unknown character: " + character)