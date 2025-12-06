
from base_robot import *

# Check the robot setup and make sure everything is working.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.speaker.beep()
    br.hub.display.number(0)
    # Wait for the robot to be ready.
    # wait(500)

    br.hub.speaker.beep()
    br.hub.speaker.beep(330, 200)
    
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
