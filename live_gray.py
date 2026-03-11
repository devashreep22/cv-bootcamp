import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Live", gray)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()