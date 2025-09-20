import keyboard as key

superShortcut = "ctrl+shift"
subShortcut = f"{superShortcut}+alt"

key.add_hotkey(f"{superShortcut}+0",lambda: key.write('\u2070'))
key.add_hotkey(f"{subShortcut}+0",lambda: key.write('\u2080'))

key.add_hotkey(f"{superShortcut}+1",lambda: key.write('\u00B9'))
key.add_hotkey(f"{subShortcut}+1",lambda: key.write('\u2081'))

key.add_hotkey(f"{superShortcut}+2",lambda: key.write('\u00B2'))
key.add_hotkey(f"{subShortcut}+2",lambda: key.write('\u2082'))

key.add_hotkey(f"{superShortcut}+3",lambda: key.write('\u00B3'))
key.add_hotkey(f"{subShortcut}+3",lambda: key.write('\u2083'))

key.add_hotkey(f"{superShortcut}+4",lambda: key.write('\u2074'))
key.add_hotkey(f"{subShortcut}+4",lambda: key.write('\u2084'))

key.add_hotkey(f"{superShortcut}+5",lambda: key.write('\u2075'))
key.add_hotkey(f"{subShortcut}+5",lambda: key.write('\u2085'))

key.add_hotkey(f"{superShortcut}+6",lambda: key.write('\u2076'))
key.add_hotkey(f"{subShortcut}+6",lambda: key.write('\u2086'))

key.add_hotkey(f"{superShortcut}+7",lambda: key.write('\u2077'))
key.add_hotkey(f"{subShortcut}+7",lambda: key.write('\u2087'))

key.add_hotkey(f"{superShortcut}+8",lambda: key.write('\u2078'))
key.add_hotkey(f"{subShortcut}+8",lambda: key.write('\u2088'))

key.add_hotkey(f"{superShortcut}+9",lambda: key.write('\u2079'))
key.add_hotkey(f"{subShortcut}+9",lambda: key.write('\u2089'))

print("SuberScript is Active: Ctrl+C to quit")

key.wait()