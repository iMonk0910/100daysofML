#Import libraries
import numpy as np
import imutils
import cv2
import time

#model
prototxt = "MobilenetSSD_deploy.prototext.txt"
model = "MobileNetSSD_deploy.caffemodel"


#Labels of network.
ClassNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }

Threshold_confi = 0.5
colours = np.random.uniform(0, 255, size = (len(ClassNames), 3))
cap = cv2.VideoCapture(0) #open the camera
time.sleep(5)

#Load the Caffe model
MBnet = cv2.dnn.readNetFromCaffe(prototxt, model)

while True:
    ret, frame = cap.read() # Capture frame-by-frame
    
    # MobileNet requires fixed dimensions for input image(s)
    frame_resized = imutils.resize(frame, width = 300) #resized to 300x300 pixels.
    # Size of frame resize (300x300)
    cols = frame_resized.shape[1]
    rows = frame_resized.shape[0]



    blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5)) # blobed image (set a scale factor to image, perform a mean subtraction (127.5, 127.5, 127.5) to normalize the input)

    # blobed image  now has the shape: 1, 3, 300, 300)
    
    MBnet.setInput(blob) #Set the blobed image input to model 
    
    detections = MBnet.forward() #Prediction
    
    
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2] #Confidence of prediction
        if confidence > Threshold_confi : # Filter prediction
            class_id = int(detections[0, 0, i, 1]) # Class label

            # Object location
            xLeftBottom X = int(detections[0, 0, i, 3] * cols)
            yLeftBottom Y = int(detections[0, 0, i, 4] * rows)
            xRightTop   W = int(detections[0, 0, i, 5] * cols)
            yRightTop   H = int(detections[0, 0, i, 6] * rows)


# Factor for scale to original size of frame
            heightFactor = frame.shape[0]/300.0
            widthFactor = frame.shape[1]/300.0
            # Scale object detection to frame
            xLeftBottom = int(widthFactor * xLeftBottom)
            yLeftBottom = int(heightFactor * yLeftBottom)
            xRightTop   = int(widthFactor * xRightTop)
            yRightTop   = int(heightFactor * yRightTop)
            
            cv2.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop), (0, 255, 0)) # location of object
           
            if class_id in ClassNames:
                label = ClassNames[class_id] + ": " + str(confidence)
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                yLeftBottom = max(yLeftBottom, labelSize[1])

                cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                     (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                     (255, 255, 255), cv2.FILLED)
                cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

                print(label) #print class and confidence

    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) >= 0: #Break       
        break
