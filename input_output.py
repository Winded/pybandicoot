import cv2
import operator

NUM_INPUT_DIMENSIONS_X = 160
NUM_INPUT_DIMENSIONS_Y = 120
NUM_OUTPUT_DIMENSIONS = 27

def define_output_array(index):
    arr = [0] * NUM_OUTPUT_DIMENSIONS
    arr[index] = 1
    return arr

KEY_MAPPINGS = [
    # WASD
    ('W', define_output_array(0)),
    ('S', define_output_array(1)),
    ('A', define_output_array(2)),
    ('D', define_output_array(3)),

    # WASD combinations
    ('WA', define_output_array(4)),
    ('WD', define_output_array(5)),
    ('SA', define_output_array(6)),
    ('SD', define_output_array(7)),

    # Jump (space) & jump combinations
    ('\x20', define_output_array(8)),
    ('\x20W', define_output_array(9)),
    ('\x20S', define_output_array(10)),
    ('\x20A', define_output_array(11)),
    ('\x20D', define_output_array(12)),
    ('\x20WA', define_output_array(13)),
    ('\x20WD', define_output_array(14)),
    ('\x20SA', define_output_array(15)),
    ('\x20SD', define_output_array(16)),

    # Spin & spin combinations
    ('F', define_output_array(17)),
    ('FW', define_output_array(18)),
    ('FS', define_output_array(19)),
    ('FA', define_output_array(20)),
    ('FD', define_output_array(21)),
    ('FWA', define_output_array(22)),
    ('FWD', define_output_array(23)),
    ('FSA', define_output_array(24)),
    ('FSD', define_output_array(25)),

    # No keys pressed
    ('', define_output_array(26)),
]

SORTED_KEY_MAPPINGS = sorted(KEY_MAPPINGS, key=lambda km: len(km[0]), reverse=True)

def keys_to_output(keys):
    for km in SORTED_KEY_MAPPINGS:
        has_keys = True
        for ch in km[0]:
            if ch not in keys:
                has_keys = False
                break
        if has_keys:
            return km[1]

    # Should never reach here
    return None

def output_to_keys(output):
    index, value = max(enumerate(output), key=operator.itemgetter(1))

    if value < 0.5 or index >= len(KEY_MAPPINGS):
        return KEY_MAPPINGS[-1][0]

    return KEY_MAPPINGS[index][0]

def screencap_to_input(screen):
    # resize to something a bit more acceptable for a CNN
    screen = cv2.resize(screen, (NUM_INPUT_DIMENSIONS_X,NUM_INPUT_DIMENSIONS_Y))
    # convert to grayscale
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    return screen