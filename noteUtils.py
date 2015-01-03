__author__ = '7sDream'

import numpy as n
import winsound
import time
FS = 44100
dt = 1.0 / FS

LENGTHTABLE = [0.5, 0.25, 0.125]
LENGTHSUFFFIX = ['2', '4', '8']
FREQTABLE = [
    [62, 123, 247, 494, 988, 1976, 3951, 0],
    [58, 117, 233, 466, 932, 1865, 3729, 0],
    [55, 110, 220, 440, 880, 1760, 3520, 0],
    [52, 104, 208, 415, 831, 1661, 3322, 0],
    [49, 98, 196, 392, 784, 1568, 3136, 0],
    [46, 92, 185, 370, 740, 1480, 2960, 0],
    [44, 87, 175, 349, 698, 1397, 2794, 0],
    [41, 82, 165, 330, 659, 1319, 2637, 0],
    [39, 78, 156, 311, 622, 1245, 2489, 4978],
    [37, 73, 147, 294, 587, 1175, 2349, 4698],
    [35, 69, 139, 277, 554, 1109, 2217, 4434],
    [33, 65, 131, 262, 523, 1047, 2093, 4186]]
SCALETABLE = ['B', 'AB', 'A', 'GA', 'G', 'FG', 'F', 'E', 'DE', 'D', 'CD', 'C']


class Note():
    def __init__(self, note_name, note_freq, note_length, note_signal):
        self.name = note_name
        self.freq = note_freq
        self.length = note_length
        self._signal = note_signal

    def play(self):
        winsound.Beep(int(self.freq), int(self.length))


class NoteUtils():
    def __init__(self):
        self.notes = _init_notes()

    def pos_2_text_and_play(self, x, y, length):
        # Think as only have white key.
        table = [['', 'FG3', 'GA3', 'AB3', '', 'CD4', 'DE4', '', 'FG4', 'GA4',
                  'AB4', '', 'CD5', 'DE5', '', 'FG5', 'GA5', 'AB5', '', 'CD6',
                  'DE6', ''],
                 ['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4',
                  'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6',
                  'E6', 'F6']]
        row = 1
        col = int(x / 17)
        if y < 66:  # may be black key.
            for left in range(-6, 352, 17):
                right = left + 10
                if left > x:
                    break
                if left <= x <= right:
                    pre_col = int((left + 6) / 17)
                    r = pre_col % 7
                    if 1 != r != 5:
                        row = 0
                        col = pre_col
                    break
        # noinspection PyTypeChecker
        note_text = table[row][col] + LENGTHSUFFFIX[length]
        self.play_by_text(note_text)
        return note_text

    def play_by_text(self, note_text):
        try:
            length = LENGTHSUFFFIX.index(note_text[-1])
            if len(note_text) >= 3:
                scale_in_text = note_text[:-2]
                scale = SCALETABLE.index(scale_in_text)
                degree = int(note_text[-2])
                self.play_note_by_args(scale, degree, length)
            else:
                time.sleep(LENGTHTABLE[length])
        except (ValueError, IndexError) as e:
            print("the note text '" + note_text + "' is invalid")

    def play_note_by_args(self, scale, degree, length):
        self.notes[length][scale][degree].play()

    def get_empty_note_text_by_length(self, length):
        return '0' + LENGTHSUFFFIX[length]

    def play_note_texts(self, notetexts):
        notes = notetexts.split(',')
        for note in notes:
            self.play_by_text(note)


def _init_notes():
    mutes = []
    all_notes = []

    for (length, lengthSuffix) in zip(LENGTHTABLE, LENGTHSUFFFIX):

        mutes.append(n.zeros(int(length / dt)))

        x = n.arange(0, length, dt)
        mod = (x ** 4) * n.exp(x ** 0.5 * -30)
        mod = mod / max(mod)

        length_notes = []

        for (scales, scaleName) in zip(FREQTABLE, SCALETABLE):

            scale_notes = []

            for (freq, degreeName) in zip(scales, range(1, 9)):
                signal = mod * n.cos(x * 2 * n.pi * freq)
                signal /= max(signal)
                note = Note(scaleName + str(degreeName) + lengthSuffix,
                            freq, length * 1000, signal)
                scale_notes.append(note)

            length_notes.append(scale_notes)

        all_notes.append(length_notes)

    return all_notes
