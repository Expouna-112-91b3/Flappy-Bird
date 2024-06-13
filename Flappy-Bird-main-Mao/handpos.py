import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe as mp
import numpy as np


def handidf(hands):

    cap = cv2.VideoCapture(1) # Dependendo da máquina o valor pode variar entre 0, 1, 2, 3
    #with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence=0.5, max_num_hands=1, static_image_mode= False) as hands:

    ret, frame = cap.read()
    cv2.waitKey(1)
            
    #Detecções
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    '''h, w, _ = image.shape
     print(h, w)'''

    image.flags.writeable = False

    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image.flags.writeable = True

    h, w, _ = image.shape
    pontos = []
    # Renderizando 
    if results.multi_hand_landmarks:
        for num, landmarks in enumerate(results.multi_hand_landmarks):
            #drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS,                               #
                                    #drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),   # Printa as landmarks na mão
                                    #drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),) #
            for id, coord in enumerate(landmarks.landmark):
                cx, cy = int(coord.x*w), int(coord.y*h)
                #cv2.putText(image, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2) # Enumera as landmarks
                pontos.append((cx,cy))

            #cv2.putText(image, "centro", (int(np.mean([i[0] for i in pontos])), int(np.mean([i[1] for i in pontos]))), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2) # Printa a centróide na mão
    
    cv2.imshow("Hand Tracking", image) # Exibe a janela da camera

    if pontos:
        return np.mean([i[1] for i in pontos])
        
    return
    
