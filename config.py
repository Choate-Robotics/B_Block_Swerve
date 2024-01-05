from dataclasses import dataclass

from units.SI import (
    inches_to_meters,
    meters,
    meters_per_second,
    meters_per_second_squared,
    radians,
)

# Drivetrain
front_left_move_id = 4
front_left_turn_id = 5
front_left_encoder_port = 1
front_left_encoder_zeroed_pos = 3.0514

front_right_move_id = 6
front_right_turn_id = 7
front_right_encoder_port = 0
front_right_encoder_zeroed_pos = 3.023127

back_left_move_id = 2
back_left_turn_id = 3
back_left_encoder_port = 2
back_left_encoder_zeroed_pos = 2.97

back_right_move_id = 8
back_right_turn_id = 9
back_right_encoder_port = 7
back_right_encoder_zeroed_pos = 2.9912

driver_centric: bool = True
drivetrain_reversed: bool = False

# Gyro
gyro_id = 13

# Intake
roller_id = 20
hinge_id = 10
intake_init_pos = 100
intake_deploy_pos = 0
intake_standard_pos = intake_init_pos
intake_roller_speed = 1
intake_idle_speed = 0