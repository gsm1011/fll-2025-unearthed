
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
    br.driveForDistance(distance=680, speedPct=60)
    br.turnInPlace(angle=-45, speedPct=50)
    br.driveForDistance(distance=-50, speedPct=100)
    br.moveLeftAttachmentMotorForDegrees(degrees=55, speedPct=20)
    wait(1000)
    br.driveForDistance(distance=60, speedPct=100)
    br.moveLeftAttachmentMotorForDegrees(degrees=-75, speedPct=20)
    
    # push soil back
    br.driveForDistance(distance=200, speedPct=60)
    
    # br.turnInPlace(angle=-45, speedPct=50)
    br.driveForDistance(distance=-200, speedPct=100)
    # br.moveLeftAttachmentMotorForDegrees(degrees=-55, speedPct=30)
    
    # drive home
    # br.driveForDistance(distance=-100, speedPct=100)
    br.turnInPlace(angle=55, speedPct=50)
    br.driveForDistance(distance=-750, speedPct=60)
    
    wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
