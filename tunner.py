
from base_robot import *

# Check the robot setup and make sure everything is working.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.speaker.beep()
    br.hub.display.number(0)
    # Wait for the robot to be ready.
    # wait(500)

    br.moveLeftAttachmentMotorForDegrees(degrees=-30)
    br.leftAttachmentMotor.reset_angle()
    
    br.moveRightAttachmentMotorForDegrees(speedPct=-30)
    br.rightAttachmentMotor.reset_angle()

    br.hub.speaker.beep()
    
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
