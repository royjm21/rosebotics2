"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_wait_until_intensity_is_less_than()


def test_wait_until_intensity_is_less_than():
    print('testing')
    robot = rb.Snatch3rRobot()
    robot.color_sensor.wait_until_intensity_is_less_than(12)
    print('test complete')


main()
