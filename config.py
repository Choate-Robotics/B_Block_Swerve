from dataclasses import dataclass

from units.SI import (
    inches_to_meters,
    meters,
    meters_per_second,
    meters_per_second_squared,
    radians,
)

# Drivetrain
front_left_move_id = 1
front_left_turn_id = 2
front_left_encoder_port = 1
front_left_encoder_zeroed_pos = 0

front_right_move_id = 3
front_right_turn_id = 4
front_right_encoder_port = 2
front_right_encoder_zeroed_pos = 0

back_left_move_id = 5
back_left_turn_id = 6
back_left_encoder_port = 3
back_left_encoder_zeroed_pos = 0

back_right_move_id = 7
back_right_turn_id = 8
back_right_encoder_port = 4
back_right_encoder_zeroed_pos = 0

driver_centric: bool = True
drivetrain_reversed: bool = False

# Gyro
gyro_id = 0