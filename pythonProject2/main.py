import cv2
from matplotlib import pyplot as plt
import numpy as np

fotograf = cv2.imread("rose.jpg", 0)

# dosyanın okunup okunamadığından emin olmak için kontrol ediyorum

if fotograf is not None:
    Hist = np.zeros(256)
    w, h = fotograf.shape

    for i in range(0,w):
        for j in range(0,h):
            a = fotograf[i, j]
            Hist[a] = Hist[a] + 1

    plt.plot(Hist)
    plt.show()

    cv2.imshow("rose", fotograf)
    cv2.waitKey(0)


else:
    print("Dosya okunamadı veya bulunamadı.")




