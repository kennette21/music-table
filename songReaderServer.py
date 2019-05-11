from flask import Flask
import cv2
import pyzbar.pyzbar as pyzbar

#qr_index_dict = {'vocal-3': 11, 'vocal-0': 8, 'drum-2': 14, 'vocal-2': 10, 'drum-3': 15, 'drum-0': 12, 'drum-1': 13, 'vocal-1': 9, 'melody-3': 7, 'melody-2': 6, 'melody-1': 5, 'melody-0': 4, 'bass-0': 0, 'bass-1': 1, 'bass-2': 2, 'bass-3': 3}
TRACK_COUNT = 16
app = Flask(__name__)

print("intializing")
cap = cv2.VideoCapture(1)

@app.route('/')
def hello_world():
    return get_qr_codes()

def get_qr_codes():
    song_state = [0]*16
    ret, frame = cap.read()
    if (ret):
        qr_codes = pyzbar.decode(frame)
        if len(qr_codes) > 0:
            for code in qr_codes:
                song_state[qr_index_dict[code.data]] = 1
            
            return str(song_state)
        else:
            return str(song_state)
    else:
        #failed to read camera
        return 'failed to read camera'

def generate_index_map():
    inst_list = ["bass","melody","vocal","drum"]
    qr_index_dict = {}
    for i in range(4):
        for j in range(4):
            index = j+i*4
            inst_string = inst_list[i]+'-'+str(j)
            qr_index_dict[inst_string] = index
    return qr_index_dict

qr_index_dict = generate_index_map()

