import win32con
import game

keymap = {
    # Directions
    'up': {
        'key': win32con.VK_UP,
    },
    'down': {
        'key': win32con.VK_DOWN,
    },
    'left': {
        'key': win32con.VK_LEFT,
        'duration': 2 * game.DEFAULT_DURATION,
    },
    'right': {
        'key': win32con.VK_RIGHT,
        'duration': 2 * game.DEFAULT_DURATION,
    },
    
    # Actions
    'item': {
        'key': 0x57, # W
    },
    'hit': {
        'key': 0x53, # S
    },
    'whack': {
        'key': 0x53, # S (alias)
    },
    'jump': {
        'key': 0x41, # A
    },
    'bow': {
        'key': 0x44, # D
    },
    'roll': {
        'key': 0x51, # Q
    },
    'switch': {
        'key': 0x45, # E
    },
    
    'map': {
        'key': win32con.VK_TAB,
    },
    'menu': {
        'key': win32con.VK_SHIFT,
    },
    
    # 👸
    'ry': {
        'key': [0x41, 0x51], # [A, Q]
    },
}