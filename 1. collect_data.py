import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import input_output

starting_value = 1

filename_format = 'training_data-{}.npy'
file_name = 'training_data-1.npy'

while True:
    file_name = filename_format.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        break

def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []

    paused = True
    show_im = False
    while(True):
        if not paused or show_im:
            screen = grab_screen(region=(0,40,1280,720))
            screen = input_output.screencap_to_input(screen)
            
            keys = key_check()
            output = input_output.keys_to_output(keys)

            if show_im:
                cv2.imshow('window',screen)
                #print(output)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

            if not paused:
                training_data.append([screen,output])
                if len(training_data) % 100 == 0:
                    print(len(training_data))
                    
                    if len(training_data) % 2000 == 0:
                        np.save(file_name,training_data)
                        training_data = []
                        starting_value += 1
                        file_name = filename_format.format(starting_value)
                        print('SAVED')
                    
        keys = key_check()
        if 'T' in keys:
            paused = not paused
            if paused:
                print('Paused!')
            else:
                print('Unpaused!')
            time.sleep(0.2)
        if 'Y' in keys:
            show_im = not show_im
            if show_im:
                print('Showing IM!')
            else:
                print('Not showing IM!')
            time.sleep(0.2)


main(file_name, starting_value)
