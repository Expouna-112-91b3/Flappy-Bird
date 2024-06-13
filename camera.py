import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe as mp
import numpy as np

import multiprocessing as multip    

cap = cv2.VideoCapture(1)

with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence=0.5, max_num_hands=1, static_image_mode= False) as hands:
    while True:
        ret, frame = cap.read()
        cv2.waitKey(1)
                
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        image.flags.writeable = False

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        h, w, _ = image.shape
        pontos = []
        # Renderizando 
        if results.multi_hand_landmarks:
            for num, landmarks in enumerate(results.multi_hand_landmarks):
                for id, coord in enumerate(landmarks.landmark):
                    cx, cy = int(coord.x*w), int(coord.y*h)
                    pontos.append((cx,cy))
                
        cv2.imshow("Hand Tracking", image) # Exibe a janela da camera

        if pontos:
            print(np.mean([i[1] for i in pontos]))
            #q.put(np.mean([i[1] for i in pontos]))

        else:
            #q.put("")
            print("None")
