"""Takes series of notes from markov chain and plays it"""

import atexit
import os
from random import choice

from psonic import *

# The sample directory is relative to this source file's directory.
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "samples")

SAMPLE_FILE = os.path.join(SAMPLES_DIR, "bass_G2.wav")
SAMPLE_NOTE = D2  # the sample file plays at this pitch


def play_note(note, beats=1, bpm=300, amp=100):
    """Plays note for `beats` beats. Returns when done."""
    # `note` is this many half-steps higher than the sampled note
    half_steps = note - SAMPLE_NOTE
    # An octave higher is twice the frequency. There are twelve half-steps per octave. Ergo,
    # each half step is a twelth root of 2 (in equal temperament).
    rate = (2 ** (1 / 12)) ** half_steps
    assert os.path.exists(SAMPLE_FILE)
    # Turn sample into an absolute path, since Sonic Pi is executing from a different working directory.
    sample(os.path.realpath(SAMPLE_FILE), rate=rate, amp=amp)
    sleep(beats * 60 / bpm) #sleep(0.5) #


def stop():
    """Stops all tracks."""
    msg = osc_message_builder.OscMessageBuilder(address='/stop-all-jobs')
    msg.add_arg('SONIC_PI_PYTHON')
    msg = msg.build()
    synthServer.client.send(msg)


atexit.register(stop)  # stop all tracks when the program exits normally or is interrupted
beats_per_minute = 45

# curr_note = 60
major_intro = [2,2,1,2,2,2,1]
minor_intro = [-1 -1 -1 -1 -1 -2 -2]
def play_music(curr_note=60, interval=[2,2,1,2,2,2,1]):
    beats = 1
    bpm = 300
    amp = 100
    play_note(curr_note, beats, bpm, amp)
    for note in interval:
        curr_note += note
        print('note: ', note)
        if 0 <= curr_note:
            play_note(curr_note, beats, bpm, amp)
        else:
            curr_note = 0
            play_note(curr_note, beats, bpm, amp)

if __name__ == "__main__":
    play_music()
