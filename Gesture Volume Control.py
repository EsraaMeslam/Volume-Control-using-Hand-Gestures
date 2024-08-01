import cv2
import numpy as np
import HandTracking_Module  as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume




w,h=620, 480
cap=cv2.VideoCapture(0)
cap.set(3,w)
cap.set(4,h)

detector=htm.handDetector(detectionCon=.5)



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


# volume.GetMute()
# volume.GetMasterVolumeLevel()
vol_range=volume.GetVolumeRange()
min_vol=vol_range[0]
max_vol=vol_range[1]
vol=0

while True:
    ret,img=cap.read()
    img=detector.findHands(img)
    all_lmlists = detector.find_pos(img)
    for lmlist in all_lmlists:
        if len(lmlist) != 0:
          #  print(lmlist[4],lmlist[8])
            x1,y1=lmlist[4][1],lmlist[4][2]
            x2, y2 = lmlist[8][1], lmlist[8][2]
            cx,cy=(x1+x2)//2,(y1+y2)//2

            cv2.circle(img,(x1,y1),10, (0, 0,0),cv2.FILLED)
            cv2.circle(img,(x2,y2 ),10, (0, 0,0),cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2), (0, 0,0),3)
            cv2.circle(img,(cx,cy),10,(0, 0, 255),cv2.FILLED)

            length=math.hypot(x2-x1,y2-y1)


            vol=np.interp(length,[10,150],[min_vol,max_vol])

            print(vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length<50:
                cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)


    cv2.putText(img, "Volume Control Using Hand Gestures",
                (int(w / 2) - 160, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0,0), 1, cv2.LINE_AA)

    cv2.imshow("Volume Control Using Hand Gestures", img)
    cv2.waitKey(1)

