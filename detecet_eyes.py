import cv2
import time


cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
face_cascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade =cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
blink_count = 0
timeBetweenBlinks = 0
blinktime = 0
startBlink = True
maxtime = 0
timer = time.time()
initial = True
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x,y,h,w in faces:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,0),2)
        roi = gray[ y:y+h//2,x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi,1.1,6)

        if timeBetweenBlinks>maxtime:
            maxtime = timeBetweenBlinks
            print(maxtime)

        if len(eyes) == 0:
            if initial:
                timer = time.time()
                initial = False
            blinktime = time.time() - timer
            if blinktime > 1:
                print("wake up")
                print(time.time() - timer)
            if startBlink:
                startBlink = False
                timer = time.time()
            if blink_count == 0:
                currentTime = time.time()
            else:
                timeBetweenBlinks = time.time() - currentTime
                currentTime = time.time()
            blink_count += 1
        else:
            startBlink = True
            initial = True


        for ex, ey, eh, ew in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + eh, ey + ew), (0, 255, 0), 2)

    cv2.imshow("image",frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()