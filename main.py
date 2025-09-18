import keyboard as key

key.add_hotkey("ctrl+shift+0",lambda: key.write('\u2070'))
key.add_hotkey("ctrl+shift+alt+0",lambda: key.write('\u2080'))

key.add_hotkey("ctrl+shift+1",lambda: key.write('\u00B9'))
key.add_hotkey("ctrl+shift+alt+1",lambda: key.write('\u2081'))

key.add_hotkey("ctrl+shift+2",lambda: key.write('\u00B2'))
key.add_hotkey("ctrl+shift+alt+2",lambda: key.write('\u2082'))

key.add_hotkey("ctrl+shift+3",lambda: key.write('\u00B3'))
key.add_hotkey("ctrl+shift+alt+3",lambda: key.write('\u2083'))

key.add_hotkey("ctrl+shift+4",lambda: key.write('\u2074'))
key.add_hotkey("ctrl+shift+alt+4",lambda: key.write('\u2084'))

key.add_hotkey("ctrl+shift+5",lambda: key.write('\u2075'))
key.add_hotkey("ctrl+shift+alt+5",lambda: key.write('\u2085'))

key.add_hotkey("ctrl+shift+6",lambda: key.write('\u2076'))
key.add_hotkey("ctrl+shift+alt+6",lambda: key.write('\u2086'))

key.add_hotkey("ctrl+shift+7",lambda: key.write('\u2077'))
key.add_hotkey("ctrl+shift+alt+7",lambda: key.write('\u2087'))

key.add_hotkey("ctrl+shift+8",lambda: key.write('\u2078'))
key.add_hotkey("ctrl+shift+alt+8",lambda: key.write('\u2088'))

key.add_hotkey("ctrl+shift+9",lambda: key.write('\u2079'))
key.add_hotkey("ctrl+shift+alt+9",lambda: key.write('\u2089'))

key.wait()