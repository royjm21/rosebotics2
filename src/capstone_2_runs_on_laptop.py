"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Susan Harmet.
"""

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

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    frequency_retreval = RecieverOfNoteSpecsEtc()
    mqtt_client = com.MqttClient(frequency_retreval)
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)
    root.mainloop()
    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this pc.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=30)
    check_button_a_scale = ttk.Radiobutton(frame, value='A', text='A Major Scale')
    check_button_b_scale = ttk.Radiobutton(frame, value='B', text='B Major Scale')
    check_button_c_scale = ttk.Radiobutton(frame, value='C', text='C Major Scale')
    check_button_d_scale = ttk.Radiobutton(frame, value='D', text='D Major Scale')
    check_button_e_scale = ttk.Radiobutton(frame, value='E', text='E Major Scale')
    check_button_f_scale = ttk.Radiobutton(frame, value='F', text='F Major Scale')
    check_button_g_scale = ttk.Radiobutton(frame, value='g', text='G Major Scale')

    play_tone_button = ttk.Button(frame, text="Theremin it UP")
    # if check_button_b_scale.selection_get():
    #     scale_to_play = check_button_b_scale
    # if check_button_a_scale.selection_get():
    #     scale_to_play = check_button_a_scale

    """
    make a button that sends a message and the revieving end is the theremin method
    """
    which_string_var = tkinter.StringVar()
    check_button_a_scale['variable'] = which_string_var
    check_button_b_scale['variable'] = which_string_var
    check_button_c_scale['variable'] = which_string_var
    check_button_d_scale['variable'] = which_string_var
    check_button_e_scale['variable'] = which_string_var
    check_button_f_scale['variable'] = which_string_var
    check_button_g_scale['variable'] = which_string_var

    which_string_var.set('A')
    area_scales_button = ttk.Button(frame, text='Launch scale play', padding=10)

    frame.grid()
    check_button_a_scale.grid()
    check_button_b_scale.grid()
    check_button_c_scale.grid()
    check_button_d_scale.grid()
    check_button_e_scale.grid()
    check_button_f_scale.grid()
    check_button_g_scale.grid()

    play_tone_button.grid()
    area_scales_button.grid()

    area_scales_button['command'] = lambda: area_dependent_scales(which_string_var, mqtt_client)
    play_tone_button['command'] = (lambda: tell_to_sing_scales(which_string_var, mqtt_client))

    # speed_entry_box = ttk.Entry(frame);
    # go_forward_button = ttk.Button(frame, text="Go forward")
    #
    # speed_entry_box.grid()
    # go_forward_button.grid()
    #
    # go_forward_button['command'] = \
    #     lambda: handle_go_forward(speed_entry_box, mqtt_client)


def handle_go_forward(entry_box, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    print('Sending the go_forward message with speed_string:', speed_string)
    mqtt_client.send_message('go_forward', [speed_string])


def tell_to_sing_scales(which_string_var, mqtt_client):
    """
    pretty self explanatory because of def name
    :param type_of_scale:
    :param mqtt_client:
    :return:
    """
    print('Sending the tell_to_sing_scales message with type of scale:', which_string_var.get())
    mqtt_client.send_message('play_scales', [which_string_var.get()])  # breaks because doesn't know attribute


def tell_to_stop(mqtt_client):
    print('Sending stop command to robot')
    mqtt_client.send_message('stop_playing_command')


def area_dependent_scales(which_string_var, mqtt_client):
    print('Commanding robot to begin playing area dependent scales')
    mqtt_client.send_message('area_scales', [which_string_var.get()])


class RecieverOfNoteSpecsEtc(object):
    def __init__(self):
        pass

    def receive_notes(self, type_of_scale):
        print('Received type of note played!')
        print('This note played is:', type_of_scale)
        photo = tkinter.PhotoImage(file='singing gif.gif')
        new_window = tkinter.Toplevel()
        label = ttk.Label(new_window, image=photo)
        label.image = photo
        label.grid()


main()
