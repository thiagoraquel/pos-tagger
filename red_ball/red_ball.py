import cv2
import numpy as np
from adc_red_ball import add_red_ball

# Carrega a screenshot
img = cv2.imread('screenshot.png')

img_red_ball = add_red_ball(img)

# Salva a imagem com a bola vermelha no diretório
cv2.imwrite('screenshot_red_ball.png', img_red_ball)

# Converte de BGR (padrão do OpenCV) para HSV
hsv_img = cv2.cvtColor(img_red_ball, cv2.COLOR_BGR2HSV)
cv2.imwrite('outputs/hsv_image.png', hsv_img)

# Definir o intervalo de cores vermelhas no espaço HSV
lower_red_1 = np.array([0, 120, 70])   # Vermelho escuro
upper_red_1 = np.array([10, 255, 255]) # Vermelho claro

lower_red_2 = np.array([170, 120, 70]) # Vermelho escuro (segunda faixa)
upper_red_2 = np.array([180, 255, 255])# Vermelho claro (segunda faixa)

# Cria as máscaras para detectar os dois intervalos de vermelho
mask1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
cv2.imwrite('outputs/mask1.png', mask1)

mask2 = cv2.inRange(hsv_img, lower_red_2, upper_red_2)
cv2.imwrite('outputs/mask2.png', mask2)

# Combina as duas máscaras
mask = cv2.bitwise_or(mask1, mask2)
cv2.imwrite('outputs/mask_combined.png', mask)

# Aplica a máscara na imagem original
result = cv2.bitwise_and(img_red_ball, img_red_ball, mask=mask)
cv2.imwrite('outputs/mask_applied.png', result)

# Encontra os contornos na máscara combinada
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Se encontrar pelo menos um contorno
if contours:
    # Pega o maior contorno (assumindo que é a bola vermelha)
    largest_contour = max(contours, key=cv2.contourArea)

    # Encontra um círculo mínimo que engloba o contorno
    (x, y), radius = cv2.minEnclosingCircle(largest_contour)

    # Converte para inteiros
    center = (int(x), int(y))
    radius = int(radius)

    # Desenha um círculo sobre a imagem original
    output = img_red_ball.copy()
    cv2.circle(output, center, radius, (0, 255, 0), 2)

    # Salva a imagem com o círculo desenhado
    cv2.imwrite('outputs/detected_circle.png', output)

    # Define o tamanho do recorte (por exemplo, 2x o raio)
    crop_size = radius * 2

    # Coordenadas do recorte
    x_start = max(0, center[0] - crop_size * 2)
    y_start = max(0, center[1] - crop_size * 2)
    x_end = min(img_red_ball.shape[1], center[0] + crop_size * 2)
    y_end = min(img_red_ball.shape[0], center[1] + crop_size * 2)

    # Realiza o recorte
    cropped = img_red_ball[y_start:y_end, x_start:x_end]

    # Salva o recorte
    cv2.imwrite('outputs/red_ball_crop.png', cropped)