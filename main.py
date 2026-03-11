import cv2
import numpy as np

# 1️⃣ Start camera
cam = cv2.VideoCapture(0)

# 2️⃣ Infinite loop for live feed
while True:
    ret, frame = cam.read()   # Capture frame

    # 3️⃣ Processing will happen here (empty for now)

    cv2.imshow("Live Camera", frame)  # Show frame

    # 4️⃣ Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

# 5️⃣ Release resources
cam.release()
cv2.destroyAllWindows()