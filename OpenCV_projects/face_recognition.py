import cv2, numpy, os #OpenCV library
size = 4
haar_file = "haarcascade_frontalface_default.xml" #accessed the model file
datasets = "datasets"
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    print(dir)
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + "/" + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(label)
        id += 1

(width, height) = (130, 120)
(images, labels) = [numpy.array(xx) for xx in [images, labels]]
#print(images, labels)
model = cv2.face.LBPHFaceRecognizer_create()
#model = cv2.face.FisherFaceRecognizer_create()
model.train(images, labels)
face_cascade = cv2.CascadeClassifier(haar_file)

Camera = cv2.VideoCapture(0)    #initialize the camera
cnt = 0
while True:
    (_, Img) = Camera.read()      #reading the frame from the video
   ## Img = imutils.resize(Img, width=500) #resize
    grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY) #color to gray scale image
    faces = face_cascade.detectMultiScale(grayImg, 1.3, 5) #gets cordinates of the face

    for (x, y, w, h) in faces:
        cv2.rectangle(Img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        face = grayImg[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(Img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if(prediction[1] < 800):
          cv2.putText(Img, "%s - %.0f" % (names[prediction[0]], prediction[1]), (x-10, y-20), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 0, 255), 2)
          print(names[prediction[0]])
          cnt = 0
        else:
          cnt+=1
          cv2.putText(Img,'Unknown', (x-10, y-20), cv2.FONT_HERSHEY_PLAIN, 1,(0, 255, 0), 2)

          if(cnt>100):
            print("Unknown Person")
            cv2.imwrite("input.jpg", Img)
            cnt = 0
    cv2.imshow("OpenCV", Img)
    key = cv2.waitKey(10 & 0xFF)
    if key == ord("q"):
      break
Camera.release() # releasing the camera
cv2.destroyAllWindows() #destroy all windows
