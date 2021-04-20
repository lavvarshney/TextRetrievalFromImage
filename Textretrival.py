import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en','hi'])

Image("/content/p10.jpg")

output = reader.readtext('/content/p10.jpg')

output

l=len(output)
for i in range(0,l):
  print(output[i][1])