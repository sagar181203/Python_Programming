import cv2
cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	if ret == False:
		break

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)	
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	txt = "Found {0} faces!".format(len(faces))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		cv2.putText(frame, text= txt, org=(200, 100),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),
            thickness=2, lineType=cv2.LINE_AA)


	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(100) & 0xFF == 27:
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
