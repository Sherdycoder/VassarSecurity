import cv2
import sys
import winsound
import time
import random

cascPath =  "haarfront.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
clips = ('vassar.wav', 'vassar2.wav', 'vassar3.wav', 'vassar4.wav', 'vassar5.wav','vassar6.wav','vassar7.wav','vassar8.wav','vassar9.wav')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
#play sound if face is detected    

    if len(faces) != 0: 
        randomclip = random.choice(clips)
        winsound.PlaySound(randomclip,winsound.SND_FILENAME)         
        time.sleep(2)    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
    
