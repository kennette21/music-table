import requests
import pyzbar.pyzbar as pyzbar
import time
import cv2
import numpy
from PIL import Image
from StringIO import StringIO
from pygame import mixer
import glob


LOOP_TYPES = ["bass", "melody", "drum", "vocal"]
CUR_PLAYING = []
CONT_PLAYING = []
SOUNDS = {}
TYPE_CANNEL_MAPPER = {"bass": 0, "drum": 1, "vocal": 2, "melody": 3}

def decode(im):
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print("FOUND ONE!")
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

  return decodedObjects

def detect_loop(image):
    qr_codes = pyzbar.decode(image)

    for code in qr_codes:
        # print("****** new loop")
        loop = code.data
        if loop in CUR_PLAYING:
            continue_loop(loop)
        else:
            loop_type = code.data.split("-")[0]
            if loop_type in LOOP_TYPES:
                start_loop(loop)

    manage_song()

def manage_song():
    for loop in CUR_PLAYING:
        if loop not in CONT_PLAYING:
            stop_loop(loop)


def start_loop(loop):
    # mixer.music.play(song) with channel
    print("+ start: " + loop)
    CUR_PLAYING.append(loop)
    CONT_PLAYING.append(loop)
    loop_type = loop.split("-")[0]
    index = int(loop.split("-")[1])
    mixer.Channel(TYPE_CANNEL_MAPPER[loop_type]).play(SOUNDS.get(loop_type)[index], -1)

def continue_loop(loop):
    CONT_PLAYING.append(loop)

def stop_loop(loop):
    loop_type = loop.split("-")[0]
    print("- stop: " + loop)
    try:
        CUR_PLAYING.remove(loop)
        mixer.Channel(TYPE_CANNEL_MAPPER[loop_type]).stop()
    except ValueError:
        print("SHIT!! REMOVING ALREADY REMOVED SONG")


def save_sounds():
    loops_dir = glob.glob("/Users/tbean/Projects/mashMachine/loops/*")
    sounds = {}
    for category in loops_dir:
        # import pdb; pdb.set_trace()
        category_name = category.split('/')[-1]
        sounds[category_name] = []
        category_sound_files = glob.glob(category + "/*")
        for sound_file in category_sound_files:
            # import pdb; pdb.set_trace()
            sound_name = sound_file.split('/')[-1]
            print("creating sound_name: " + str(sound_name) + " with file: " + str(sound_file))
            sounds[category_name].append(mixer.Sound(sound_file))

    return sounds


# Main
if __name__ == '__main__':
    mixer.init()

    cap = cv2.VideoCapture(1)

    SOUNDS = save_sounds()

    try:
        while True:
            empty_list = []
            CONT_PLAYING = empty_list
            # cur_img = requests.get("http://192.168.0.12:8080/shot.jpg")
            # pl_img = Image.open(StringIO(cur_img.content))
            ret, frame = cap.read()


            # decObjs = decode(pl_img)
            detect_loop(pl_img)


    except KeyboardInterrupt:
        print("im out!!")
