# Imports
import time
import random
from machine import Pin
from neopixel import NeoPixel

# Define the RGB LEDs
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

#def act7():
#s = 0.25
leds = [GRBled1, GRBled2]

while True:

    for i in range(24):
    
        g = random.randint(0,255)
        r = random.randint(0,255)
        b = random.randint(0,255)
        led = random.randint(0,1)
        
        leds[led].fill(((g,r,b)))
        leds[led].write()
        time.sleep(0.5)
        
        time.sleep(0.5)
        GRBled1.fill(((0,0,0)))
        GRBled1.write()
        GRBled2.fill(((0,0,0)))
        GRBled2.write()