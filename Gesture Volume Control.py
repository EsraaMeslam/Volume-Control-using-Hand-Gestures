# # import cv2
# # import numpy as np
# # import HandTracking_Module  as htm
# # import math
# # from comtypes import CLSCTX_ALL
# # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# #
# #
# #
# #
# # w,h=440,380
# # cap=cv2.VideoCapture(0)
# # cap.set(3,w)
# # cap.set(4,h)
# #
# # detector=htm.handDetector(detectionCon=.5)
# #
# #
# #
# # devices = AudioUtilities.GetSpeakers()
# # interface = devices.Activate(
# #     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# # volume = interface.QueryInterface(IAudioEndpointVolume)
# #
# #
# # # volume.GetMute()
# # # volume.GetMasterVolumeLevel()
# # vol_range=volume.GetVolumeRange()
# # min_vol=vol_range[0]
# # max_vol=vol_range[1]
# # vol=0
# # vol_bar=0
# #
# # while True:
# #     ret,img=cap.read()
# #     img=detector.findHands(img)
# #     all_lmlists = detector.find_pos(img,draw=False)
# #     for lmlist in all_lmlists:
# #         if len(lmlist) != 0:
# #           #  print(lmlist[4],lmlist[8])
# #             x1,y1=lmlist[4][1],lmlist[4][2]
# #             x2, y2 = lmlist[8][1], lmlist[8][2]
# #             cx,cy=(x1+x2)//2,(y1+y2)//2
# #
# #             cv2.circle(img,(x1,y1),10,(0,0,0),cv2.FILLED)
# #             cv2.circle(img,(x2,y2 ),10,(0,0,0),cv2.FILLED)
# #             cv2.line(img,(x1,y1),(x2,y2),(0,0,0),3)
# #             cv2.circle(img,(cx,cy),10,(0,0,0),cv2.FILLED)
# #
# #             length=math.hypot(x2-x1,y2-y1)
# #            # print(length)
# #           #Hand range 50 to 300
# #           #vol Range -65 to 0
# #           #10 :100,w,h=440,380
# #
# #
# #             vol=np.interp(length,[10,100],[min_vol,max_vol])
# #             vol_bar = np.interp(length, [10, 100], [400, 150])
# #             print(vol)
# #             volume.SetMasterVolumeLevel(vol, None)
# #
# #             if length<50:
# #                 cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
# #     cv2.rectangle(img,(50,150),(85,400),(0,0,0),2)
# #     cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 0, 0), cv2.FILLED)
# #     #cv2.putText()
# #     # if (len(lmlist)!=0):
# #     #     print(lmlist[4],lmlist[8])
# #
# #     cv2.putText(img, "Gesture Volume Control", (int(w / 2) - 100, 30),
# #                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
# #     cv2.imshow("Gesture Volume Control ",img)
# #     cv2.waitKey(1)
#
#
# import cv2
# import numpy as np
# import HandTracking_Module as htm
# import math
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#
# w, h = 440, 380
# cap = cv2.VideoCapture(0)
# cap.set(3, w)
# cap.set(4, h)
#
# detector = htm.handDetector(detectionCon=0.5)
#
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = interface.QueryInterface(IAudioEndpointVolume)
#
# vol_range = volume.GetVolumeRange()
# min_vol = vol_range[0]
# max_vol = vol_range[1]
#
# vol = 0
# vol_bar = 400
# vol_per = 0
#
# while True:
#     ret, img = cap.read()
#     img = detector.findHands(img)
#     all_lmlists = detector.find_pos(img)
#
#     if len(all_lmlists) != 0:
#         lmlist = all_lmlists[0]
#         x1, y1 = lmlist[4][1], lmlist[4][2]
#         x2, y2 = lmlist[8][1], lmlist[8][2]
#         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
#
#         cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED)  # Green circle
#         cv2.circle(img, (x2, y2), 10, (0, 255, 0), cv2.FILLED)  # Green circle
#         cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)  # Green line
#         cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
#
#         length = math.hypot(x2 - x1, y2 - y1)
#
#         vol = np.interp(length, [10, 100], [min_vol, max_vol])
#         vol_bar = np.interp(length, [10, 100], [400, 150])
#         vol_per = np.interp(length, [10, 100], [0, 100])
#
#         volume.SetMasterVolumeLevel(vol, None)
#
#         if length < 50:
#             cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
#
#     # # Draw volume bar
#     # cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 2)
#     # cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 0, 0), cv2.FILLED)
#     # cv2.putText(img, f'{int(vol_per)} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
#
#     # Draw volume level in discrete steps
#     num_bars = 10
#     bar_height = (400 - 150) // num_bars
#     vol_step = (max_vol - min_vol) / num_bars
#     current_step = int((vol - min_vol) / vol_step)
#
#     # for i in range(num_bars):
#     #     bar_top = 400 - (i + 1) * bar_height
#     #     bar_bottom = bar_top + bar_height - 2
#     #     bar_color = (0, 0, 0) if i < current_step else (200, 200, 200)
#     #     cv2.rectangle(img, (90, bar_top), (120, bar_bottom), bar_color, cv2.FILLED)
#
    # cv2.putText(img, "Volume Control Using Hand Gestures",
    #             (int(w / 2) - 150, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
    #
    # cv2.imshow("Volume Control Using Hand Gestures", img)
    # cv2.waitKey(1)
#

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

