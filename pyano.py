import numpy as np
import simpleaudio as sa
from pynput.keyboard import Key, Listener, KeyCode
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

SOUND_H = 4

class FREQ():
    key_coverity = {'g':'C', 'y':'Cis', 'h':'D', 'u':'Dis', 'j':'E', 'k':'F', 'o':'Fis', 'l':'G', 'p':'Gis', ';':'A', '[':'B', '\'':'H'}

    C0 = 16.35
    Cis0 = 17.32
    D0 = 18.35
    Dis0 = 19.45
    E0 = 20.60
    F0 = 21.83
    Fis0 = 23.12
    G0 = 24.50
    Gis0 = 25.96
    A0 = 27.50
    B0 = 29.14
    H0 = 30.87
    C1 = 32.70
    Cis1 = 34.65
    D1 = 36.71
    Dis1 = 38.89
    E1 = 41.20
    F1 = 43.65
    Fis1 = 46.25
    G1 = 49.00
    Gis1 = 51.91
    A1 = 55.00
    B1 = 58.27
    H1 = 61.74
    C2 = 65.41
    Cis2 = 69.30
    D2 = 73.42
    Dis2 = 77.78
    E2 = 82.41
    F2 = 87.31
    Fis2 = 92.50
    G2 = 98.00
    Gis2 = 103.83
    A2 = 110.00
    B2 = 116.54
    H2 = 123.47
    C3 = 130.81
    Cis3 = 138.59
    D3 = 146.83
    Dis3 = 155.56
    E3 = 164.81
    F3 = 174.61
    Fis3 = 185.00
    G3 = 196.00
    Gis3 = 207.65
    A3 = 220.00
    B3 = 233.08
    H3 = 246.94
    C4 = 261.63
    Cis4 = 277.18
    D4 = 293.66
    Dis4 = 311.13
    E4 = 329.63
    F4 = 349.23
    Fis4 = 369.99
    G4 = 392.00
    Gis4 = 415.30
    A4 = 440.00
    B4 = 466.16
    H4 = 493.88
    C5 = 523.25
    Cis5 = 554.37
    D5 = 587.33
    Dis5 = 622.25
    E5 = 659.25
    F5 = 698.46
    Fis5 = 739.99
    G5 = 783.99
    Gis5 = 830.61
    A5 = 880.00
    B5 = 932.33
    H5 = 987.77
    C6 = 1046.50
    Cis6 = 1108.73
    D6 = 1174.66
    Dis6 = 1244.51
    E6 = 1318.51
    F6 = 1396.91
    Fis6 = 1479.98
    G6 = 1567.98
    Gis6 = 1661.22
    A6 = 1760.00
    B6 = 1864.66
    H6 = 1975.53
    C7 = 2093.00
    Cis7 = 2217.46
    D7 = 2349.32
    Dis7 = 2489.02
    E7 = 2637.02
    F7 = 2793.83
    Fis7 = 2959.96
    G7 = 3135.96
    Gis7 = 3322.44
    A7 = 3520.00
    B7 = 3729.31
    H7 = 3951.07
    C8 = 4186.01
    Cis8 = 4434.92
    D8 = 4698.63
    Dis8 = 4978.03
    E8 = 5274.04
    F8 = 5587.65
    Fis8 = 5919.91
    G8 = 6271.93
    Gis8 = 6644.88
    A8 = 7040.00
    B8 = 7458.62
    H8 = 7902.13

def play_note(freq):
    fs = 44100

    total_length = 10
    attack  = 1
    sustain = 1
    release = 1
    silence = total_length-(attack+sustain+release)

    t_r = np.linspace(0, total_length, total_length*fs, endpoint=False)
    n_r = freq*t_r*2*np.pi

    sound_calculation = np.concatenate((
        np.linspace(0, 1, int( (total_length*fs)*(attack /total_length) ), endpoint=True),
        np.linspace(1, 1, int( (total_length*fs)*(sustain/total_length) ), endpoint=True),
        np.linspace(1, 0, int( (total_length*fs)*(release/total_length) ), endpoint=True), 
        np.linspace(0, 0, int( (total_length*fs)*(silence/total_length) )) 
            ))

    note_total = np.sin(n_r) * sound_calculation
    audio_total = note_total * (2**15 - 1) / np.max(np.abs(note_total))
    audio_total = audio_total.astype(np.int16)

    sa.play_buffer(audio_total, 1, 2, fs)

def is_piano_key(key):
    if key == KeyCode.from_char('g') or \
    key == KeyCode.from_char('h') or \
    key == KeyCode.from_char('j') or \
    key == KeyCode.from_char('k') or \
    key == KeyCode.from_char('l') or \
    key == KeyCode.from_char(';') or \
    key == KeyCode.from_char('\'') or \
    key == KeyCode.from_char('y') or \
    key == KeyCode.from_char('u') or \
    key == KeyCode.from_char('o') or \
    key == KeyCode.from_char('p') or \
    key == KeyCode.from_char('['):
        return str(key)[1:-1]
    else:
        return False

def is_0to8_key(key):
    if key == KeyCode.from_char('0') or \
    key == KeyCode.from_char('1') or \
    key == KeyCode.from_char('2') or \
    key == KeyCode.from_char('3') or \
    key == KeyCode.from_char('4') or \
    key == KeyCode.from_char('5') or \
    key == KeyCode.from_char('6') or \
    key == KeyCode.from_char('7') or \
    key == KeyCode.from_char('8'):
        return str(key)[1:-1]
    else:
        return False

def on_press(key):
    global SOUND_H

    piano_key = is_piano_key(key)
    tone_h = is_0to8_key(key)

    if piano_key:
        exp_build = f'play_note(FREQ.{FREQ.key_coverity[piano_key]}{SOUND_H})'
        eval(exp_build)
    elif tone_h:
        SOUND_H = int(tone_h)
    else: 
        if key == Key.up and SOUND_H < 8:
            SOUND_H += 1
        elif key == Key.down and SOUND_H > 0:
            SOUND_H -= 1
                
def on_release(key):
    if key == Key.esc:
        return False

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text='Pyano v1').grid(column=0, row=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)

with Listener(on_press=on_press, on_release=on_release) as listener:
    root.mainloop()
    listener.join()














############## LABORATORY ####################

# fs = 44100
# freq = 440

# total_length = 10
# attack  = 0
# sustain = 0
# release = 0
# silence = total_length-(attack+sustain+release)

# t_r = np.linspace(0, total_length, total_length*fs, endpoint=False)
# n_r = freq*t_r*2*np.pi

# sound_calculation = np.concatenate((
#     np.linspace(0, 1, int( (total_length*fs)*(attack /total_length) ), endpoint=True),
#     np.linspace(1, 1, int( (total_length*fs)*(sustain/total_length) ), endpoint=True),
#     np.linspace(1, 0, int( (total_length*fs)*(release/total_length) ), endpoint=True), 
#     np.linspace(0, 0, int( (total_length*fs)*(silence/total_length) )) 
#         ))

# note_total = np.sin(n_r) * sound_calculation
# audio_total = note_total * (2**15 - 1) / np.max(np.abs(note_total))
# audio_total = audio_total.astype(np.int16)

# sa.play_buffer(audio_total, 1, 2, fs)

# plt.plot(audio_total)
# plt.show()