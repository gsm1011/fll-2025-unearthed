
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

    
    br.driveForDistance(distance=550, speedPct=60)
    br.turnInPlace(angle=50, speedPct=50)
    br.driveForDistance(distance=200, speedPct=50)
    br.turnInPlace(angle=-90, speedPct=50)
    br.driveForDistance(distance=-70, speedPct=60)
    

    br.moveLeftAttachmentMotorForDegrees(degrees=130, speedPct=10)
    wait(600)
    
    br.driveForDistance(distance=80, speedPct=60)
    br.moveLeftAttachmentMotorForDegrees(degrees=-130, speedPct=20)
    br.turnInPlace(angle=-7, speedPct=50)
    
    
    br.driveForDistance(distance=215, speedPct=80)
    wait(500)
    br.driveForDistance(distance=-215, speedPct=80)
    
    # go back home
    br.driveForDistance(distance=-50, speedPct=80)
    br.turnInPlace(angle=55, speedPct=50)
    br.driveForDistance(distance=-700, speedPct=80)
        
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
