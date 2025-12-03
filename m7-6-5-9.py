
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.display.number(7)
    br.hub.speaker.beep()

    br.driveForDistance(distance=650, speedPct=60)
    br.turnRightInPlace(angle=45, speedPct=50)
    br.driveForward(distance=30, speedPct=50)
    br.lowerLeftArm(degrees=90, speedPct=20)
    br.driveForward(distance=55, speedPct=50)
    br.raiseLeftArm(degrees=120, speedPct=20)
    
    br.hub.display.number(6)
    br.turnLeftInPlace(angle=25, speedPct=50)
    
    br.hub.display.number(5)
    br.driveBackward(distance=100, speedPct=50)
    br.turnLeftInPlace(angle=15, speedPct=50)
    br.driveForward(distance=150, speedPct=50)
    br.turnLeftInPlace(angle=45, speedPct=50)
    
    br.hub.display.number(9)
    br.driveBackward(distance=50, speedPct=60)
    br.turnLeftInPlace(angle=50, speedPct=50)
    br.driveForward(distance=400, speedPct=60)
    br.turnRightInPlace(angle=24, speedPct=50)
    br.driveBackward(distance=300, speedPct=60)
    
    # go home.
    br.hub.display.char('H')
    br.driveForward(distance=200, speedPct=60)
    br.turnLeftInPlace(angle=35, speedPct=50)
    
    br.curve(radius=-480, angle=-60, speedPct=150)
    br.driveBackward(distance=500, speedPct=60)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
