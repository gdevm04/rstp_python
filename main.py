import cv2
import os
from dotenv import load_dotenv


load_dotenv()


rtsp_url = os.getenv('RTSP_URL')    

cap = cv2.VideoCapture(rtsp_url)

cv2.namedWindow('Câmera', cv2.WINDOW_NORMAL)


cv2.setWindowProperty('Câmera', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()

    

    
    height, width = frame.shape[:2]
    new_width = 1500
    new_height = int((new_width/width) * height)
    resized_frame = cv2.resize(frame, (new_width, new_height))


    

    
    cv2.imshow('Câmera', resized_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()