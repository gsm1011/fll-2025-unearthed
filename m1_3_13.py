
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

    br.driveForDistance(distance=820, speedPct=60)
    br.turnInPlace(angle=90, speedPct=50)
    
    br.hub.display.number(3)
    br.moveLeftAttachmentMotorForDegrees(degrees=120, speedPct=30)
    br.driveForDistance(distance=200, speedPct=60)
    
    # do the lift
    br.moveLeftAttachmentMotorForDegrees(degrees=-120, speedPct=100)
    
    # back and go for mission 13
    br.hub.display.number(13)
    br.driveForDistance(distance=-200, speedPct=60)
    
    br.turnInPlace(angle=25, speedPct=50)
    br.driveForDistance(distance=250, speedPct=60)
    br.moveLeftAttachmentMotorForDegrees(degrees=120, speedPct=20)
    br.driveForDistance(distance=50, speedPct=60)
    
    # lift the statue
    br.moveLeftAttachmentMotorForDegrees(degrees=-90, speedPct=30)
    
    # back home
    br.turnInPlace(angle=-25, speedPct=50)
    br.driveForDistance(distance=-300, speedPct=60)
    br.turnInPlace(angle=-90, speedPct=50)
    br.driveForDistance(distance=-700, speedPct=60)
    
    return
    wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
