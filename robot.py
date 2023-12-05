import math

import commands2
import ctre
import wpilib
from wpilib import SmartDashboard

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
        # Gyro
        SmartDashboard.putNumber("Gyro Angle", Robot.drivetrain.gyro.get_robot_heading().degrees())

        # Encoder positions
        SmartDashboard.putNumber("Front Left Encoder", Robot.drivetrain.n_front_left.get_encoder_position())
        SmartDashboard.putNumber("Front Right Encoder", Robot.drivetrain.n_front_right.get_encoder_position())
        SmartDashboard.putNumber("Back Left Encoder", Robot.drivetrain.n_back_left.get_encoder_position())
        SmartDashboard.putNumber("Back Right Encoder", Robot.drivetrain.n_back_right.get_encoder_position())

        # Motor angle
        SmartDashboard.putNumber("Front Left Motor Angle", Robot.drivetrain.n_front_left.get_motor_angle().degrees())
        SmartDashboard.putNumber("Front Right Motor Angle", Robot.drivetrain.n_front_right.get_motor_angle().degrees())
        SmartDashboard.putNumber("Back Left Motor Angle", Robot.drivetrain.n_back_left.get_motor_angle().degrees())
        SmartDashboard.putNumber("Back Right Motor Angle", Robot.drivetrain.n_back_right.get_motor_angle().degrees())

        # Motor velocity
        SmartDashboard.putNumber("Front Left Motor Velocity", Robot.drivetrain.n_front_left.get_motor_velocity())
        SmartDashboard.putNumber("Front Right Motor Velocity", Robot.drivetrain.n_front_right.get_motor_velocity())
        SmartDashboard.putNumber("Back Left Motor Velocity", Robot.drivetrain.n_back_left.get_motor_velocity())
        SmartDashboard.putNumber("Back Right Motor Velocity", Robot.drivetrain.n_back_right.get_motor_velocity())

        commands2.CommandScheduler.getInstance().run()

    def teleopInit(self):
        # Test gyro
        Robot.drivetrain.gyro.reset_angle()

        # Test zeroing
        # Robot.drivetrain.n_front_left.zero()
        # Robot.drivetrain.n_front_right.zero()
        # Robot.drivetrain.n_back_left.zero()
        # Robot.drivetrain.n_back_right.zero()

        # Test raw output
        # Robot.drivetrain.n_front_left.raw_output(0.5)
        # Robot.drivetrain.n_front_right.raw_output(0.5)
        # Robot.drivetrain.n_back_left.raw_output(0.5)
        # Robot.drivetrain.n_back_right.raw_output(0.5)

        # Test set motor angle
        # Robot.drivetrain.n_front_left.set_motor_angle(math.radians(90))
        # Robot.drivetrain.n_front_right.set_motor_angle(math.radians(90))
        # Robot.drivetrain.n_back_left.set_motor_angle(math.radians(90))
        # Robot.drivetrain.n_back_right.set_motor_angle(math.radians(90))

        # Test set motor velocity
        # Robot.drivetrain.n_front_left.set_motor_velocity(0.5)
        # Robot.drivetrain.n_front_right.set_motor_velocity(0.5)
        # Robot.drivetrain.n_back_left.set_motor_velocity(0.5)
        # Robot.drivetrain.n_back_right.set_motor_velocity(0.5)

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
