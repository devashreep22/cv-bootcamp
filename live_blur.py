import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        break

    # 🔵 ADDED PROCESSING (Changed to Blur)
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    cv2.imshow("Blur Live", blur)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()