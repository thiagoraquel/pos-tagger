from pynput import keyboard

class CommandListener:
  def __init__(self, start_callback=None, stop_callback=None, kill_callback=None):
    self.start_sequence = [keyboard.KeyCode.from_char('i'), keyboard.KeyCode.from_char('o')]
    self.stop_sequence = [keyboard.KeyCode.from_char('p'), keyboard.KeyCode.from_char('u')]
    self.kill_sequence = [keyboard.KeyCode.from_char('t'), keyboard.KeyCode.from_char('y')]

    self.pressed_keys = set()
    self.toggle = True

    self.start_callback = start_callback
    self.stop_callback = stop_callback
    self.kill_callback = kill_callback

    self.listener = None

  def on_press(self, key):
    self.pressed_keys.add(key)

    if all(k in self.pressed_keys for k in self.start_sequence) and self.toggle:
      print("Sequência de início detectada.")
      if self.start_callback:
        self.start_callback()
      self.toggle = False

    elif all(k in self.pressed_keys for k in self.stop_sequence) and self.toggle:
      print("Sequência de pausa detectada.")
      if self.stop_callback:
        self.stop_callback()
      self.toggle = False

    elif all(k in self.pressed_keys for k in self.kill_sequence):
      print("Sequência de encerramento detectada.")
      if self.kill_callback:
        self.kill_callback()
      self.listener.stop()

  def on_release(self, key):
    if key in self.pressed_keys:
      self.pressed_keys.remove(key)
      self.toggle = True

  def run(self):
    self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
    self.listener.start()
    print("Escutando teclas... i+o para iniciar, p+u para pausar, t+y para encerrar.")
    self.listener.join()
