import cv2
import mediapipe as mp
import pickle
import numpy as np


model_dict = pickle.load(open("/home/adrien_hs/Documentos/8_IA_RECOGNIZE/model_manos.p",'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_draw_style = mp.solutions.drawing_styles


hands = mp_hands.Hands(static_image_mode = True, max_num_hands = 1, min_detection_confidence = 0.3)

cap = cv2.VideoCapture(0)

labels_dict = {0:'A', 1:'A', 2:'B', 3:'B', 4:'C', 5:'C', 6:'D', 7:'D', 8:'E', 9:'E', 10:'F', 11:'F'}
while True:
    data_aux = []
    x_ = []
    y_ = []
    
    ret,frame = cap.read()
    
    H,W, _= frame.shape
    
    frame = cv2.flip(frame,1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            """mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_draw_style.get_default_hand_landmarks_style(),
                mp_draw_style.get_default_hand_connections_style()
            )"""
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame,hand_landmarks,mp_hands.HAND_CONNECTIONS
                )
        
        
        #for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)
                x_.append(x)
                y_.append(y)
        
        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10
        
        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10
                
        prediction = model.predict([np.asarray(data_aux)])
        
        predicted_char = labels_dict[int(prediction[0])]
    
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,0), 4)
        cv2.putText(frame,predicted_char,(x1,y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,0),3,cv2.LINE_AA)
                
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 27:
            break
        
        
cap.release()
cv2.destroyAllWindows()