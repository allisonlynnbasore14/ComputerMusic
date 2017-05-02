"""Main File for Music Generation
Purpose: Create computer-generated music
Authors: Tatiana Anthony, Allison Basore, Ilya Besancon,
Hannah Kolano, Meaghen Sausville"""
# from tkinter import *
# from tkinter import messagebox
# from tkinter import font
import mido
from musicreader import play_music, Note
import random
import math


class Note:
    def __init__(self, tone=60, duration=1, volume=60):
        """initializes a note object"""
        self.tone = tone
        self.duration = duration
        self.volume = volume

class Song:
    def __init__(self, notes_list):
        """creates a song object from a list of notes"""
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)
        self.process_durations()

    def add_to_analysis(self, an_dict, duration_dict, pre_len=1):
        """hey Song, add yourself to the markov dictionary"""
        intervals = self.intervals
        for i in range(len(intervals) - pre_len):
            prefix = tuple(intervals[i:i + pre_len])
            suffix = intervals[i + pre_len]
            an_dict[prefix] = an_dict.get(prefix, tuple()) + (suffix,)
        durations = self.durations
        for i in range(len(durations)-pre_len):
            prefix = durations[i]
            suffix = durations[i+pre_len]
            duration_dict[prefix] = duration_dict.get(prefix, tuple()) + (suffix,)

    def process_durations(self):
        self.durations = []
        for note in self.concrete:
            self.durations.append(abs(note.duration))

def roundPartial (value, resolution):
    return math.ceil(value * resolution) / resolution

def check_metadata(single_track):
    num_chnl = {}
    maxItemCount = 0
    lyric_channel = -1
    bpm = 120
    tempo = 50000
    key = 'C'
    for j in range(len(single_track)-1):
        msg = single_track[j]
        nextmsg = single_track[j+1]
        if msg.type == 'lyrics' :
            if nextmsg.type == 'note_on':
                num_chnl[nextmsg.channel] =1+ num_chnl.get(nextmsg.channel, 0)
                if num_chnl[nextmsg.channel] > maxItemCount:
                    maxItemCount = num_chnl[nextmsg.channel]
                    lyric_channel = nextmsg.channel
        elif msg.type == 'set_tempo':
            tempo = msg.tempo
            bpm = mido.tempo2bpm(tempo)
        elif msg.type == 'key_signature':
            key = msg.key

    return lyric_channel, bpm, tempo, key


def key_to_start_note(key):
    list_of_keys = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    list_of_notes = [60,61,62,63,64,65,66,67,68,69,70,71]
    start_dict = dict(zip(list_of_keys,list_of_notes))

    start_note = start_dict.get(key,60)
    return start_note

def track_to_list(track,ticksinbeat,tempo,melody_channel):
    list_of_notes = []
    open_notes = []
    for j in range(len(track)):
        msg = track[j]
        # if msg.type in ['lyrics'] :
        #     print(msg)
        # print(msg.type)
        is_new_note = True
        may_be_note = False
        if msg.type == 'note_on' or msg.type == 'note_off':
            # print('found a note')
            # print(msg.channel)
            if msg.channel == melody_channel or melody_channel == -1:
                may_be_note = True
                # print(msg)
        for old_note in open_notes:
            # print(is_new_note)
            # print(msg.time/ticksinbeat)
            # print(ticksinbeat)
            added_length = msg.time/ticksinbeat
            # print(old_note.duration)
            old_note.duration += added_length
            # print(old_note.duration)
            # print(old_note.duration)
            if may_be_note:
                if old_note.tone == msg.note:
                    is_new_note = False
                    if (msg.type == 'note_on' and msg.velocity == 0) or msg.type == 'note_off':
                            old_note.duration = roundPartial(old_note.duration,8)
                            list_of_notes.append(old_note)
                            # print(old_note.duration)
                            # print(old_note.tone)
                            open_notes.remove(old_note)


        if is_new_note and may_be_note:
            new_note = Note(msg.note, 0, msg.velocity)
            open_notes.append(new_note);
    return list_of_notes

