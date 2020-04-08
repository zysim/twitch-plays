import win32api
import win32con
import time

# 🍁

class Game:

    keymap = {
        # Directions
        'up': win32con.VK_UP,
        'down': win32con.VK_DOWN,
        'left': win32con.VK_LEFT,
        'right': win32con.VK_RIGHT,
        
        # Actions
        'item': 0x57, # W
        'hit': 0x53, # S
        'whack': 0x53, # S (alias)
        'jump': 0x41, # A
        'bow': 0x44, # D
        'roll': 0x51, # Q
        'switch': 0x45, # E
        
        'map': win32con.VK_TAB,
        'menu': win32con.VK_SHIFT,
        
        # 👸
        'ry': [0x41, 0x51], # [A, Q]
    }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, buttons):
        for button in buttons:
            win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(.15)
        for button in buttons:
            win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
