
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
    
    br.driveForDistance(distance=-550, speedPct=60)
    #going to the other base
    br.turnInPlace(angle=-20, speedPct=50)
    br.driveForDistance(distance=700, speedPct=60)
    br.turnInPlace(angle=-15, speedPct=50)
    br.driveForDistance(distance=250, speedPct=60)
    #hit mission 10
    br.moveLeftAttachmentMotorForDegrees(degrees=90, speedPct=30)
    br.moveLeftAttachmentMotorForDegrees(degrees=-90, speedPct=30)
    br.turnInPlace(angle=-15, speedPct=50)
    br.moveLeftAttachmentMotorForDegrees(degrees=90, speedPct=30)
    br.moveLeftAttachmentMotorForDegrees(degrees=-90, speedPct=30)
    br.turnInPlace(angle=-15, speedPct=50)
    br.moveLeftAttachmentMotorForDegrees(degrees=90, speedPct=30)
    br.moveLeftAttachmentMotorForDegrees(degrees=-90, speedPct=30)
    br.turnInPlace(angle=30, speedPct=50)
    
    
    #back home
    br.driveForDistance(distance=-250, speedPct=60)
    br.turnInPlace(angle=35, speedPct=50)
    br.moveLeftAttachmentMotorForDegrees(degrees=-60, speedPct=30)
    br.driveForDistance(distance=1000, speedPct=60)
    br.turnInPlace(angle=90, speedPct=50)
    br.driveForDistance(distance=100, speedPct=60)
    
    
    
    wait(1000)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
