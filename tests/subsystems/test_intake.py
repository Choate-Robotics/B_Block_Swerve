from robot_systems import Robot
import constants

intake = Robot.intake
intake.init()

# def test_init_pos():
#     assert abs(intake.getIntakePosition() - constants.intake_init_pos) <= intake.tolerance

# def test_deploy_pos():
#     intake.deploy()
#     assert intake.target == constants.intake_deploy_pos

# def test_retract_pos():
#     intake.retract()
#     assert intake.target == constants.intake_retract_pos