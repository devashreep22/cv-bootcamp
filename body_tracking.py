import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
draw = mp.solutions.drawing_utils

while True:
    ret, frame = cam.read()

    # Minimal Body Detection
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if results.pose_landmarks:
        draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(1) == 27:   # Press ESC to exit
        break

cam.release()
cv2.destroyAllWindows()