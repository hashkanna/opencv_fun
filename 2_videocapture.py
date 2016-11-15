import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#out = cv2.VideoWriter('output.mp4', fourcc, 8, (width*2, height*2))
out = cv2.VideoWriter('output.mp4', fourcc, 8, (width*2, height))

#cap.set(3, 640)
#cap.set(4, 480)
zeros = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    zeros = np.zeros((720, 1280), dtype='uint8')

    (B, G, R) = cv2.split(frame)
    R = cv2.merge([zeros, zeros, R])
    G = cv2.merge([zeros, G, zeros])
    B = cv2.merge([B, zeros, zeros])
    gray = cv2.merge([gray, gray, gray])

    '''output = np.zeros((720*2, 1280*2, 3), dtype='uint8')
    output[0:height, 0:width] = frame
    output[0:height, width:width * 2] = R
    output[height:height * 2, width:width * 2] = G
    output[height:height * 2, 0:width] = B'''

    output = np.zeros((720, 1280*2, 3), dtype='uint8')
    output[0:720, 0:1280] = frame
    output[0:720, 1280:1280*2] = gray

    out.write(output)
    #print(width, height)
    #out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
