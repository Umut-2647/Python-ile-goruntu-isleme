import os
import cv2

path = os.path.join(os.getcwd(),"Python_ile_goruntu_isleme","Opencv_ile_Image_Temelleri","media","manzara.jpeg")
print(path)
img =cv2.imread(path)


while True:
    cv2.imshow("Manzara resmi",img)
    if cv2.waitKey(1) & 0xFF == 27:  # esc tuşuna basıldığında pencereyi kapat
        break

cv2.destroyAllWindows()