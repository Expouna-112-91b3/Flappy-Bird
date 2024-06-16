import pygame

from scenes.singleplayer import Singleplayer
from scenes.scenes import Scenes
from scenes.menu import Menu
from scenes.score_board import ScoreBoard

from config import Config

# Reconhecer webcam e Identificar a mão

import cv2
import mediapipe.python.solutions.hands as mp_hands
import numpy as np

import multiprocessing as multip

def game(q):
    CONFIG = Config()
    CONFIG.start_screen()
    CONFIG.setup_images()
    pygame.font.init()

    MENU = Menu()
    SINGLEPLAYER = Singleplayer()
    SCORE_BOARD = ScoreBoard()

    CONFIG.set_scene(Scenes.MENU.value)

    running = CONFIG.get_running()

    while running:

        if not CONFIG.get_running():
            running = False

        match CONFIG.get_current_scene():
            case Scenes.MENU.value:
                MENU.run()
            case Scenes.SINGLEPLAYER.value:
                SINGLEPLAYER.run(q)
            case Scenes.SCORE_BOARD.value:
                SCORE_BOARD.run()
            case _:
                break

        pygame.display.flip()
        CONFIG.clock_tick(90)
    pygame.quit()

def hand_detection(q):
    cap = cv2.VideoCapture(1)
    with mp_hands.Hands(min_detection_confidence = 0.5, 
                        min_tracking_confidence=0.5, 
                        max_num_hands=1, 
                        static_image_mode= False) as hands:
        while True:
            _, frame = cap.read()
            cv2.waitKey(1)
            
            image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            image.flags.writeable = False

            h, w, _ = image.shape
            pontos = []
            results = hands.process(image)
            if results.multi_hand_landmarks:
                for _, landmarks in enumerate(results.multi_hand_landmarks):
                    for _, coord in enumerate(landmarks.landmark):
                        cx, cy = int(coord.x*w), int(coord.y*h)
                        pontos.append((cx,cy))
            
            cv2.imshow("Hand Tracking", image) # Exibe a janela da camera

            if pontos:
                q.put(np.mean([i[1] for i in pontos]))
            else:
                q.put("")

def main():
    q = multip.Queue()
    p1 = multip.Process(target=game, args=(q,))
    p2 = multip.Process(target=hand_detection, args=(q,))

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
