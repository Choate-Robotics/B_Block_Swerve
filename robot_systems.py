from robotpy_toolkit_7407.subsystem_templates.drivetrain import SwerveGyro

import subsystem
import sensors
import wpilib


class Robot:
    drivetrain = subsystem.Drivetrain()
    intake = subsystem.Intake()


class Pneumatics:
    pass


class Sensors:
    gyro: SwerveGyro
