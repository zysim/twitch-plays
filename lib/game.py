import win32api
import win32con
import time

class Game:

    keymap = {
        'up': 0x57, // W
        'down': 0x53, // S
        'left': 0x41, // A
        'right': 0x44, // D
        'jump': 0x4B, // K
        'hit': 0x4A, // J
        'whack': 0x4A, // J
        'arrow': 0x4C, // L
        'roll': 0x55, // U
        'item': 0x49, // I
        'switch': 0x4F, // O
        'map': 0x0A, // Tab
        'menu': 0x0F, // Shift on (might have to fix this)
        // TODO: rj command
    }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(.15)
        win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
