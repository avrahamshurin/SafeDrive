import cv2
import time


class CameraOperator:
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
    def __init__(self):
        # todo initialization
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        self.blink_count = 0
        self.timeBetweenBlinks = 0
        self.blinktime = 0
        self.startBlink = True
        self.maxtime = 0
        self.timer = time.time()
        self.initial = True
        self.main()

    def main(self):

        while True:
            _, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = CameraOperator.face_cascade.detectMultiScale(gray, 1.3, 5)
            for x, y, h, w in faces:
                cv2.rectangle(frame, (x, y), (x + h, y + w), (255, 0, 0), 2)
                roi = gray[y:y + h // 2, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                eyes = CameraOperator.eye_cascade.detectMultiScale(roi, 1.1, 6)

                if self.timeBetweenBlinks > self.maxtime:
                    self.maxtime = self.timeBetweenBlinks
                    print(self.maxtime)

                if len(eyes) == 0:
                    if self.initial:
                        self.timer = time.time()
                        self.initial = False
                        self.currentTime = time.time()



                    # self.blinktime = time.time() - self.timer
                    #if self.blinktime > 1:
                        # print("wake up")
                        #print(self.blinktime)
                    # if self.startBlink:
                    #     self.startBlink = False
                    #     self.timer = time.time()
                    #if self.blink_count == 0:
                     #   self.currentTime = time.time()
                    else:
                        if time.time() - self.currentTime > 0.01:
                            self.timeBetweenBlinks = time.time() - self.currentTime
                        # print(self.timeBetweenBlinks)
                        self.currentTime = time.time()
                        self.blink_count += 1
                    self.blinktime = time.time() - self.timer
                else:
                    self.startBlink = True
                    self.initial = True

                for ex, ey, eh, ew in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + eh, ey + ew), (0, 255, 0), 2)

            cv2.imshow("image", frame)

            if cv2.waitKey(30) & 0xFF == 27:
                break

        cv2.destroyAllWindows()
        self.cap.release()

    def get_time_between_blinks(self):
        return self.timeBetweenBlinks

    def get_time_eyes_closed(self):
        return self.blinktime



CameraOperator()