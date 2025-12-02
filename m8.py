
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.speaker.beep()
    br.hub.display.number(8)

    br.driveForward(distance=360, speedPct=80)
    
    # hammer to knock the silos.
    for i in range(3):
        br.lowerLeftArm(degrees=90, speedPct=80)
        br.raiseLeftArm(degrees=90, speedPct=80)
        wait(500)
    
    # Mission done, get back to home.
    br.driveBackward(distance=360, speedPct=80)

    # Mission end indication
    br.hub.speaker.beep()
    
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
