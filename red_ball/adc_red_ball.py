import cv2

def add_red_ball(image, center_and_radius=(200, 150, 20)):
    x, y, radius = center_and_radius
    image_with_ball = image.copy()
    red_color = (0, 0, 255)  # BGR for red
    cv2.circle(image_with_ball, (x, y), radius, red_color, -1)
    return image_with_ball
