"""
  Capstone Project.  Code written by Susan Harmet.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # test_go_straight_inches()
    # time.sleep(5)
    # follow_the_black_line(rb.Snatch3rRobot())
    # time.sleep(5)
    # test_wait_until_pressed()
    # test_wait_until_released()
    # test_beep_for_object(rb.Snatch3rRobot())
    # test_beacon_button_press_commands(rb.Snatch3rRobot())


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


def test_beep_for_object(robot):
    print('Testing proximity sensor')
    print(robot.proximity_sensor.get_distance_to_nearest_object_in_inches())
    print('Testing beep mechanism')
    # robot.Sound.beep()
    print('testing Beep for object 12 inches or closer')
    robot.proximity_sensor.beep_for_object()


def test_beacon_button_press_commands(robot):
    print('Testing beacon button pressed')
    if robot.beacon_button_sensor.is_top_red_button_pressed():
        print('Button Pressed!')

    print("Testing button's capacity to control go straight 11 inches forward")
    robot.beacon_button_sensor.move_forward_with_red(11)
    print('Testing Completed')

    print("Testing button's capacity to control go straight 11 inches backwards")
    robot.beacon_button_sensor.move_backward_with_top_blue(-11)


############################################
############################################
main()
