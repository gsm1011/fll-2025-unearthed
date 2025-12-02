
from base_robot import *
hub = PrimeHub()



from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Mission start indication
    br.hub.light.on(Color.GREEN)
    # br.hub.display.text('1')
    
    br.hub.speaker.beep()
    wait(1000)
    
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.leftAttachmentMotor.reset_angle()
    
    #mission8
    br.driveForDistance(distance=350, speedPct=60, then=Stop.BRAKE)
    br.hub.display.number(8)
    for i in range(4):
        br.moveLeftAttachmentMotorForDegrees(degrees=70, speedPct=60)
        br.moveLeftAttachmentMotorForDegrees(degrees=-70, speedPct=10)
        i + 1
        print(i,'slap')
    
    
    
    br.turnInPlace(angle=-35, speedPct=20)
    br.driveForDistance(distance=430, speedPct=50)
    br.turnInPlace(angle=110, speedPct=20)
    #ms6
    br.hub.display.number(6)
    br.moveLeftAttachmentMotorForDegrees(degrees=50, speedPct=20)
    br.turnInPlace(angle=-50, speedPct=30)
    
    #ms5
    br.hub.display.number(5)
    br.driveForDistance(distance=-40, speedPct=50)
    br.moveLeftAttachmentMotorForDegrees(degrees=20, speedPct=20)
    br.turnInPlace(angle=-50, speedPct=100)
    
    br.turnInPlace(angle=50, speedPct=20)
    br.turnInPlace(angle=-60, speedPct=100)
    
    br.turnInPlace(angle=30, speedPct=20)
    br.moveLeftAttachmentMotorForDegrees(degrees=-70, speedPct=20)
    br.turnInPlace
    
    
    





        
    




if __name__ == "__main__":
    br = BaseRobot()
    Run(br)