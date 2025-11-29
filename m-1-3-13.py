
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.display.number(4)
    br.hub.speaker.beep()

    # br.moveLeftAttachmentMotorForDegrees(degrees=55, speedPct=30)
    br.driveForDistance(distance=800, speedPct=60)
    # br.driveForDistance(distance=-100, speedPct=60)
    # br.driveForDistance(distance=150, speedPct=60)
    # br.driveForDistance(distance=-700, speedPct=60)
    br.turnInPlace(angle=90, speedPct=50)
    
    br.moveLeftAttachmentMotorForDegrees(degrees=90, speedPct=30)
    br.driveForDistance(distance=200, speedPct=60)
    
    # do the lift
    br.moveLeftAttachmentMotorForDegrees(degrees=-120, speedPct=30)
    # br.moveLeftAttachmentMotorForDegrees(degrees=120, speedPct=50)
    
    # back and go for mission 13
    br.driveForDistance(distance=-200, speedPct=60)
    br.moveLeftAttachmentMotorForDegrees(degrees=120, speedPct=50)
    br.turnInPlace(angle=25, speedPct=50)
    br.driveForDistance(distance=300, speedPct=60)
    
    # back home
    br.turnInPlace(angle=-25, speedPct=50)
    br.driveForDistance(distance=-300, speedPct=60)
    br.turnInPlace(angle=-90, speedPct=50)
    br.driveForDistance(distance=-650, speedPct=60)
    
    return
    wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
