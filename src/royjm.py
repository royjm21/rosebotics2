"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_spin_in_place_degrees()


def spin_in_place_degrees(self,
                              degrees,
                              duty_cycle_percent=100,
                              stop_action=StopAction.BRAKE):
        """
        Spin in place (i.e., both wheels move, in opposite directions)
        the given number of degrees, at the given speed (-100 to 100,
        where positive is clockwise and negative is counter-clockwise),
        stopping by using the given StopAction.
        """
        # TODO: Do a few experiments to determine the constant that converts
        # TODO:   from wheel-degrees-spun to robot-degrees-spun.
        # TODO:   Assume that the conversion is linear with respect to speed.
        robot = rb.Snatch3rRobot()
        robot.drive_system.left_wheel.start_moving(duty_cycle_percent)
        robot.drive_system.right_wheel.start_moving(-duty_cycle_percent)
        while True:
            if robot.drive_system.left_wheel.get_degrees_spun() > degrees:
                break


def run_test_spin_in_place_degrees():
    print('90 degree turn')
    spin_in_place_degrees(90)
    print('180 degree turn')
    spin_in_place_degrees(180)
    print('270 degree turn')
    spin_in_place_degrees(270)
    print('360 degree turn')
    spin_in_place_degrees(360)


main()
