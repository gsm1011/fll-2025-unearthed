
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.display.number(1)
    br.hub.speaker.beep()

    br.driveForward(distance=790, speedPct=60)
    br.turnRightInPlace(angle=90, speedPct=50)
    
    br.hub.display.number(3)
    br.lowerLeftArm(degrees=120, speedPct=30)
    br.driveForward(distance=230, speedPct=60)
    
    # lift the cart
    br.raiseLeftArm(degrees=150, speedPct=20)
    
    # back and go for mission 13
    br.hub.display.number(13)
    br.driveBackward(distance=50, speedPct=60)
    br.turnRightInPlace(angle=32, speedPct=50)
    br.driveForward(distance=110, speedPct=60)
    br.lowerLeftArm(degrees=120, speedPct=20)
    br.driveForward(distance=70, speedPct=60)

    # lift the statue
    br.raiseLeftArm(degrees=120, speedPct=40)
    wait(500)
    
    # back home
    br.hub.display.char('H')
    br.turnLeftInPlace(angle=23, speedPct=50)
    # br.curve(radius=350, angle=-120, speedPct=50)
    br.driveBackward(distance=300, speedPct=60)
    br.turnLeftInPlace(angle=100, speedPct=50)
    br.driveBackward(distance=700, speedPct=60)
    
    return
    wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
