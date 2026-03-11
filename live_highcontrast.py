import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    enhanced = cv2.equalizeHist(gray)
    cv2.imshow("Surveillance Mode", enhanced)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()