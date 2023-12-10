from robotpy_toolkit_7407.command import SubsystemCommand
from subsystem import Intake
import config
import math

class SetIntake(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake, angle):
        super().__init__(subsystem)
        self.subsystem = subsystem
        self.angle = angle

    def initialize(self):
        self.subsystem.set_intake_angle(math.radians(self.angle))

    def execute(self):
        pass

    def isFinished(self):
        return self.subsystem.is_at_angle(self.angle)
    
    def end(self, interrupted):
        self.subsystem.set_intake_angle(self.subsystem.get_intake_angle())

class IntakeRoller(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake, speed: float):
        super().__init__(subsystem)
        self.subsystem = subsystem
        self.speed = speed

    def initialize(self):
        self.subsystem.set_roller_velocity(self.speed)

    def execute(self):
        pass

    def isFinished(self):
        return self.subsystem.get_roller_velocity() == self.speed

    def end(self, interrupted):
        pass