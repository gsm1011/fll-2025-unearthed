
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
    br.driveForDistance(distance=-120, speedPct=60)
    br.turnInPlace(angle=-45, speedPct=50)
    br.driveForDistance(distance=-270, speedPct=60)
    br.moveRightAttachmentMotorForDegrees(degrees=90, speedPct=10)
    br.moveRightAttachmentMotorForDegrees(degrees=-90, speedPct=10)
    
    
    # Go for mission 10
    br.hub.display.number(10)
    
    br.driveForDistance(distance=180, speedPct=40)
    br.turnInPlace(angle=-45, speedPct=40)
    br.driveForDistance(distance=-440, speedPct=40)
    br.turnInPlace(angle=90, speedPct=40)
    
    # down the hook and grab the cart
    br.driveForDistance(distance=-60, speedPct=40)
    #br.turnInPlace(angle=-10, speedPct=20)
    br.moveRightAttachmentMotorForDegrees(degrees=90, speedPct=20)
    
    # Drive back home with the cart
    br.driveForDistance(distance=80, speedPct=40)
    br.turnInPlace(angle=-80, speedPct=40)
    br.driveForDistance(distance=710, speedPct=100)

    # wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
