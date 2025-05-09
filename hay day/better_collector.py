import mss
import numpy as np
import cv2
from pynput import keyboard
import pyautogui
import time
import os

#sequencia de start
secret_sequence = [
    keyboard.KeyCode.from_char('i'),
    keyboard.KeyCode.from_char('o')
]

#sequencia de stop
kill_sequence = [
    keyboard.KeyCode.from_char('t'),
    keyboard.KeyCode.from_char('y')
]

screenshot_ready = True  # Bloqueio para evitar múltiplas capturas

pressed_keys = set()

with mss.mss() as sct:
    monitor = sct.monitors[1]  # tela principal
    while True:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # aqui você poderia detectar trigo, clicar, etc.
        cv2.imshow("Tela ao vivo", frame)
        if cv2.waitKey(1) == 27:  # ESC para sair
            break