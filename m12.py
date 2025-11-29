
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

    # br.moveLeftAttachmentMotorForDegrees(degrees=55, speedPct=30)
    br.driveForDistance(distance=480, speedPct=60)
    br.driveForDistance(distance=-100, speedPct=60)
    br.moveLeftAttachmentMotorForDegrees(degrees=-75, speedPct=30)
    br.driveForDistance(distance=200, speedPct=60)
    
    br.driveForDistance(distance=-650, speedPct=60)
    
    wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
