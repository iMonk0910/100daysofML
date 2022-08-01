import cv2 #OpenCV library

model = "haarcascade_frontalface_default.xml" #accessed the model file
haar_cascade = cv2.CascadeClassifier(model) #loading the model with cv2
Camera = cv2.VideoCapture(0)    #initialize the camera

while True:
    _,Img = Camera.read()      #reading the frame from the video
    text = "Normal"
    Img = imutils.resize(Img, width=500) #resize
    grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY) #color to gray scale image
    face = haar_cascade.detectMultiScale(grayImg,1.3, 4) #gets cordinates of the face

    for (x, y, w, h) in face:
        cv2.rectangle(Img, (x, y), (x+w, y+h), (0, 255, 0),2)
    cv2.putText(Img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)
    cv2.imshow("FaceDetected",Img)
    key = cv2.waitKey(10 & 0xFF)
    if key == ord("q"):
        break
Camera.release() # releasing the camera
cv2.destroyAllWindows() #destroy all windows
