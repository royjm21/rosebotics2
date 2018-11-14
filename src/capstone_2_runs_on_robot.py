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
    scales.mqtt_client = mqtt_client
    print('connected to pc!')
    # how do i get the value that I chose to send to the robot back to the robot?

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
        self.stop_tone = False
        self.stop_moving_action = False
        self.mqtt_client = None
        self.a_major_scale = [[880.00, 1500], [987.77, 1500], [1108.73, 1500], [1174.66, 1500], [1318.51, 1500],
                              [1479.98, 1500], [1661.22, 1500], [1760.00, 1500], [1760.00, 1500], [1661.22, 1500],
                              [1479.98, 1500], [1318.51, 1500], [1174.66, 1500], [1108.73, 1500], [987.77, 1500],
                              [880.00, 1500]]

    def convert_to_freq(self, type_of_scale):
        if type_of_scale == 'A':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 440
        elif type_of_scale == 'B':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 493
        elif type_of_scale == 'C':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 523
        elif type_of_scale == 'D':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 587
        elif type_of_scale == 'E':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 659
        elif type_of_scale == 'F':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 698
        elif type_of_scale == 'G':
            print('type of starting note or default note:', type_of_scale)
            type_of_scale = 783
        else:
            type_of_scale = 440
        self.mqtt_client.send_message('receive_notes', [type_of_scale])
        return type_of_scale

    def play_scales(self, type_of_scale):
        """
            :type robot: rb.Snatch3rRobot
            :type type_of_scale: str \ int
        """
        type_of_scale = self.convert_to_freq(type_of_scale)
        print('telling the robot to play this dope scale:', type_of_scale)
        # if type_of_scale == 'A':  # A major scale
        #     ev3.Sound.tone(self.a_major_scale)
        # if robot.camera.get_biggest_blob().get_area() >= 1000:
        #     robot.drive_system.turn_degrees(10)
        # robot.drive_system.stop_moving()
        # starting_note = type_of_scale

        x_coordinate = self.robot.camera.get_biggest_blob().center.x / 23

        frequency_in_hz = (2 ** (x_coordinate / 12)) * type_of_scale  # 440 is A4's frequency
        print('frequency input', frequency_in_hz)

        # y_coordinate = self.robot.camera.get_biggest_blob().center.y / 2
        # print('Getting x coordinate:', x_coordinate)
        # print('Getting y coordinate:', y_coordinate)
        # volume_of_hz = ev3.Sound.set_volume(y_coordinate)
        # print('volume of hz:', volume_of_hz)

        ev3.Sound.tone(frequency_in_hz, 1000).wait()
        self.mqtt_client.send_message('receive_notes', [type_of_scale])
        time.sleep(1)
        if self.stop_tone is False:
            self.play_scales(type_of_scale)

    def stop_playing_command(self):
        print('Telling to stop')
        self.stop_tone = True

    def stop_moving(self):
        print('Telling robot to stop moving')
        if self.stop_moving_action is True:
            self.robot.drive_system.stop_moving()

    def area_scales(self, type_of_scale):
        type_of_scale = self.convert_to_freq(type_of_scale)
        print('Commencing are dependent scales with type of scale:', type_of_scale)
        area_argument = 1000
        while True:
            length_away_by_area = self.robot.camera.get_biggest_blob().get_area()
            print('the length by area:', length_away_by_area)
            frequency_in_hz = (2 ** (length_away_by_area / area_argument)) * type_of_scale
            print('area argument is:', area_argument)
            if length_away_by_area <= area_argument:
                print('area is:', length_away_by_area)
                print('Robot moving 3 inches')
                self.robot.drive_system.go_straight_inches(3)
                ev3.Sound.tone(frequency_in_hz, 1500).wait()
                print('Frequency instructed to play:', frequency_in_hz)
                time.sleep(1)
                area_argument -= 10
                print('Area argument is now:', area_argument)
            else:
                print('breaking')
                break
        # if self.stop_moving_action is False:
        #     self.area_scales(type_of_scale)


main()
