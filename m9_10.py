
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    
    br.hub.speaker.beep()

    # Moving backwards
    br.hub.display.number(9)
    br.driveForward(distance=110, speedPct=60)
    br.turnLeftInPlace(angle=50, speedPct=50)
    br.driveForward(distance=355, speedPct=60)
    br.lowerLeftArm(degrees=90, speedPct=10)
    br.raiseLeftArm(degrees=90, speedPct=10)
    
    
    # Go for mission 10
    br.hub.display.number(10)
    br.driveBackward(distance=185, speedPct=40)
    br.turnLeftInPlace(angle=45, speedPct=40)
    br.driveForward(distance=460, speedPct=40)
    br.turnRightInPlace(angle=90, speedPct=40)
    
    # down the hook and grab the cart
    br.driveForward(distance=83, speedPct=40)
    br.lowerLeftArm(degrees=90, speedPct=20)
    
    # Drive back home with the cart
    br.driveBackward(distance=98, speedPct=40)
    br.turnLeftInPlace(angle=85, speedPct=40)
    br.driveBackward(distance=710, speedPct=100)

    # wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
