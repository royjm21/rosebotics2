"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_wait_until_intensity_is_less_than()
    test_wait_until_intensity_is_greater_than()
    test_wait_until_color_is()
    test_wait_until_color_is_one_of()


def test_wait_until_intensity_is_less_than():
    print('testing')
    robot = rb.Snatch3rRobot()
    robot.color_sensor.wait_until_intensity_is_less_than(12)
    print('test complete')


def test_wait_until_intensity_is_greater_than():
    print('testing')
    robot = rb.Snatch3rRobot()
    robot.color_sensor.wait_until_intensity_is_greater_than(15)
    print('test complete')


def test_wait_until_color_is():
    print('testing')
    robot = rb.Snatch3rRobot()
    robot.color_sensor.wait_until_color_is('black')
    print('test complete')


def test_wait_until_color_is_one_of():
    print('testing')
    robot = rb.Snatch3rRobot()
    robot.color_sensor.wait_until_color_is_one_of('black', 'blue')


main()
