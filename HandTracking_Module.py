
import cv2
import mediapipe as mp  # for hand detection

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        # Initialize the default parameters
        self.mode = mode
        self.maxHands = maxHands  # no of hands
        self.detectionCon = detectionCon  # min detection confidence threshold
        self.trackCon = trackCon  # min tracking confidence threshold

        self.mp_Hands = mp.solutions.hands  # hand module
        self.hands = self.mp_Hands.Hands(self.mode, self.maxHands,
                                         min_detection_confidence=self.detectionCon,
                                         min_tracking_confidence=self.trackCon)
        self.mp_draw = mp.solutions.drawing_utils  # drawing

    def findHands(self, img, draw=True):
        img = cv2.flip(img, 1)  # flip to match selfie vid
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cvt from BGT TO RGB
        self.res = self.hands.process(img_RGB)

        if self.res.multi_hand_landmarks:  # draw landmarks
            for hand_lms in self.res.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_Hands.HAND_CONNECTIONS)
        return img

    def find_pos(self, img, draw=True):
        all_lmlists = []  # store all landmarks positions
        if self.res.multi_hand_landmarks:
            for hand_lms in self.res.multi_hand_landmarks:
                lmlist = []
                for id, lm in enumerate(hand_lms.landmark):
                    h, w, c = img.shape  # dimensions
                    cx, cy = int(lm.x * w), int(lm.y * h)  # centers
                    lmlist.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 6, (0, 0, 255), cv2.FILLED)
                all_lmlists.append(lmlist)
        return all_lmlists

def main():
    cap = cv2.VideoCapture(0)  # start vid capture
    detector = handDetector()  # object from the class
    while True:
        ret, img = cap.read()
        img = detector.findHands(img)  # detect hands
        all_lmlists = detector.find_pos(img)  # get positions
        for lmlist in all_lmlists:
            if len(lmlist) != 0:
                print(lmlist[4])

        cv2.imshow('image', img)  # Display the frame
        if cv2.waitKey(1) & 0xFF == ord('q'):  # exit (stop) 'q'
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
