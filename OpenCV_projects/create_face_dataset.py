import cv2, os #OpenCV library
haar_file = "haarcascade_frontalface_default.xml" #accessed the model file
datasets = "datasets"
sub_data = "rr1"


path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.makedirs(path)
(width, height) = (130, 120)

face_cascade = cv2.CascadeClassifier(haar_file)

Camera = cv2.VideoCapture(0)
count = 1
while count < 51:
    (_, Img) = Camera.read()  # reading the frame from the video
    ## Img = imutils.resize(Img, width=500) #resize
    grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # color to gray scale image
    faces = face_cascade.detectMultiScale(grayImg, 1.3, 4)  # gets cordinates of the face
    for (x, y, w, h) in faces:
        cv2.rectangle(Img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face = grayImg[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path, count), face_resize)
        count += 1
    cv2.imshow("OpenCV", Img)

    key = cv2.waitKey(10 & 0xFF)
    if key == ord("q"):
        break
Camera.release()
cv2.destroyAllWindows() #destroy all windows
