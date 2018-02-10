import cv2

detector = cv2.CascadeClassifier('C:/Users/Omer/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
img = cv2.imread("C:/Users/Omer/Desktop/b.jpg")

while (True):
    gray = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
    faces = detector.detectMultiScale(gray,1.3,5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,0, 255), 2)#renkler 0,0,255=kýrmýzý

    cv2.imshow('Yuz Tanima v.1', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #çýkýþ için 'q' ya bas
        break

img.release()
cv2.destroyAllWindows()