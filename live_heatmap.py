import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING
    heatmap = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
    cv2.imshow("Edge Live", heatmap)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()