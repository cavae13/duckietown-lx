from typing import Tuple
import numpy as np

# Several attempts to set gain and const. With gain=0.1 and const=0.25, the speed is not too high and this fits well with the very simple matrix.

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[150:500, 325:500] = -1
    res[150:500, 150:325] = 1
# The matrix is very simple, only duckies in the vicinity are taken into account (150 to 500), those far away are not (white).
# Same concept for the sides, the robot concentrates for duckies approached from the front between 150 and 500, at the margins (1-150 and 500-650) they are not considered, still white as before.
# If a duckie is seen to the left, the robot will turn to the right, so the left wheel is accelerated (red = 1) and the right wheel is slowed down (blue = -1), same concept but in reverse in the case of a duckie seen to the right.
    return res

def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[150:500, 325:500] = 1
    res[150:500, 150:325] = -1
    return res
# With this set-up, the robot hit duckies in the centre of the field a few times, but 2 others reached the right-hand edge, committing a long diagonal run.










