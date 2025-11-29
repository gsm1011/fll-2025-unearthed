
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.speaker.beep()
    br.hub.display.number(1)
    # Wait for the robot to be ready.
    # wait(500)
    
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # straight line test.
    br.driveForDistance(distance=380, speedPct=80)
    
    # hammer to knock the silos.
    # for i in range(3):
    #     br.moveLeftAttachmentMotorForDegrees(degrees=45, speedPct=100)
    #     wait(500)
    #     br.moveLeftAttachmentMotorForDegrees(degrees=-45, speedPct=100)
    #     wait(500)

    # Go for the next mission.
    br.turnInPlace(angle=-45, speedPct=50)
    br.driveForDistance(distance=350, speedPct=50)
    br.turnInPlace(angle=90, speedPct=50)
    br.driveForDistance(distance=60, speedPct=80)
    
    # Lower arm for levers.
    br.moveLeftAttachmentMotorForDegrees(degrees=35, speedPct=10)
    br.turnInPlace(angle=-80, speedPct=80)
    
    # MIssion down, get back to home.
    br.moveLeftAttachmentMotorForDegrees(degrees=-45, speedPct=50)
    br.driveForDistance(distance=-600, speedPct=80)

    # Mission end indication
    br.hub.speaker.beep()
    
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
