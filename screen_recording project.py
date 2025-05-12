import pyautogui
import numpy as np
import cv2

resolution =(1920,1080)
codec=cv2.VideoWriter_fourcc(*"XVID")
my_file = "recording.avi"
fps=70.0
out=cv2.VideoWriter(my_file,codec,fps,resolution)
cv2.namedWindow("live",cv2.WINDOW_NORMAL)
cv2.resizeWindow("live",520,520)

while True:
    img = pyautogui.screenshot()
    frame =np.array(img)

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("live",frame)
    if cv2.waitKey(1) == ord('q'):
        break
out.release()
cv2.destroyAllWindows