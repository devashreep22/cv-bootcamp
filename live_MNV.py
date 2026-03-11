import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # 🔵 ADDED PROCESSING (Night Vision)
    green = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    night_vision = cv2.merge([
        np.zeros_like(green),
        green,
        np.zeros_like(green)
    ])

    cv2.imshow("Night Vision", night_vision)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()