from robotpy_toolkit_7407.utils.units import (
    mile,
    hour,
    m,
    s,
    rev,
    rad
)

# Drivetrain
drivetrain_turn_gear_ratio = 6.8
# drivetrain_move_gear_ratio = 6.8
drivetrain_move_gear_ratio_as_rotations_per_meter = 1
track_width = 1
drivetrain_max_vel = (20 * mile / hour).asNumber(m / s)
drivetrain_max_target_accel = (45 * mile / hour).asNumber(m / s)
drivetrain_max_angular_vel = (1 * rev / s).asNumber(rad / s)

# Intake
intake_gear_ratio = 100 / 1
