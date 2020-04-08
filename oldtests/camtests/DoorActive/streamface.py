import cv2
import sys
import RPi.GPIO as GPIO
import datetime
import os
import time

doorbell = 3
doorring = 5
print("Waiting Doorbell")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(doorbell,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(doorring,GPIO.OUT)

faceCascade = cv2.CascadeClassifier('facehaar2.xml')

video_capture = cv2.VideoCapture(1)
video_capture.set(3,320)
video_capture.set(4,240)


path = None
timeout = None
while True:
    if GPIO.input(doorbell) == GPIO.LOW:
        GPIO.output(doorring,True)
        time.sleep(1)
        GPIO.output(doorring,False)
        time.sleep(.5)
        path = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timeout = time.time()+30
        if not os.path.exists("Captured/"+path):
            os.makedirs("Captured/"+path)
        break
        
while time.time()<timeout:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=2
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # if not os.path.exists("Captured/"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        #     os.makedirs("Captured/"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cv2.imwrite("Captured/"+path+"/"+str(int(datetime.datetime.now().strftime("%S"))%5)+".png",frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()