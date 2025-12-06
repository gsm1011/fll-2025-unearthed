from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
from base_robot import *

# Initialize the hub
hub = PrimeHub()

# Set the initial number
current_number = 0
MAX_NUMBER = 10

# Initialize sets for edge detection
was_pressed = set()
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

br = BaseRobot()
br.hub.speaker.beep()

while True:
    # Display the current number on the hub matrix
    hub.display.number(current_number)
    # print(f'Current number: {current_number}')
    # hub.display.text(str(current_number), on=5000, off=0)

    # Get the current state of pressed buttons
    is_pressed = set(hub.buttons.pressed())

    # Check for a single tap of the RIGHT button to increment the number
    if Button.RIGHT in is_pressed and Button.RIGHT not in was_pressed:
        if current_number < MAX_NUMBER:
            current_number += 1
            # Optional: Play a short sound on change
            hub.speaker.beep(440, 50)

    # Check for a single tap of the LEFT button to decrement the number
    if Button.LEFT in is_pressed and Button.LEFT not in was_pressed:
        if current_number >= 1:
            current_number -= 1
            # Optional: Play a short sound on change
            hub.speaker.beep(220, 50)
            
    if Button.CENTER in is_pressed and Button.CENTER not in was_pressed:
        print(f'Running mission: {current_number}')
        hub.speaker.beep(330, 200)
        if current_number == 0:
            from tunner import Run
            Run(br)
        if current_number == 1:
            from m2 import Run
            Run(br)
        if current_number == 2:
            from m1_3_13 import Run
            Run(br)
        if current_number == 3:
            from m12 import Run 
            Run(br)
        if current_number == 4:
            from m9_10 import Run 
            Run(br)
        if current_number == 5:
            from m7_6_5 import Run
            Run(br)
        if current_number == 6:
            from m8 import Run
            Run(br)
        elif current_number >= 7:
            br.hub.speaker.beep(100, 500)  # Indicate no mission available

    # Update the previous state for the next iteration
    was_pressed = is_pressed

    # Wait briefly to prevent the loop from running too fast
    wait(100)
