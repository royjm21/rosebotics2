"""
  Capstone Project.  Code written by Susan Harmet.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_go_straight_inches()
    # test_wait_until_pressed()
    # test_wait_until_released()


def test_go_straight_inches():
    print('testing go_straight_inches')

    print('Test 1')
    robot = rb.Snatch3rRobot()  # to construct a dog doq = Dog(), WAS MISSING PARENTHESES

    print('Testing with 12 inches')
    robot.drive_system.go_straight_inches(12)


def test_wait_until_pressed():
    print('Testing wait_until_pressed')
    print('Test 1')
    robot = rb.Snatch3rRobot()

    print('Testing whether it can tell when the button has been pressed')
    robot.touch_sensor.wait_until_pressed()
    print('Sensor was pressed!')


def test_wait_until_released():
    print('testing wait until released')
    robot = rb.Snatch3rRobot()
    robot.touch_sensor.wait_until_released()
    print('Sensor released')


def test_calibrated():
    print('test if calibrated')
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate(12)
    print('Arm calibrated')


def test_raise_arm_and_close_claw():
    print("testing raise arm and close claw")
    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw(11)

############################################
############################################
main()
