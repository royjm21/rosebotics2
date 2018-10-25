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
                              stop_action=rb.StopAction.BRAKE):
        """
        Spin in place (i.e., both wheels move, in opposite directions)
        the given number of degrees, at the given speed (-100 to 100,
        where positive is clockwise and negative is counter-clockwise),
        stopping by using the given StopAction.
        """
        # TODO: Do a few experiments to determine the constant that converts
        # TODO:   from wheel-degrees-spun to robot-degrees-spun.
        # TODO:   Assume that the conversion is linear with respect to speed
        self.drive_system.left_wheel.start_moving(duty_cycle_percent)
        self.drive_system.right_wheel.start_moving(-duty_cycle_percent)
        while True:
            if self.drive_system.left_wheel.get_degrees_spun() > degrees:
                self.drive_system.left_wheel.stop_moving(stop_action)
                self.drive_system.right_wheel.stop_moving(stop_action)
                break


def run_test_spin_in_place_degrees():
    robot = rb.Snatch3rRobot()
    print('45 degree turn')
    robot.drive_system.spin_in_place_degrees(300)
    time.sleep(5)
    print('90 degree turn')
    robot.drive_system.spin_in_place_degrees(930)
    time.sleep(5)
    print('180 degree turn')
    robot.drive_system.spin_in_place_degrees(1860)
    time.sleep(5)
    print('360 degree turn')
    robot.drive_system.spin_in_place_degrees(3660)

main()
