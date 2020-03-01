# import cv2

# #print("Before URL")
# # cap = cv2.VideoCapture('http://192.168.100.12:8080/jsfs.html')
# cap = cv2.VideoCapture('https://www.youtube.com/watch?v=2H1Gho3LOUE')
# #print("After URL")

# while True:

#     #print('About to start the Read command')
#     ret, frame = cap.read()
#     #print('About to show frame of Video.')
#     cv2.imshow("Capturing",frame)
#     #print('Running..')

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import urllib.request as ur
# import numpy as np

# stream = ur.urlopen('http://192.168.100.12:8080/browserfs.html')
# bytes = ''
# while True:
#     bytes += stream.read(1024)
#     a = bytes.find('\xff\xd8')
#     b = bytes.find('\xff\xd9')
#     if a != -1 and b != -1:
#         jpg = bytes[a:b+2]
#         bytes = bytes[b+2:]
#         i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
#         cv2.imshow('i', i)
#         if cv2.waitKey(1) == 27:
#             exit(0)  

import numpy as np
import cv2

# Open a sample video available in sample-videos
vcap = cv2.VideoCapture('http://192.168.100.12:8080/browserfs.html')
#if not vcap.isOpened():
#    print "File Cannot be Opened"

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print ("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print ("Video stop")