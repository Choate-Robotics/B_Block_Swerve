import config
import constants
from robotpy_toolkit_7407.motors import TalonConfig, TalonSRX
from robotpy_toolkit_7407 import Subsystem


PID = TalonConfig(1, 0, 1, 0)

class Intake(Subsystem):

    roller_motor: TalonSRX = TalonSRX(config.roller_id, config=PID)
    hinge_motor: TalonSRX = TalonSRX(config.hinge_id, config=PID)
    deployed: bool = False
    target: float
    tolerance: float = 0.02

    def __init__(self):
        super().__init__()
        self.deployed = False

    def init(self):
        self.roller_motor.init()
        self.hinge_motor.init()
        self.hinge_motor.set_sensor_position(constants.intake_init_pos)

    def deploy(self):
        self.target = constants.intake_deploy_pos
        self.hinge_motor.set_target_position(self.target)
        self.deployed = True

    def retract(self):
        self.target = constants.intake_retract_pos
        self.hinge_motor.set_target_position(self.target)
        self.deployed = False

    def intake(self):
        self.roller_motor.set_target_velocity(constants.intake_speed)

    def extake(self):
        self.roller_motor.set_target_velocity(-constants.intake_speed)

    def stop(self):
        self.roller_motor.set_target_velocity(0)

    def isDeployed(self):
        return self.deployed
    
    def getIntakePosition(self):
        return self.hinge_motor.get_sensor_position()
    
    def getTargetPosition(self):
        return self.target
    
    def getRollerVelocity(self):
        return self.roller_motor.get_sensor_velocity()
