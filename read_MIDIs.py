import mido


class Note:
    def __init__(self, value=60, volume=60, duration=0):
        self.value = value
        self.duration = duration
        self.volume = volume


def read_midi(filename):
    mid = mido.MidiFile(filename)
    print(mid)
    list_of_notes = []
    open_notes = []
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        # test_track = track[350]
        #
        # print(track[350])
        for j in range(len(track)):
            msg = track[j]
            print(msg)
            # print(msg.type)
            is_new_note = True
            for old_note in open_notes:
                print(is_new_note)
                old_note.duration += msg.time
                if msg.type == 'note_on' or msg.type == 'note_off':
                    if old_note.value == msg.note:
                        is_new_note = False
                        if msg.type == 'note_on':
                            if msg.velocity == 0:
                                list_of_notes.append(old_note)
                                open_notes.remove(old_note)
                        elif msg.type == 'note_off':
                            list_of_notes.append(old_note)
                            open_notes.remove(old_note)

            if is_new_note:
                if len(old_notes) > 0:
                        new_note = Note(msg.note, msg.velocity)
                        open_notes.append(new_note)
            # try:
            #     nextmsg = track[j+1]
            #     # print(nextmsg.time)
            # except:
            #     pass
    return list_of_notes


if __name__ == "__main__":
    a = read_midi('Untitled_441406.mid')
    print(a)
