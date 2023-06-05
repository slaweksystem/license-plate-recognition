from anrp import PyImageSearchANPR
import imutils
import cv2

def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

class Detector:
    def __init__(self, psm = 8, clear_border = -1):
        self.anrp = PyImageSearchANPR(debug = False)
        self.psm = psm
        self.clear_border = clear_border

    def detect(self, image):

        license_plates = ""

        # Resize image
        image = imutils.resize(image, width=600)

        # apply automatic license plate recognition
        (lpText, lpCnt) = self.anrp.find_and_ocr(image, psm=self.psm,
            clearBorder=self.clear_border > 0)

        # only continue if the license plate was successfully OCR'd
        if lpText is not None and lpCnt is not None:
            # fit a rotated bounding box to the license plate contour and
            # draw the bounding box on the license plate
            box = cv2.boxPoints(cv2.minAreaRect(lpCnt))
            box = box.astype("int")
            cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

            # compute a normal (unrotated) bounding box for the license
            # plate and then draw the OCR'd license plate text on the
            # image
            (x, y, w, h) = cv2.boundingRect(lpCnt)
            cv2.putText(image, cleanup_text(lpText), (x, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            # show the output ANPR image
            #print("[INFO] {}".format(lpText))
            #cv2.imshow("Output ANPR", image)
            #cv2.waitKey(0)
            license_plates = lpText


        if license_plates == "":
            license_plates = "No license plate detected"
        return image, license_plates

