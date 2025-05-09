import pyautogui

# Define a resolução da tela como referência
screen_width, screen_height = 1920, 1080

# Solicita as coordenadas do usuário
x = int(input(f"Digite a coordenada X (0 a {screen_width}): "))
y = int(input(f"Digite a coordenada Y (0 a {screen_height}): "))

# Move o mouse até o ponto indicado
pyautogui.moveTo(x, y, duration=0)
print(f"Mouse movido para ({x}, {y})")
