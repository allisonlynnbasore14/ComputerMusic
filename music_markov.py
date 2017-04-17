'''
music_markov.py

Purpose: takes a list of notes from the music analysis, do some markov
analysis, and return a list of notes to be played.

Author:Hannah Kolano
hannah.kolano@students.olin.edu

Next step: fix the markov function
'''


# All the imports
import random


# global variables
m_dict = dict()                 # markov dictionary
pre_len = 1                     # prefix length
# num_measures = 8                # number of desired measures, in 4/4, not implemented yet


# Important Classes
class Song:
    def __init__(self, notes_list):
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)

    def add_to_analysis(self):
        add_to_markov_dict(self.intervals)


class Note:
    def __init__(self, note, duration):
        self.tone = note
        self.duration = duration


# Functions
def con_to_int(note_list):
    """takes a song object and returns a list of note intervals"""
    int_list = [0]
    for i in range(len(note_list)-1):
        int_list.append(note_list[i+1].tone - note_list[i].tone)
    return int_list


def add_to_markov_dict(intervals):
    """takes a song object and creates a markov dictionary
    keys are PREFIX tuples
    values is a list of integers that are SUFFIXES"""
    for i in range(len(intervals)-pre_len):
        prefix = tuple(intervals[i:i+pre_len])
        suffix = intervals[i+pre_len]
        m_dict[prefix] = m_dict.get(prefix, tuple()) + (suffix,)


def create_markov_chain(mark_dict):
    """takes a markov dicionary and returns a generated list of note intervals"""
    new_melody = list(random.choice(list(mark_dict.keys())))
    for i in range(32 - pre_len):
        options = m_dict[tuple(new_melody[i:i+pre_len])]
        next_note = random.choice(options)
        new_melody.append(next_note)
    return new_melody

# options = prefixes_dict[tuple(prefix)]
#         next_word = random.choice(options)

# Initialize some songs
baa_baa_concrete = [Note(0, 1), Note(0, 1), Note(7, 1), Note(7, 1),                 # baa baa black sheep
                    Note(9, .5), Note(9, .5), Note(9, .5), Note(9, .5), Note(7, 2), # have you any wool
                    Note(5, 1), Note(5, 1), Note(4, 0), Note(4, 0),                 # yes sir yes sir
                    Note(2, 1), Note(2, 1), Note(0, 2),                             # three bags full
                    Note(7, 1), Note(7, 0.5), Note(7, 0.5), Note(5, 1), Note(5, 1), # one for the doctor
                    Note(4, 1), Note(4, 0.5), Note(4, 0.5), Note(2, 2),             # one for the dame
                    Note(7, 1), Note(7, 0.5), Note(7, 0.5),                         # one for the
                    Note(5, .5), Note(5, .5), Note(5, .5), Note(5, .5),             # little boy who
                    Note(4, 1), Note(4, 0.5), Note(4, 0.5), Note(2, 2),             # lives down the lane
                    Note(0, 1), Note(0, 1), Note(7, 1), Note(7, 1),                 # baa baa black sheep
                    Note(9, .5), Note(9, .5), Note(9, .5), Note(9, .5), Note(7, 2), # have you any wool
                    Note(5, 1), Note(5, 1), Note(4, 0), Note(4, 0),                 # yes sir yes sir
                    Note(2, 1), Note(2, 1), Note(0, 2)]                             # three bags full
BaaBaa = Song(baa_baa_concrete)
hot_cross_concrete = [Note(4, 1), Note(2, 1), Note(0, 2),                   # hot cross buns
                      Note(4, 1), Note(2, 1), Note(0, 2),                   # hot cross buns
                      Note(0, .5), Note(0, .5), Note(0, .5), Note(0, .5),   # one a penny
                      Note(2, .5), Note(2, .5), Note(2, .5), Note(2, .5),   # two a penny
                      Note(4, 1), Note(2, 1), Note(0, 2)]                   # hot cross buns
HotCross = Song(baa_baa_concrete)
mary_had_concrete = [Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # Mary had a
                     Note(4, 1), Note(4, 1), Note(4, 2),                # Little lamb
                     Note(2, 1), Note(2, 1), Note(2, 2),                # little lamb
                     Note(4, 1), Note(7, 1), Note(7, 2),                # little lamb
                     Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # Mary had a
                     Note(4, 1), Note(4, 1), Note(4, 1), Note(4, 1),    # little lamb whose
                     Note(2, 1), Note(2, 1), Note(4, 1), Note(2, 1),    # fleece was white as
                     Note(0, 4),                                        # snow
                     Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # every where that
                     Note(4, 1), Note(4, 1), Note(4, 2),                # mary went
                     Note(2, 1), Note(2, 1), Note(2, 2),                # mary went
                     Note(4, 1), Note(7, 1), Note(7, 2),                # mary went
                     Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # every where that
                     Note(4, 1), Note(4, 1), Note(4, 1), Note(4, 1),    # mary went that
                     Note(2, 1), Note(2, 1), Note(4, 1), Note(2, 1),    # lamb was sure to
                     Note(0, 4)]                                        # go
MaryHad = Song(mary_had_concrete)
this_old_concrete = [Note(7, 1), Note(4, 1), Note(7, 2),                # this old man
                     Note(7, 1), Note(4, 1), Note(7, 2),                # he played one
                     Note(9, 1), Note(7, 1), Note(5, 1), Note(4, 1),    # he played knick-knack
                     Note(2, 1), Note(4, 1), Note(5, 1),                # on my thumb
                     Note(4, .5), Note(5, .5), Note(7, 1), Note(0, 1),  # with a nick nack
                     Note(0, .5), Note(0, .5), Note(0, 1),              # paddy whack
                     Note(0, .5), Note(2, .5), Note(4, .5), Note(5, .5), Note(7, 2), # give the dog a bone
                     Note(7, 1), Note(2, 1), Note(2, 1), Note(5, 1),    # this old man came
                     Note(4, 1), Note(2, 1), Note(0, 2)]                # rolling home
ThisOld = Song(this_old_concrete)


# Actually run stuff
ThisOld.add_to_analysis()
MaryHad.add_to_analysis()
BaaBaa.add_to_analysis()
HotCross.add_to_analysis()

chain = create_markov_chain(m_dict)
print(chain)
