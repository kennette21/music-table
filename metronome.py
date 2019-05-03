import time
from pygame import mixer

def main(bpm = 120, bpb = 4):
    mixer.init()
    metronom = mixer.Sound('metronom-klack.wav')
    start_time = time.time()

    while True:
        cur_time = time.time() -  start_time
        # print("raw current time")
        # print(cur_time)
        # print("rounded current time: ")
        # print(round(cur_time, 1))
        # print("-------------------------------")
        # time.sleep(.01)
        if (cur_time % .5 == 0):
            print(cur_time)
            print(round(cur_time, 3)), "rounded time"
            print("playing metronom")
            mixer.Channel(5).play(metronom)

    # sleep = 60.0 / bpm
    # counter = 0
    # while True:
    #     counter += 1
    #     if counter % bpb:
    #         print 'tick'
    #         mixer.Channel(5).play(metronom)
    #     else:
    #         print 'TICK'
    #         mixer.Channel(5).play(metronom)
    #     time.sleep(sleep)

# def procedure():
#    time.sleep(2.5)
#
# # measure process time
# t0 = time.clock()
# procedure()
# print time.clock(), "seconds process time"
#
# # measure wall time
# t0 = time.time()
# procedure()
# print time.time() - t0, "seconds wall time"



main()
