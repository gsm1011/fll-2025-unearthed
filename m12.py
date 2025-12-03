
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.display.number(12)
    br.hub.speaker.beep()

    br.driveForward(distance=440, speedPct=60)
    br.driveBackward(distance=150, speedPct=60)
    br.raiseLeftArm(degrees=120, speedPct=30)
    
    br.driveBackward(distance=50, speedPct=60)
    br.turnLeftInPlace(angle=30, speedPct=50)
    br.driveForward(distance=250, speedPct=60)
    br.turnRightInPlace(angle=28, speedPct=50)
    br.driveForward(distance=220, speedPct=60)
    
    # back to base.
    br.hub.display.char('H')
    br.driveBackward(distance=80, speedPct=100)
    br.turnLeftInPlace(angle=20, speedPct=50)
    br.curve(radius=1200, angle=58, speedPct=100)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
