import requests
import pyzbar.pyzbar as pyzbar
import time
import cv2
import numpy
from PIL import Image
from StringIO import StringIO


def decode(im):
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print("FOUND ONE!")
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

  return decodedObjects

# Main
if __name__ == '__main__':
    try:
        while True:
            cur_img = requests.get("http://192.168.0.12:8080/shot.jpg")
            pl_img = Image.open(StringIO(cur_img.content))
            decObjs = decode(pl_img)

    except KeyboardInterrupt:
        print("im out!!")