def read_midi(filename):
    mid = mido.MidiFile(filename)
    ticksperbeat=mid.ticks_per_beat
    print(ticksperbeat)
    # print(mid)

    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))

        melody_channel, bpm, tempo, key = check_metadata(track)
        list_of_notes = track_to_list(track,ticksperbeat,tempo,melody_channel)
        start_note = key_to_start_note(key)
        print(start_note)
    return list_of_notes, bpm, start_note


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
    """takes a list of note objects and returns a list of note intervals"""
    int_list = []
    for i in range(len(note_list)-1):
        int_list.append(note_list[i+1].tone - note_list[i].tone)
    return int_list


def bassline(startnote, song_length, riff='bass_random'):
    """
    input: startnote, length of each note, type of riff.
    Riff options: bass_random, pop_1, pop_2, pop_1_inv, pop_2_inv
    Generates:
    - randomely created bassline from scale
    - two algorythmic basslines, each with a variation
    All of these are returned as a list of note objects.
    """
    b_length = 4
    # in beats, 4 beats per measure
    # song_beats = 32
    song_measures = song_length  # song_beats // 4
    measure_per_riff = b_length
    riff_per_song = song_measures // b_length
    # bass_repeats = song_beats // ((b_length*4)//4)
    print(song_measures, 'measures per song,', b_length, 'measures per riff.')
    print('Riff repeats :', riff_per_song, 'times!')
    startnote = startnote - 12
    # list of possible notes
    use_scale = poss_notes(startnote, 'minor')
    # drops it down an octave
    octave_scale = [note - 12 for note in use_scale]
    # print('octaved scale: ', octave_scale)
    total_notes = len(octave_scale)
    
    # I V VI IV:
    riff_1 = [startnote, startnote + 7, startnote + 9, startnote + 5]
    riff_1_N = [Note(item, b_length) for item in riff_1]
    # same but lower instead of higher
    riff_inv_1 = [startnote, startnote - 5, startnote - 3, startnote - 7]
    riff_inv_1_N = [Note(thing, b_length) for thing in riff_inv_1]
    # I VI IV V:
    riff_2 = [startnote, startnote + 9, startnote + 5, startnote + 7]
    riff_2_N = [Note(stuff, b_length) for stuff in riff_2]
    # Same but lower
    riff_inv_2 = [startnote, startnote - 3, startnote - 7, startnote - 5]
    riff_inv_2_N = [Note(thing, b_length) for thing in riff_inv_2]
    # randomely picks notes from a bottom section of the scale
    bassline_notes = [Note(startnote, b_length)]
    for i in range(total_notes//b_length):
        bassline_notes.append(Note(
            random.choice(octave_scale[0:16]), b_length))
    
    if riff == 'pop_1':
        bassline_notes = riff_1_N * riff_per_song
    elif riff == 'pop_1_inv':
        bassline_notes = riff_inv_1_N * riff_per_song
    elif riff == 'pop_2':
        bassline_notes = riff_2_N * riff_per_song
    elif riff == 'pop_2_inv':
        bassline_notes = riff_inv_2_N * riff_per_song
    else: # using bass_random or some misspelling
        print('Using random bass line')

    bassline_notes.append(Note(startnote,2))
    bassline_notes.append(Note(startnote-12,2))
    return bassline_notes

def harmony_analysis(notes, startnote):
    """
    Sections and produces better sounding song
    input: list of notes
    output: new list of notes
    """
    pass



def create_markov_chain(mark_dict, dur_dict, start_note=60, len_in_measures=12, pre_len=1):

    """takes a markov dict; returns a markov'd list of note objects"""
    # initialize some variables
    possible_notes = poss_notes(start_note, 'major')
    new_intervals = [0]
    first_duration = abs(random.choice(list(dur_dict.keys())))
    new_durations = [first_duration]
    new_melody = [Note(start_note, new_durations[0])]
    num_beats = first_duration
    measure_counter = 0
    note_counter = 0
    n = 0
    # do this for as many beats as we want
    while measure_counter < len_in_measures:
        next_note = -1
        tone_options = mark_dict[new_intervals[n], ]
        print(new_durations)

        dur_options = dur_dict.get(new_durations[n],(0.25,))

        # tone is right when it's in the possible notes list
        while next_note not in possible_notes:
            if len(tone_options) ==0:
                next_interval = 0
            else:
                next_interval = random.choice(tone_options)
                tone_options = tuple(x for x in tone_options if x != next_interval)
            next_note = new_melody[n].tone + next_interval

        next_duration = random.choice(dur_options)

        # makes sure the next duration would finish a measure
        while num_beats + float(next_duration) > 4:
            counter = 0
            for duration in dur_options:
                if duration+num_beats < 4:
                    next_duration = random.choice(dur_options)
                else:
                    counter += 1
            if counter == len(dur_options):
                next_duration = 4 - num_beats

        # reset number of beats in current measure
        num_beats = float(num_beats) + float(next_duration)
        if num_beats == 4:
            num_beats = 0
            measure_counter += 1

        # append everything
        new_melody.append(Note(next_note, next_duration))
        new_intervals.append(next_interval)
        new_durations.append(next_duration)
        n += 1
    new_melody.append(Note(start_note,8))
    return new_melody


def poss_notes(start_note, key_in='major'):
    '''takes a starting note; returns list of possible notes in major or minor key of that note'''
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


def main(filename, user_picked_bassline='pop_1',rand_seed = random.random()):
    """
    Performs Markov analysis on many songs and
    input: takes an input of all file names
    output: plays a song
    """
    random.seed(rand_seed)
    print(rand_seed)
    print(user_picked_bassline, filename)
    if type(filename) == 'list':
        list_of_songs = filename
    else:
        list_of_songs = [filename]
        note_dict = dict()
        duration_dict = dict()
    for song in list_of_songs:
        # cleaned = MIDI_clean(song)
        # new_song_con = MIDI_to_song(cleaned)
        new_song_con, bpm, start_note = read_midi(filename)
        NewSong = Song(new_song_con)
        NewSong.add_to_analysis(note_dict, duration_dict)

        song_length =  12  # in measures!
        new_intervals = create_markov_chain(note_dict, duration_dict, start_note, song_length)

        """ To generate a bassline(start note, length of each note, riff type)
        use Riff options: bass_random, pop_1, pop_2, pop_1_inv, pop_2_inv
        """
        bassline_notes = bassline(start_note, song_length, user_picked_bassline)
        print(len(bassline_notes))
        # new_intervals = NewSong.intervals

        # print(type(new_intervals))
        # print(new_intervals)
    play_music(new_intervals, bassline_notes,bpm)
    print(bpm)
    print(rand_seed)


if __name__ == "__main__":

    #play_music()

    # mid = mido.MidiFile('UpAllNight.mid')
    # for i, track in enumerate(mid.tracks):
    #     print('Track {}: {}'.format(i, track.name))
    #     check_for_lyrics(track)

    # """ To generate a bassline(start note, length of each note, riff type)
    # use Riff options: bass_random, pop_1, pop_2, pop_1_inv, pop_2_inv
    # """
    # a = bassline(51, 2, 'pop_1')
    # print('Bassline ', a )

    # main('UpAllNight.mid', 'pop_1')
    # main('UpAllNight.mid', 'pop_2')
    main('UpAllNight.mid', 'pop_2_inv')
    # main('UpAllNight.mid', 'bass_random')

    #main('TwinkleTwinkleLittleStar.mid, WhatMakesYouBeautiful.mid')
    # play_music()
    #read_midi('UpAllNight.mid')


#The GUI draft (COMMENT OUT FOR NOW)
#fonts
#Times10 = (family="Times",size=10,weight="bold")

# top = Tk()
# top.geometry("400x400")

# #Function for Commands
# def printchoice(e):
# 	output = E.curselection()
# 	print(output)
