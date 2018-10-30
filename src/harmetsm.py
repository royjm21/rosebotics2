"""
  Capstone Project.  Code written by Susan Harmet.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # test_go_straight_inches()
    follow_the_black_line(rb.Snatch3rRobot())
    # test_wait_until_pressed()
    # test_wait_until_released()


def follow_the_black_line(robot):
    while True:
        x = robot.color_sensor.get_reflected_intensity()  # 100 in intensity is white, 1 through 4 is black
        print(x)
        if x <= 10:
            robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        if x >= 10:  # go counterclockwise in this case
            robot.drive_system.start_moving(left_wheel_duty_cycle_percent=0, right_wheel_duty_cycle_percent=50)
        

def test_go_straight_inches():
    print('testing go_straight_inches')

    print('Test 1')
    robot = rb.Snatch3rRobot()  # to construct a dog doq = Dog(), WAS MISSING PARENTHESES
    time.sleep(2)
    print('Testing with 12 inches')
    robot.drive_system.go_straight_inches(35)
    print('Testing complete')


def test_follow_the_black_line():
    print('testing follow the black line')
    robot = rb.Snatch3rRobot()
    robot.drive_system.follow_the_black_line()


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


# def test_calibrated():
#     print('test if calibrated')
#     robot = rb.Snatch3rRobot()
#     robot.calibrate(12)
#     print('Arm calibrated')

#
# def test_raise_arm_and_close_claw():
#     print("testing raise arm and close claw")
#     robot = rb.Snatch3rRobot()
#     robot.arm.raise_arm_and_close_claw(11)


############################################
############################################
main()
