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
    rc.mqtt_client = mqtt_client
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
        self.mqtt_client = None

    def go_forward(self, speed_string):
        """makes the robot go forward at the given speed"""""
        print('telling the robot to start moving at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def follow_path(self):
        while True:
            x = self.robot.color_sensor.get_reflected_intensity()  # 100 in intensity is white, 1 through 4 is black
            print(x)
            if x <= 10:
                self.robot.drive_system.start_moving(left_wheel_duty_cycle_percent=45,
                                                     right_wheel_duty_cycle_percent=45)
            if x >= 10:  # go counterclockwise in this case
                self.robot.drive_system.start_moving(left_wheel_duty_cycle_percent=0, right_wheel_duty_cycle_percent=50)

            if x >= 20 and x <= 25:
                self.robot.drive_system.stop_moving()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.beep()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.speak('I found blue!')
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.beep()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                self.robot.drive_system.spin_in_place_degrees(360)
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(3)
                break

            if x >= 74 and x <= 80:
                self.robot.drive_system.stop_moving()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.beep()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.speak('I found red!')
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.beep()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                self.robot.drive_system.spin_in_place_degrees(720)
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(3)
                break

            if x >= 15 and x <= 19:
                self.robot.drive_system.stop_moving()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.beep()
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.speak('I found green!')
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(1.5)
                ev3.Sound.beep()
                self.robot.drive_system.spin_in_place_degrees(180)
                self.mqtt_client.send_message('handle_increment_progress_bar')
                time.sleep(3)
                break

            if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 4:
                ev3.Sound.beep()
                ev3.Sound.speak('There is something in my way!')
                ev3.Sound.beep()

    def path_by_color(self):
        x = self.robot.color_sensor.get_reflected_intensity()

        if x >= 20 and x <= 25:
            ev3.Sound.speak('I found blue!')
            self.robot.drive_system.spin_in_place_degrees(360)

        if x >= 74 and x <= 80:
            ev3.Sound.speak('I found red!')
            self.robot.drive_system.spin_in_place_degrees(720)

        if x >= 15 and x <= 19:
            ev3.Sound.speak('I found green!')
            self.robot.drive_system.spin_in_place_degrees(180)


main()
