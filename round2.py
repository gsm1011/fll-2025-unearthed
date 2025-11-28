
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.display.number(2)
    br.hub.speaker.beep()

    br.driveForDistance(distance=400, speedPct=80)
    br.turnInPlace(angle=-45, speedPct=50)
    br.driveForDistance(distance=350, speedPct=50)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
