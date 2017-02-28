"""
Dialog box class
"""

from time import sleep
import logging

class DialogBox():
    """Implements a dialog box with given values (or some default ones if chosen)."""

    default_options = {"y":["Yes", True], 'n':["No", False], 'c':["Cancel", None]}

    def __init__(self, values, input_device, output_device,
                 message="Are you sure?", name="DialogBox"):
        """Initialises the DialogBox object.

        Args:

            * ``values``: values to be used. Should be a list of ``[label, returned_value]`` pairs.

            * You can also pass a string "yn" to get "Yes(True), No(False)" options,
                or "ync" to get "Yes(True), No(False), Cancel(None)" options.
            * Values put together with spaces between them can't
                be longer than the screen's width or an exception is raised

            * ``input_device``, ``output_device``: input&output device objects

        Kwargs:

            * ``message``: Message to be shown on the first line of the screen when
                UI element is activated
            * ``name``: UI element name which can be used internally and for debugging.

        """
        #attribute docstrings, should show up in Sphinx docs, verify this works as desired.
        #:input device i.e. keyboard
        self.input_device = input_device
        #:output device i.e. screen
        self.output_device = output_device
        #:True if dialog is in foreground, False otherwise
        self.in_foreground = False
        #:caret column
        self.pointer = 0
        self.value_selected = False
        self.name = name
        if isinstance(values, str):
            self.values = []
            for char in values:
                self.values.append(self.default_options[char])
        elif isinstance(values, (list, tuple)):
            assert values, "DialogBox: Empty/invalid 'values' argument!"
            self.values = values
        else:
            raise "Unsupported 'values' argument!"

        self.message = message
        self.process_values()
        self.generate_keymap()

    def to_foreground(self):
        """brings dialog to foreground"""
        self.in_foreground = True
        self.refresh()
        self.set_keymap()

    def activate(self):
        """causes dialog to be shown"""
        logging.info("% activated", self.name)
        self.output_device.cursor()
        self.to_foreground()
        self.value_selected = False
        self.pointer = 0
        while self.in_foreground: #All the work is done in input callbacks
            sleep(0.1)
        self.output_device.noCursor()
        logging.debug(self.name+" exited")
        if self.value_selected:
            return self.values[self.pointer][1]
        else:
            return None

    def deactivate(self):
        """hides dialog"""
        self.in_foreground = False
        logging.info("%s deactivated", self.name)

    def generate_keymap(self):
        """maps keys to actions"""
        self.keymap = {
            "KEY_RIGHT":    self.move_right(),
            "KEY_LEFT":     self.move_left(),
            "KEY_KPENTER":  self.accept_value(),
            "KEY_ENTER":    self.accept_value()
        }

    def set_keymap(self):
        """assigns key map to input device"""
        self.input_device.stop_listen()
        self.input_device.clear_keymap()
        self.input_device.keymap = self.keymap
        self.input_device.listen()

    def move_left(self):
        """moves caret one character left"""
        if self.pointer == 0:
            self.deactivate()
            return
        self.pointer -= 1
        self.refresh()

    def move_right(self):
        """moves caret one character right"""
        if self.pointer == len(self.values)-1:
            return
        self.pointer += 1
        self.refresh()

    def accept_value(self):
        """returns value from input device and hides dialog"""
        self.value_selected = True
        self.deactivate()

    def process_values(self):
        """creates text and metadata for dialog display on output device"""
        self.labels = [label for label, value in self.values]
        label_string = " ".join(self.labels)
        if len(label_string) > self.output_device.cols:
            error_message = "DialogBox {}: all values combined are" \
            " longer than screen's width".format(self.name)
            raise ValueError(error_message)
        self.right_offset = (self.output_device.cols - len(label_string))/2
        self.displayed_label = " "*self.right_offset+label_string
        #Need to go through the string to mark the first places
        #because we need to remember where to put the cursors
        current_position = self.right_offset
        self.positions = []
        for label in self.labels:
            self.positions.append(current_position)
            current_position += len(label) + 1

    def refresh(self):
        """sends text to output device"""
        self.output_device.setCursor(1, self.positions[self.pointer])
        self.output_device.display_data(self.message, self.displayed_label)
