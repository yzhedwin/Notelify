import tkinter
from tkSnack import *

def setVolume(volume=50):
    """set the volume of the sound system"""
    if volume > 100:
        volume = 100
    elif volume < 0:
        volume = 0
    tkSnack.audio.play_gain(volume)


def playNote(freq, duration):
    """play a note of freq (hertz) for duration (seconds)"""
    snd = tkSnack.Sound()
    filt = tkSnack.Filter('generator', freq, 30000, 0.0, 'sine', int(11500 * duration))
    snd.stop()
    snd.play(filter=filt, blocking=1)


def soundStop():
    """stop the sound the hard way"""
    try:
        root = root.destroy()
        filt = None
    except:
        pass

if __name__ == '__main__':

    root = tkinter.Tk()

    # have to initialize the sound system, required!!
    tkSnack.initializeSnack(root)
    # set the volume of the sound system (0 to 100%)
    setVolume(30)
    # play a note of requency 440 hertz (A4) for a duration of 5 seconds
    playNote(440, 5)
    # play a note of requency 261.6 hertz (C4) for a duration of 5 seconds
    playNote(261.6, 5)
    # optional
    soundStop()

root.withdraw()