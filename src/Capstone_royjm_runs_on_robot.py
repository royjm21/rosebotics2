"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Jeremy Roy.
"""


import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello, how are you?')
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot.
        :type   robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed_string):
        """makes robot move forward at a given speed"""
        print('robot should move at speed = speed_string', speed_string)
        robot = rb.Snatch3rRobot()
        robot.drive_system.right_wheel.reset_degrees_spun()
        robot.drive_system.left_wheel.reset_degrees_spun()

    def follow_path(self):
        robot = rb.Snatch3rRobot
        while True:
            x = robot.color_sensor.get_reflected_intensity()  # 100 in intensity is white, 1 through 4 is black
            print(x)
            if x <= 10:
                robot.drive_system.start_moving(left_wheel_duty_cycle_percent=45, right_wheel_duty_cycle_percent=45)
            if x >= 10:  # go counterclockwise in this case
                robot.drive_system.start_moving(left_wheel_duty_cycle_percent=0, right_wheel_duty_cycle_percent=50)


main()
