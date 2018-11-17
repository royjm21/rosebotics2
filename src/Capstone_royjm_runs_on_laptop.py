"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Jeremy Roy.
"""
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    delegate = ReceiveMessages()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_ev3()

    progress_bar = setup_gui(root, mqtt_client)
    delegate.progress_bar = progress_bar

    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=35, relief='groove')
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")
    follow_path_button = ttk.Button(frame, text='follow path')
    progress_bar = ttk.Progressbar(frame, length=200)
    path_by_color_button = ttk.Button(frame, text='path by color')
    find_nearest_object_button = ttk.Button(frame, text='find nearest object')

    progress_bar.grid()
    speed_entry_box.grid()
    go_forward_button.grid()
    follow_path_button.grid()
    path_by_color_button.grid()
    find_nearest_object_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt_client)

    follow_path_button['command'] = \
        lambda: handle_follow_path(mqtt_client)

    path_by_color_button['command'] = \
        lambda: handle_path_by_color(mqtt_client)

    find_nearest_object_button['command'] = \
        lambda: handle_find_nearest(mqtt_client)

    return progress_bar


def handle_go_forward(entry_box, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    print('sending the go_forward message with speed', speed_string)
    mqtt_client.send_message('go_forward', [speed_string])
    # --------------------------------------------------------------------------


def handle_follow_path(mqtt_client):
    """
    tells the robot to follow the path with colors along it
    """
    print('sending the follow path message')
    mqtt_client.send_message('follow_path')


def handle_path_by_color(mqtt_client):
    print('sending the path by color message')
    mqtt_client.send_message('path_by_color')


def handle_find_nearest(mqtt_client):
    print('sending find nearest object message')
    mqtt_client.send_message('find_nearest_object')


class ReceiveMessages(object):
    def __init__(self):
        self.progress_bar = None

    def handle_increment_progress_bar(self):
        # print('hello') # 'for testing purposes'
        self.progress_bar.step(amount=20)


main()
