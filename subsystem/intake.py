import config
import constants
import math
from units.SI import radians
from robotpy_toolkit_7407.motors import TalonConfig, TalonFX
from robotpy_toolkit_7407 import Subsystem

INTAKE_CONFIG = TalonConfig(1, 0, 1, 0)


class Intake(Subsystem):

    def __init__(self):
        super().__init__()

        self.roller_motor: TalonFX = TalonFX(
            can_id=config.roller_id
        )
        self.hinge_motor: TalonFX = TalonFX(
            can_id=config.hinge_id,
            config=INTAKE_CONFIG
        )

        self.deployed: bool = False
        self.target: float
        self.tolerance: radians = math.radians(2)

    def init(self):
        self.roller_motor.init()
        self.hinge_motor.init()

    def set_intake_angle(self, angle: radians):
        self.hinge_motor.set_target_position(angle * constants.intake_gear_ratio)

    def get_intake_angle(self) -> radians:
        return self.hinge_motor.get_sensor_position() / constants.intake_gear_ratio

    def is_at_angle(self, angle: radians) -> bool:
        return abs(self.get_intake_angle() - angle) < self.tolerance

    def set_roller_velocity(self, speed):
        self.roller_motor.set_target_velocity(speed)

    def get_roller_velocity(self):
        return self.roller_motor.get_sensor_velocity()

    def zero_intake(self):
        self.hinge_motor.set_sensor_position(0)
