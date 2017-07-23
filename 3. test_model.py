import numpy as np
from grabscreen import grab_screen
import cv2
import time
import directkeys
from models import alexnet2, alexnet
from getkeys import key_check
import random
import input_output

WIDTH = input_output.NUM_INPUT_DIMENSIONS_X
HEIGHT = input_output.NUM_INPUT_DIMENSIONS_Y
LR = 1e-3
MODEL_NAME = 'pybandicoot-model-alexnet2.model'

model = alexnet2(WIDTH, HEIGHT, LR, output = input_output.NUM_OUTPUT_DIMENSIONS)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = True
    try:
        while True:
            
            if not paused:
                # 800x600 windowed mode
                screen = grab_screen(region=(0,40,1280,720))
                last_time = time.time()
                screen = input_output.screencap_to_input(screen)

                prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
                #print(prediction)

                keys = input_output.output_to_keys(prediction)
                #print(keys)
                keys = directkeys.keys_to_direct(keys)
                directkeys.ReleaseAll()
                directkeys.PressKeys(keys)
                
            keys = key_check()

            # p pauses game and can get annoying.
            if 'T' in keys:
                if paused:
                    paused = False
                    print("Unpaused!")
                    time.sleep(1)
                else:
                    paused = True
                    print("Paused!")
                    directkeys.ReleaseAll()
                    time.sleep(1)
    finally:
        directkeys.ReleaseAll()

main()       
