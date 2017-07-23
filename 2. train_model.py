import numpy as np
from models import alexnet, alexnet2, inception_v3 as googlenet
from random import shuffle
import pandas as pd
import input_output
from datetime import datetime
import os

# what to start at
START_NUMBER = 1

# what to end at
END_NUMBER = 10

# use a previous model to begin?
START_FRESH = False

WIDTH = input_output.NUM_INPUT_DIMENSIONS_X
HEIGHT = input_output.NUM_INPUT_DIMENSIONS_Y
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pybandicoot-model-alexnet2.model'
EXISTING_MODEL_NAME = 'pybandicoot-model-alexnet2.model'

model = alexnet2(WIDTH, HEIGHT, LR, output=input_output.NUM_OUTPUT_DIMENSIONS)
#model = alexnet(WIDTH, HEIGHT, LR, output=input_output.NUM_OUTPUT_DIMENSIONS)
#model = googlenet(WIDTH, HEIGHT, 1, LR, output=input_output.NUM_OUTPUT_DIMENSIONS, model_name=MODEL_NAME)

if not START_FRESH:
    print("Loading existing model")
    model.load(EXISTING_MODEL_NAME)

START_TIME = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

train_data = np.load('training-data-balanced.npy')

for i in range(EPOCHS):
    #data_order = [i for i in range(START_NUMBER,END_NUMBER+1)]
    #shuffle(data_order)
    #for count,i in enumerate(data_order):
    #    train_data = np.load('training_data-{}.npy'.format(i))
        
        #df = pd.DataFrame(train_data)
        #df = df.iloc[np.random.permutation(len(df))]
        #train_data = df.values.tolist()

        train = train_data[:-500]
        test = train_data[-500:]

        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

        model.save(MODEL_NAME)

END_TIME = datetime.now().strftime("%d.%m.%Y %H.%M.%S")
print("START TIME: %s" % START_TIME)
print("END TIME: %s" % END_TIME)

# tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming-phase5/log