from time import sleep

from adafruit_dotstar import DotStar
from adafruit_debouncer import Button, Debouncer
from adafruit_ticks import ticks_ms, ticks_add, ticks_less

from board import A0, A2, APA102_MOSI, APA102_SCK, D2
from digitalio import DigitalInOut, Direction
from touchio import TouchIn

COLORS = [
    (0, 255, 0),
    (0, 0, 255),
    (255, 0, 0),
    (0, 255, 255),
    (255, 255, 0),
    (255, 0, 255),
    (255, 255, 255),
]

leds_touch = TouchIn(A0)
leds_switch = Debouncer(leds_touch)
leds_button = Button(leds_touch, value_when_pressed=True, long_duration_ms=2000)

leds = DigitalInOut(D2)
leds.direction = Direction.OUTPUT

dots_touch = TouchIn(A2)
dots_switch = Debouncer(dots_touch)
dots_button = Button(dots_touch, value_when_pressed=True, long_duration_ms=2000)

dotstar = DotStar(APA102_SCK, APA102_MOSI, 1)

DOTSTAR_OFF = 0
DOTSTAR_SOLID = 1
DOTSTAR_TOUCH = 2
DOTSTAR_GLOW = 3
DOTSTAR_CYCLE = 4
NUM_DOTSTAR_MODES = 5
dotstar_mode = DOTSTAR_OFF

color_index = 0
color = COLORS[color_index % len(COLORS)]

MAX_BRIGHTNESS = 0.2
MIN_BRIGHTNESS = 0.0
MIN_GLOW_BRIGHTNESS = 0.05

GLOW_STEP = 0.01
GLOW_BRIGHTER = 0
GLOW_DIMMER = 1
glow_state = GLOW_BRIGHTER
glow_brightness = MIN_GLOW_BRIGHTNESS

next_update = ticks_add(ticks_ms(), 1000)

LEDS_OFF = 0
LEDS_SOLID = 1
LEDS_TOUCH = 2
NUM_LED_MODES = 3
leds_mode = LEDS_SOLID

while True:
    dots_switch.update()
    dots_button.update()

    leds_switch.update()
    leds_button.update()

    #
    # DOTSTAR
    # 

    if dots_button.long_press:
        dotstar_mode = (dotstar_mode + 1) % NUM_DOTSTAR_MODES
        print(dotstar_mode)

    if dotstar_mode == DOTSTAR_OFF:
        dotstar.brightness = MIN_BRIGHTNESS
        dotstar.show()

    elif dotstar_mode == DOTSTAR_SOLID:
        dotstar.brightness = MAX_BRIGHTNESS
        dotstar.fill(color)

        if dots_switch.fell and not dots_button.long_press:
            color_index = (color_index + 1) % len(COLORS)
            color = COLORS[color_index]

    elif dotstar_mode == DOTSTAR_TOUCH:
        dotstar.brightness = MAX_BRIGHTNESS if dots_switch.value else MIN_BRIGHTNESS
        dotstar.fill(color)       
        
        
    elif dotstar_mode == DOTSTAR_GLOW:

        if ticks_less(ticks_ms(), next_update):
            continue

        next_update = ticks_add(ticks_ms(), 200)

        glow_brightness += GLOW_STEP if glow_state == GLOW_BRIGHTER else -GLOW_STEP

        if glow_brightness <= MIN_GLOW_BRIGHTNESS:
            glow_state = GLOW_BRIGHTER
        elif glow_brightness >= MAX_BRIGHTNESS:
            glow_state = GLOW_DIMMER

        dotstar.brightness = glow_brightness
        dotstar.fill(color)

        print(dotstar.brightness)

    elif dotstar_mode == DOTSTAR_CYCLE:
        dotstar.brightness = 0.1
        dotstar.fill(color)

        if not ticks_less(ticks_ms(), next_update):
            color_index = (color_index + 1) % len(COLORS)
            color = COLORS[color_index]
            next_update = ticks_add(ticks_ms(), 1000)
        
    else:
        pass

    
    #
    # LEDs
    #

    if leds_button.long_press:
        leds_mode = (leds_mode + 1) % NUM_LED_MODES
        print("LED Mode:", leds_mode)

    if leds_mode == LEDS_OFF:
        leds.value = False

    elif leds_mode == LEDS_SOLID:
        leds.value = True

    elif leds_mode == LEDS_TOUCH:
        leds.value = True if leds_switch.value else False

    else:
        pass
