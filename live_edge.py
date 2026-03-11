import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow("Edge Live", edges)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()