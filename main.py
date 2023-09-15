import time
import pyautogui
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os
from press import toggle_q_on, toggle_q_off, press_r, press_d, press_laugh

load_dotenv()

print(os.getenv("NEUROSITY_DEVICE_ID"))

neurosity = NeurositySDK({
    "device_id": "9565655c3cb79d803724caa14ae7a943"
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})


def callback_for_focus(data):
    if data['label'] == 'focus' and data['probability'] > 0.4:
        print(f"focus level: {data['probability']}")
        toggle_q_on()

def callback_for_calm(data):
    if data['label'] == 'calm' and data['probability'] > 0.35:
        print(f"calm level: {data['probability']}")
        toggle_q_off()

def callback_for_kinesis(data):
    # print(data)
    if data['label'] == 'bitingAlemon' and data['confidence'] > 0.99:
        print("kinesis")
        press_d()
        press_laugh()
        press_r()

focus_stream = neurosity.focus(callback_for_focus) #if over 0.5 == focus
kinesis_stream = neurosity.kinesis("bitingALemon", callback_for_kinesis)


# import cv2
# import mediapipe as mp
# import pyautogui as pg
# import random
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_width, screen_height = pg.size()

# def click_mouse(button):
#     pg.click(button=button)
#     pg.sleep(1)

# last_10_frames = []
# last_10_right_frames = []
# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     width = 640
#     height = 360
#     dim = (width, height)
#     frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_height, frame_width, _ = frame.shape
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
#         landmark = landmarks[474]
#         x = int(landmark.x * frame_width)
#         y = int(landmark.y * frame_height)
#         cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
#         screen_x = int(x * screen_width / frame_width)
#         screen_y = int(y * screen_height / frame_height)
#         pg.moveTo(screen_x, screen_y)
            
#         right = [landmarks[374], landmarks[386]]
#         for landmark in right:
#             x = int(landmark.x * frame_width)
#             y = int(landmark.y * frame_height)
#             cv2.circle(frame, (x, y), 2, (255, 255, 0), -1)
#             print(right[0].y - right[1].y)
#             last_10_right_frames.append(right[0].y - right[1].y)
#             if len(last_10_right_frames) > 20:
#                 last_10_right_frames.pop(0)
#             if sum(last_10_right_frames) / len(last_10_right_frames) < 0.013:
#                 print("right")
#                 click_mouse('right')
#                 last_10_right_frames = last_10_right_frames[10:20]

#         left = [landmarks[145], landmarks[159]]
#         for landmark in left:
#             x = int(landmark.x * frame_width)
#             y = int(landmark.y * frame_height)
#             cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)
#             last_10_frames.append(left[0].y - left[1].y)
           
#             if len(last_10_frames) > 20:
#                 last_10_frames.pop(0)
#             if sum(last_10_frames) / len(last_10_frames) < 0.01:
#                 print("left")
#                 click_mouse('left')
#                 last_10_frames = last_10_frames[10:20]
                    
#     cv2.imshow("eye aim tracking", frame)
#     cv2.waitKey(1)