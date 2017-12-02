import cv2
import sys
import urllib3
import time;

video_name = sys.argv[1]
count = 0
lastCount = 0;
lastTime = time.time();
http = urllib3.PoolManager()
def sendRequestToServer(arg):
    r = http.request('GET', "http://localhost/ocv.php?count=" + str(arg))
vid = cv2.VideoCapture(video_name)
font = cv2.FONT_HERSHEY_SIMPLEX

car_cascade = cv2.CascadeClassifier('cars.xml')
f=0
while f==0:
    try:
        ret, frames = vid.read()

        grey = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(grey, 1.1, 1)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
            count = count + 1
            cv2.putText(frames,str(count),(10,50), font, 1,(0,0,0),2,cv2.LINE_AA)
            if (time.time()>=lastTime+5):
                sendRequestToServer(count-lastCount)
                lastCount = count
                lastTime = time.time()

        cv2.imshow('Video Output', frames)

        if cv2.waitKey(33) == 27:
            break
    except:
        f=1


cv2.destroyAllWindows()
re=http.request('GET',"http://localhost/generate_csv.php")
print("hey")