import cv2

# Read Image
img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,500,255))
cv2.putText(img,
            "Earth",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,400,255))
cv2.putText(img,
            "Mercuray",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,350,255))
cv2.putText(img,
            "Venus",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,300,255))
cv2.putText(img,
            "Jupiter",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,50,255))
cv2.putText(img,
            "Saturn",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,100,255))
cv2.putText(img,
            "Urans",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,150,255))
cv2.putText(img,
            "Neptune",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,200,255))

cv2.imwrite("solar-system.jpg",img)