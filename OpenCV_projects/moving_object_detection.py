import cv2 #OpenCV library
import imutils #resize
import time #delay

Camera = cv2.VideoCapture(0)    #initialize the camera
time.sleep(1)
firstFrame = None
area = 500

while True:
    _,Img = Camera.read()      #reading the frame from the video
    text = "Normal"
    Img = imutils.resize(Img, width=500) #resize
    grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY) #color to gray scale image
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gaussianImg # capturing first Frame
        continue
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  #absolute difference b/w firstFrame and gaussian image(current Image)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    countours = cv2.findContours(threshImg.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    countours = imutils.grab_contours(countours)
    for c in countours:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(Img, (x, y), (x+w, y+h), (0, 255, 0))    
    text="Moving object detected"
    cv2.putText(Img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)
    cv2.imshow("VideoStream", Img)  #showing the frame image
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
Camera.release() # releasing the camera
cv2.destroyAllWindows() #destroy all windows








