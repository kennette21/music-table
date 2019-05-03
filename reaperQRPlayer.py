import requests
import pyzbar.pyzbar as pyzbar
# from Pillow import Image
from StringIO import StringIO


LOOP_TYPES = ["bass", "melody", "drum", "vocal"]
CUR_PLAYING = []
CONT_PLAYING = []
SOUNDS = {}
TYPE_CANNEL_MAPPER = {"bass": 0, "drum": 1, "vocal": 2, "melody": 3}
TRACK_DICT = {"bass": [], "drum": [], "vocal": [], "melody": []}

def detect_loop(image):
    qr_codes = pyzbar.decode(image)

    for code in qr_codes:
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
    CUR_PLAYING.append(loop)
    CONT_PLAYING.append(loop)
    loop_type = loop.split("-")[0]
    index = int(loop.split("-")[1])
    toggle_mute(TRACK_DICT[loop_type][index])

def continue_loop(loop):
    CONT_PLAYING.append(loop)

def stop_loop(loop):
    loop_type = loop.split("-")[0]
    index = int(loop.split("-")[1])
    try:
        CUR_PLAYING.remove(loop)
        toggle_mute(TRACK_DICT[loop_type][index])
        # we need to load all the tracks, then map them so we can toggle mute
        # mixer.Channel(TYPE_CANNEL_MAPPER[loop_type]).stop()
    except ValueError:
        print("SHIT!! REMOVING ALREADY REMOVED SONG")
        
def toggle_mute(track):
    if RPR_SetMediaTrackInfo_Value(track, 'B_MUTE'):   
      RPR_SetMediaTrackInfo_Value(tr, 'B_MUTE', False)
    else:
      RPR_SetMediaTrackInfo_Value(tr, 'B_MUTE', True)

def see_song():
    empty_list = []
    CONT_PLAYING = empty_list
    cur_img = requests.get("http://192.168.0.12:8080/shot.jpg")
    pl_img = Image.open(StringIO(cur_img.content))
    detect_loop(pl_img)

# Main
if __name__ == '__main__':
    for i in range(0,13):
      if (0 <= i <= 3):
        TRACK_DICT["bass"].append(RPR_GetTrack(0,i))
      if (4 <= i <= 7):
        TRACK_DICT["drum"].append(RPR_GetTrack(0,i))  
      if (9 <= i <= 12):
        TRACK_DICT["melody"].append(RPR_GetTrack(0,i))

    RPR_defer("see_song()")
