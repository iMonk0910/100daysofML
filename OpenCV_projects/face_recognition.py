import cv2, numpy, os #OpenCV library
size = 4
model = "haarcascade_frontalface_default.xml" #accessed the model file
haar_cascade = cv2.CascadeClassifier(model) #loading the model with cv2
datasets = "datasets"
(image,labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(detasets):
  for subdir in dir:
    names[id] = subdir
    subjectpath = os.path.join(datasets, subdir)
    for filename in os.listdir(subjectpath):
      path = subjectpath + "/" + filename
      label =id
      images.append(cv2.imread(path, 0 ))
      labels.append(int(labels))

(width,height) = (150,120)
(images, labels) = [numpy.array(xx) for xx in [images,labels]]
#print(images, labels)
model = cv2.face.LBPHFaceRecognizer_create()
#model = cv2.face.FisherFaceRecognizer_create()
model.train(width,height)
face_cascade = cv2.CascadeClassifier(haar_file)

Camera = cv2.VideoCapture(0)    #initialize the camera
cnt = 0
while True:
    _,Img = Camera.read()      #reading the frame from the video
   ## Img = imutils.resize(Img, width=500) #resize
    grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY) #color to gray scale image
    face = haar_cascade.detectMultiScale(grayImg,1.3, 4) #gets cordinates of the face
