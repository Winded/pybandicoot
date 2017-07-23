# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import input_output

FILENAME = 'training_data-{}.npy'
files = []
for i in range(1, 11):
    f = FILENAME.format(i)
    files.append(f)

train_data = None
for f in files:
    arr = np.load(f)
    if train_data != None:
        train_data = np.concatenate((train_data, arr), axis=0)
    else:
        train_data = arr

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

choices = []
for i in range(input_output.NUM_OUTPUT_DIMENSIONS):
    choices.append([])

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    for idx, key in enumerate(input_output.KEY_MAPPINGS):
        if choice == key[1]:
            choices[idx].append([img, choice])
            break

#avg = 0
#for idx, ch in enumerate(choices):
#    avg = avg + len(ch)
#    print("%i: %i" % (idx, len(ch)))
#avg = avg / input_output.NUM_OUTPUT_DIMENSIONS
#print("avg = %i" % avg)

choices[0] = choices[0][:1300]
choices[26] = choices[26][:750]

#choices = list(map(lambda k: k[:int(avg)], choices))
for idx, ch in enumerate(choices):
    print("%i: %i" % (idx, len(ch)))

final_data = []
for ch in choices:
    final_data += ch
shuffle(final_data)

np.save("training-data-balanced.npy", final_data)




