import numpy as np
import cv2
import time
from getkeys import key_check
from grabscreen import grab_screen
import os

def keys_to_output(keys):
    #[A,W,D]

    output = [0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

file_name = 'training_data.npy'

def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    
    while True:
        screen = grab_screen(region=(0,40,800,640))
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

main()
