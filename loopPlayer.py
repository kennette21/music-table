# this file is meant for experiemnt with pygame sound
from pygame import mixer
import glob
import cv2



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

    sounds = save_sounds()

    print(sounds)

    prompt_bass = int(raw_input("pick a drum line (0, 1, or 2): "))
    mixer.Channel(0).play(sounds.get('bass')[prompt_bass], -1)
    prompt_melody = int(raw_input("pick a melody (0, 1, or 2): "))
    mixer.Channel(1).play(sounds.get('organ')[prompt_melody], -1)
    prompt_vocals = int(raw_input("finally throw in some vocals (0, 1, or 2): "))
    mixer.Channel(2).play(sounds.get('vocals')[prompt_vocals], -1)

    while True:
        k = cv2.waitKey(1) & 0xFF
        # press 'q' to exit
        if k == ord('q'):
            break
        elif k == ord('b'):
            if mixer.Channel(0).get_busy():
                mixer.Channel(0).stop()
        elif k == ord('o'):
            if mixer.Channel(1).get_busy():
                mixer.Channel(1).stop()
        elif k == ord('v'):
            if mixer.Channel(2).get_busy():
                mixer.Channel(2).stop()
        elif k == ord('c'):
            print("working on changeing music!")
            # change a variable / do something ...
