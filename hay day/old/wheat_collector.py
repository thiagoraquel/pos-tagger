import pyautogui
import cv2
import numpy as np

# Carrega a imagem da tela (já está em formato BGR com cv2.imread)
#screenshot = cv2.imread('screenshot_20250509-151548.png', cv2.IMREAD_COLOR)
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Carrega o modelo (imagem do trigo)
template = cv2.imread('trigo3.png', cv2.IMREAD_COLOR)
w, h = template.shape[1], template.shape[0]

# Realiza a correspondência de template
res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

# Define um limiar de similaridade
threshold = 0.95
locations = list(zip(*np.where(res >= threshold)[::-1]))  # Lista de tuplas (x, y)

# Desenha círculos nos pontos encontrados
for pt in locations:
    center = (pt[0] + w // 2, pt[1] + h // 2)
    radius = max(w, h) // 4
    cv2.circle(screenshot, center, radius, (0, 255, 0), 5)

# Clica no trigo mais acima (menor valor de y)
if locations:
    # Calcula o centro de cada match
    centros = [(pt[0] + w // 2, pt[1] + h // 2) for pt in locations]
    trigo_mais_acima = min(centros, key=lambda c: c[1])
    pyautogui.moveTo(trigo_mais_acima[0], trigo_mais_acima[1], duration=0.2)
    pyautogui.click()
    print(f"Clicando no ponto mais acima: {trigo_mais_acima}")
else:
    print("Nenhum trigo encontrado.")

# Mostra o resultado
cv2.imshow('Resultado', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
