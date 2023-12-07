from robotpy_toolkit_7407.utils import logger
from oi.keymap import Keymap
from robot_systems import Robot
import config, constants, math, command, commands2
from commands2 import InstantCommand

logger.info("Hi, I'm OI!")


class OI:
    @staticmethod
    def init() -> None:
        logger.info("Initializing OI...")

    @staticmethod
    def map_controls():
        logger.info("Mapping controls...")
        
        def intake_deploy():
            Robot.intake.set_intake_angle(math.radians(config.intake_deploy_pos))
            Robot.intake.set_roller_velocity(config.intake_roller_speed)

        def intake_idle():
            Robot.intake.set_intake_angle(math.radians(config.intake_standard_pos))
            Robot.intake.set_roller_velocity(config.intake_idle_speed)

        def intake_rotate(speed):
            Robot.intake.rotate_intake(speed)

        def zero_intake():
            Robot.intake.zero_intake()

        Keymap.Intake.DEPLOY_INTAKE.whileTrue(InstantCommand(intake_deploy)).onFalse(InstantCommand(intake_idle))

        Keymap.Intake.ZERO_INTAKE.onTrue(zero_intake)

        Keymap.Intake.INTAKE_UP.whileTrue(InstantCommand(intake_rotate(config.intake_roller_speed))).onFalse(InstantCommand(intake_rotate(0)))

        Keymap.Intake.INTAKE_DOWN.whileTrue(InstantCommand(intake_rotate(-config.intake_roller_speed))).onFalse(InstantCommand(intake_rotate(0)))
