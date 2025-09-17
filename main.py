import pyautogui as pag
while True:
    if pag.keyDown('ctrl') and pag.keyDown('shift') and pag.keyDown('2'):
        pag.write('\u00B2')