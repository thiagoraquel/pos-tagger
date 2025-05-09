# Arquivo: main_program.py
import time
from commandListener import CommandListener

running = False
stopped = False

def start():
  global running, stopped
  running = True
  stopped = False
  print("Contador iniciado ou retomado.")

def stop():
  global running
  running = False
  print("Contador pausado.")

def kill():
  global running, stopped
  running = False
  stopped = True
  print("Encerrando programa...")

listener = CommandListener(start_callback=start, stop_callback=stop, kill_callback=kill)
listener_thread = listener.run()  # Este bloqueia até t+y ser pressionado

start_time = time.time()

while True:
  if stopped:
    break
  if running:
    elapsed = int(time.time() - start_time)
    print(f"Se passaram {elapsed} segundos desde o início.")
    time.sleep(1)
