from pynput import keyboard
import pyautogui
import time
import os

# Sequência secreta, por exemplo: Ctrl + Shift + S
secret_sequence = [
    keyboard.KeyCode.from_char('i'),
    keyboard.KeyCode.from_char('o')
]

kill_sequence = [
    keyboard.KeyCode.from_char('t'),
    keyboard.KeyCode.from_char('y')
]
screenshot_ready = True  # Bloqueio para evitar múltiplas capturas


pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    global screenshot_ready
    # Verifica se todos os da sequência estão pressionados
    if all(k in pressed_keys for k in secret_sequence) and screenshot_ready == True:
        #print("Sequência detectada! Tirando screenshot...")
        take_screenshot()
        screenshot_ready = False

    elif all(k in pressed_keys for k in kill_sequence):
        #print("Sequência de encerramento detectada. Encerrando...")
        listener.stop()

def on_release(key):
    global screenshot_ready
    # Remove a tecla quando solta
    if key in pressed_keys:
        pressed_keys.remove(key)
        screenshot_ready = True

def take_screenshot():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    save_dir = r"C:\Users\thiag\Downloads\exercicios_programming\hay day"
    os.makedirs(save_dir, exist_ok=True)  # Cria a pasta se não existir

    filepath = os.path.join(save_dir, f"screenshot_{timestamp}.png")    
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    #print(f"Screenshot salva como screenshot_{timestamp}.png")

# Começa a escutar o teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Escutando teclas... Pressione Ctrl+Shift+S para tirar screenshot.")
    listener.join()
