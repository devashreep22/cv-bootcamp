import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)
    cv2.imshow("Thermal Search", thermal)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()