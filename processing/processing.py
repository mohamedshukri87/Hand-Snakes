import mediapipe as mp
import cv2
import numpy as np
import redis


def calculate_distance(p1, p2):
    return(np.array(p1) - np.array(p2))

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    r = redis.Redis(host='localhost', port=6379, db=0)

    
    read, frame = cap.read()
    if not read:
        break

    frame = cv2.flip(frame, 1)




    h, w, _ = frame.shape
    center_point = (w//2, h//2)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)
    index_finger_pos = None 

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_finger_pos = (int(index_finger_tip.x * w), int(index_finger_tip.y * h))

            cv2.circle(frame, index_finger_pos, 10, (0,0, 255), -1)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.circle(frame, center_point, 10, (255,0,0), -1)

            #if index_finger_pos:
            distance = calculate_distance(center_point, index_finger_pos)

            r.set("key", str(distance[0]) + " " + str(distance[1]))
            cv2.line(frame, center_point, index_finger_pos, (0, 255, 0), 2)

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

class cameraCapture:
    def __init__(self):
        pass

    def function(self):
        print("working")