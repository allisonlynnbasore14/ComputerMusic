"""Main File for Music Generation
Purpose: Create computer-generated music
Authors: Tatiana Anthony, Allison Basore, Ilya Besancon,
Hannah Kolano, Meaghen Sausville"""
# from tkinter import *
# from tkinter import messagebox
# from tkinter import font
import mido
from musicreader import play_music
import random

class Note:
    def __init__(self, tone = 60, volume = 60, duration = 0):
        self.tone = tone
        self.duration = duration
        self.volume = volume

class Song:
    def __init__(self, notes_list):
        """creates a song object from a list of notes"""
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)

    def add_to_analysis(self, an_dict, pre_len=1):
        """hey Song, add yourself to the markov dictionary"""
        intervals = self.intervals
        for i in range(len(intervals) - pre_len):
            prefix = tuple(intervals[i:i + pre_len])
            suffix = intervals[i + pre_len]
            an_dict[prefix] = an_dict.get(prefix, tuple()) + (suffix,)


def read_midi(filename):
    mid = mido.MidiFile(filename)
    # print(mid)
    list_of_notes = []
    open_notes = []
    for i, track in enumerate(mid.tracks):
        # print('Track {}: {}'.format(i, track.name))
        # test_track = track[350]
        # print(track[350])
        for j in range(len(track)):
            msg = track[j]
            # print(msg)
            # print(msg.type)
            is_new_note = True
            may_be_note = False
            if msg.type == 'note_on' or msg.type == 'note_off':
                may_be_note = True
            for old_note in open_notes:
                # print(is_new_note)
                old_note.duration += msg.time
                if may_be_note:
                    if old_note.tone == msg.note:
                        is_new_note = False
                        if msg.type == 'note_on':
                            if msg.velocity == 0:
                                list_of_notes.append(old_note)
                                open_notes.remove(old_note)
                        elif msg.type == 'note_off':
                            list_of_notes.append(old_note)
                            open_notes.remove(old_note)

            if is_new_note and may_be_note:
                new_note = Note(msg.note, msg.velocity)
                open_notes.append(new_note);
            # try:
            #     nextmsg = track[j+1]
            #     # print(nextmsg.time)
            # except:
            #     pass
    return list_of_notes

def MIDI_clean(filename):
    """
    Cleans up the MIDI files
    input: MIDI file name
    output: MIDI information
    """
    pass

def MIDI_to_song(MIDI_info):
    """
    Gets the important information from the MIDI file
    input:  MIDI information from function, list of notes
    output: list of notes (and other impmortant parts to make the song?)
    """
    pass


def con_to_int(note_list):
    """takes a song object and returns a list of note intervals"""
    int_list = []
    for i in range(len(note_list)-1):
        int_list.append(note_list[i+1].tone - note_list[i].tone)
    return int_list


def harmony_analysis(notes):

	"""
	Completes a harmony, arrangement, sectioning analysis and give better sounding song
	input: list of notes
	output: new list of notes
	"""
	pass


def create_markov_chain(mark_dict, start_note=60, len_in_measures=32, pre_len=1):
    """takes a markov dicionary and returns a generated list of note intervals"""
    new_melody = list(random.choice(list(mark_dict.keys())))
    melody_concrete = [start_note]
    possible_notes = poss_notes(start_note, 'minor')
    for i in range(len(new_melody)):
        melody_concrete.append(melody_concrete[i]+new_melody[i])
    for i in range(len_in_measures - pre_len):
        options = mark_dict[tuple(new_melody[i:i+pre_len])]
        next_interval = random.choice(options)
        next_note = melody_concrete[i+pre_len] + next_interval
        while next_note not in possible_notes:
            next_interval = random.choice(options)
            next_note = melody_concrete[i+pre_len] + next_interval
        new_melody.append(next_interval)
        melody_concrete.append(next_note)
    return new_melody


def poss_notes(start_note, key_in='major'):
    '''takes a starting note; returns list of possible notes in major key of that note'''
    if key_in == 'major':
        intervals = [2, 2, 1, 2, 2, 2, 1]
    elif key_in == 'minor':
        intervals = [2, 1, 2, 2, 1, 2, 2]
    while start_note >= 36:
        start_note += -12
    possible_notes = [start_note]
    counter = 0
    for i in range(6):
        for interval in intervals:
            new_note = possible_notes[counter] + interval
            possible_notes.append(new_note)
            counter += 1
    return possible_notes


def play_song(song_intervals):
    """
    Plays the song
    input: list of notes/intervals
    output: *speaker output*
    """
    pass


def main(filename):
    if type(filename) == list:
        list_of_songs = filename
    else:
        list_of_songs = [filename]
        m_dict = dict()
    for song in list_of_songs:
    # cleaned = MIDI_clean(song)
    # new_song_con = MIDI_to_song(cleaned)
        new_song_con = read_midi(filename)
        NewSong = Song(new_song_con)
        NewSong.add_to_analysis(m_dict)
        new_intervals = create_markov_chain(m_dict, 57)
    # new_intervals = NewSong.intervals
    print(type(new_intervals))
    print(new_intervals)
    play_music(60,new_intervals)


if __name__ == "__main__":
   main('TwinkleTwinkleLittleStar.mid')
    # play_music()

