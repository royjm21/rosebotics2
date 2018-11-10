"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Susan Harmet.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    print('Testing proximity sensor to note equation')

    # while True:
    #     distance = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
    #     hz = distance
    #     ev3.Sound.tone()
    # a_major_scale = [[880.00, 1500], [987.77, 1500], [1108.73, 1500], [1174.66, 1500], [1318.51, 1500],
    #                  [1479.98, 1500], [1661.22, 1500], [1760.00, 1500], [1760.00, 1500], [1661.22, 1500],
    #                  [1479.98, 1500], [1318.51, 1500], [1174.66, 1500], [1108.73, 1500], [987.77, 1500],
    #                  [880.00, 1500]]
    # ev3.Sound.tone(a_major_scale[0][0], a_major_scale[0][1]).wait()
    # ev3.Sound.tone(a_major_scale[1][0], a_major_scale[1][1]).wait()
    # ev3.Sound.tone(a_major_scale[2][0], a_major_scale[2][1]).wait()
    # ev3.Sound.tone(a_major_scale[3][0], a_major_scale[3][1]).wait()
    # ev3.Sound.tone(a_major_scale[4][0], a_major_scale[4][1]).wait()
    # ev3.Sound.tone(a_major_scale[5][0], a_major_scale[5][1]).wait()
    # ev3.Sound.tone(a_major_scale[6][0], a_major_scale[6][1]).wait()
    # ev3.Sound.tone(a_major_scale[7][0], a_major_scale[7][1]).wait()
    #
    # ev3.Sound.tone(a_major_scale[7][0], a_major_scale[7][1]).wait()
    # ev3.Sound.tone(a_major_scale[6][0], a_major_scale[6][1]).wait()
    # ev3.Sound.tone(a_major_scale[5][0], a_major_scale[5][1]).wait()
    # ev3.Sound.tone(a_major_scale[4][0], a_major_scale[4][1]).wait()
    # ev3.Sound.tone(a_major_scale[3][0], a_major_scale[3][1]).wait()
    # ev3.Sound.tone(a_major_scale[2][0], a_major_scale[2][1]).wait()
    # ev3.Sound.tone(a_major_scale[1][0], a_major_scale[1][1]).wait()
    # ev3.Sound.tone(a_major_scale[0][0], a_major_scale[0][1]).wait()

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    scales = ScalesEtc(robot)
    mqtt_client = com.MqttClient(scales)
    mqtt_client.connect_to_pc()
    print('connected to pc!')

    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------

    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()

        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEct(object):
    def __init__(self, robot):
        """
        Stores the robot
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed_string):
        """makes the robot go forward at the given speed"""""
        print('telling the robot to start moving at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)


class ScalesEtc(object):
    def __init__(self, robot):
        """

            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        self.a_major_scale = [[880.00, 1500], [987.77, 1500], [1108.73, 1500], [1174.66, 1500], [1318.51, 1500],
                              [1479.98, 1500], [1661.22, 1500], [1760.00, 1500], [1760.00, 1500], [1661.22, 1500],
                              [1479.98, 1500], [1318.51, 1500], [1174.66, 1500], [1108.73, 1500], [987.77, 1500],
                              [880.00, 1500]]

    def play_scales(self, type_of_scale, robot):
        print('telling the robot to play this dope scale:', type_of_scale)
        if type_of_scale == 'A':  # A major scale
            ev3.Sound.tone(self.a_major_scale)
        while True:
            x_coordinate = robot.camera.get_biggest_blob().center.x / 23
            y_coordinate = robot.camera.get_biggest_blob().center.y / 2
            print('Getting x coordinate:', x_coordinate)
            print('Getting y coordinate:', y_coordinate)
            frequency_in_hz = (2 ** (x_coordinate / 12)) * 440  # 440 is A4's frequency
            volume_of_hz = ev3.Sound.set_volume(y_coordinate)
            print('frequency input', frequency_in_hz)
            print('volume of hz:', volume_of_hz)
            ev3.Sound.tone(frequency_in_hz, 1000).wait()
            time.sleep(0.5)


main()
