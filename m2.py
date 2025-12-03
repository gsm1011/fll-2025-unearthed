
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

    br.driveForward(distance=690, speedPct=60)
    br.turnLeftInPlace(angle=45, speedPct=50)
    br.driveBackward(distance=50, speedPct=100)
    wait(500)
    br.driveForward(distance=80, speedPct=100)
    br.raiseLeftArm(degrees=75, speedPct=20)
    
    # push soil back
    br.driveForward(distance=220, speedPct=60)
    
    br.driveBackward(distance=200, speedPct=100)
    
    # drive home
    br.turnRightInPlace(angle=55, speedPct=100)
    br.driveBackward(distance=750, speedPct=100)
    
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
