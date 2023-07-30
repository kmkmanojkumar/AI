#pip install opencv-python
#pip install mediapipe
import cv2
import mediapipe as mp
import pyautogui as p
#import autopy
mp_hands = mp.solutions.hands
drawing=mp.solutions.drawing_utils
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)
screen_w,screen_h=p.size()
screen_y=0
while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    height,width,_=frame.shape
    if not ret:
        break
    # Convert the image to RGB and process it with the hand detection module
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    hand1=results.multi_hand_landmarks
    #print(results.multi_hand_landmarks)
    if hand1:
        for hand in hand1:
            drawing.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*width)
                y=int(landmark.y*height)
                print(x,y)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    screen_x = int(screen_w/width * x)
                    screen_y = int(screen_h/height * y)
                    print("screen",screen_y)
                    # Move the mouse to the screen coordinates
                    p.moveTo(screen_x, screen_y)
                if id==12:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thum_x = int(screen_w/width * x)
                    thum_y = int(screen_h/height * y)
                    print("thum",thum_y)
                    print("abs",abs(screen_y-thum_y))
                    if abs(screen_y-thum_y)<30:
                        print("click")
                        p.click()
                        p.sleep(1)
                    
               
            # Get the x, y, and z coordinates of the index finger
            '''index_finger_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            index_finger_z = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
            # Convert the coordinates to screen coordinates
            screen_x = int(index_finger_x * width)
            screen_y = int(index_finger_y * height)
            print(screen_x,screen_y)'''
    cv2.imshow('VM',frame)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
        
