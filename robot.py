import commands2
import ctre
import wpilib
import command
import config
import constants
import robot_systems
import sensors
import subsystem
import utils
from oi.OI import OI
from robot_systems import *


class _Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Command Scheduler
        period = .03
        commands2.CommandScheduler.getInstance().setPeriod(period)

        # Initialize subsystems
        Robot.drivetrain.init()

        # Sensors
        Sensors.gyro = Robot.drivetrain.gyro

        # Initialize Operator Interface
        OI.init()
        OI.map_controls()

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def teleopInit(self):
        Robot.drivetrain.n_front_left.zero()
        Robot.drivetrain.n_front_right.zero()
        Robot.drivetrain.n_back_left.zero()
        Robot.drivetrain.n_back_right.zero()

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(_Robot)
