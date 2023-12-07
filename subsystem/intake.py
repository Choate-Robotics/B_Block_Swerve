import config
import constants
import math
from robotpy_toolkit_7407.motors import TalonConfig, TalonFX
from robotpy_toolkit_7407 import Subsystem


INTAKE_CONFIG = TalonConfig(1, 0, 1, 0)

class Intake(Subsystem):

    

    def __init__(self):
        super().__init__()
        self.roller_motor: TalonFX = TalonFX(config.roller_id)
        self.hinge_motor: TalonFX = TalonFX(config.hinge_id, config=INTAKE_CONFIG)
        self.deployed: bool = False
        self.target: float
        self.tolerance: float = math.radians(0.5) #radians

    def zero_intake(self):
        self.hinge_motor.set_sensor_position(0)

    def init(self):
        self.roller_motor.init()
        self.hinge_motor.init()
        self.zero_intake()

    def set_intake_angle(self, angle):
        # angle param: radians
        self.hinge_motor.set_target_position(angle * constants.intake_gear_ratio)

    def rotate_intake(self, speed):
        self.hinge_motor.set_target_velocity(speed)

    def set_roller_velocity(self, speed):
        self.roller_motor.set_target_velocity(speed)
    
    def get_intake_angle(self):
        # Returns angle in radians
        return self.hinge_motor.get_sensor_position() / constants.intake_gear_ratio
        
    def is_at_angle(self, angle):
        #angle param: radians
        return abs(self.get_intake_angle() - angle) < self.tolerance
    
    def get_roller_velocity(self):
        return self.roller_motor.get_sensor_velocity()
