import cv2
import numpy as np

text = """What is python and how it works in the real world."""

img = np.ones((400, 800, 3), dtype=np.uint8) * 255


font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  # looks like cursive handwriting
position = (50, 150)

cv2.putText(img, text, position, font, 1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.imwrite("handwriting_output.png", img)

print("✅ Handwriting-style image saved as handwriting_output.png")
