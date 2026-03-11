import cv2
import numpy as np
import mediapipe as mp   # ➕ Added

# MediaPipe setup ➕
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh()
mp_draw = mp.solutions.drawing_utils

# 1️⃣ Start camera
cam = cv2.VideoCapture(0)

# 2️⃣ Infinite loop for live feed
while True:
    ret, frame = cam.read()

    # 🔵 Minimal Processing (Face Landmarks)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)
    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            mp_draw.draw_landmarks(frame, face, mp_face.FACEMESH_TESSELATION)

    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()