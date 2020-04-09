import win32api
import win32con
import time
import keymap

# 🍁

DEFAULT_DURATION = .15

class Game:

    def get_valid_buttons(self):
        return [button for button in keymap.keys()]

    def is_valid_button(self, button):
        return button in keymap.keys()

    def button_to_key(self, button):
        return keymap[button]

    def push_button(self, button):
        self._handle(button, 0)
        time.sleep(button['duration'] if 'duration' in button else DEFAULT_DURATION)
        self._handle(button, win32con.KEYEVENTF_KEYUP)

    def _handle(self, button, event):
        if isinstance(button['key'], list):
            for b in button['key']:
                win32api.keybd_event(self.button_to_key(b), 0, event, 0)
        else:
            win32api.keybd_event(self.button_to_key(button['key']), 0, event, 0)

