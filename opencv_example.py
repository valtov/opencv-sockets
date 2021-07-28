import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FPS, 20)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while(True):
    ret, frame = cap.read()
    print('****\n', frame, '$$$$\n')
    cv2.imshow('frame window to capture video', frame)
    k = cv2.waitKey(30) 
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
