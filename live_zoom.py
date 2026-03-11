import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING (Zoom Surveillance)
    h, w, _ = frame.shape
    crop = frame[h//4:3*h//4, w//4:3*w//4]
    zoom = cv2.resize(crop, (w, h))

    cv2.imshow("Zoom Surveillance", zoom)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()