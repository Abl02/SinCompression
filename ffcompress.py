#! /bin/python3

"""
Functions :
  checkInput()
  play()
  showFFT()
  showWave()
  decompose()
  setFile()
"""

import os

from src.sinSound import SIN
from src.fileSound import FILE

import matplotlib.pyplot as plt

import pyaudio

p = pyaudio.PyAudio()

# GLOBAL
CURRENT_FILE = None
FILE_NOT_EXIST = "The file '{}' does not exist."
NO_FILE_ENTERED = "Enter a built-in sound or a filepath to a .wav file"
ACTION_NOT_SUPPORTED = "'{}' is not a supported action"


def checkInput(i, a):
    if i == "":
        if not CURRENT_FILE:
            print(NO_FILE_ENTERED)
            return 1
        else:
            checkInput(CURRENT_FILE, a)

    elif i == "sin":
        # for build-in sin function
        f = SIN()
        match a:
            case "S":
                f.play(p)
            case "P":
                f.plot(plt)
            case "F":
                f.plot(plt)
            case "D":
                print("Noting to do here")
            case _:
                print(ACTION_NOT_SUPPORTED.format(a))
                return 1

    else:
        # file
        if not CURRENT_FILE:
            if not os.path.isfile(i):
                print(FILE_NOT_EXIST.format(i))
                return 1
            else:
                f = FILE(i)
        else:
            f = CURRENT_FILE
        match a:
            case "S":
                f.play(p)
            case "P":
                f.plot(plt)
            case "F":
                f.plotFFT(plt)
            case "D":
                f.decompose(plt)
            case _:
                print(ACTION_NOT_SUPPORTED.format(a))


def play(i=""):
    """
    play a sound using PyAudio
    """
    checkInput(i, "S")


def showFFT(i=""):
    """
    Plot the given sound Fast Fourier Transfrom function
    """
    checkInput(i, "F")


def showWav(i=""):
    """
    Plot the wave of the given sound
    """
    checkInput(i, "P")


def decompose(i=""):
    """
    Plot the given sound's elemental sinusoidal fucntions with the
    help of the Fast Fourier Transform function
    """
    # TO DO - in FILE class
    checkInput(i, "D")


def setFile(i=""):
    """
    Set the current file
    """
    global CURRENT_FILE
    if not os.path.isfile(i):
        print(FILE_NOT_EXIST.format(i))
        CURRENT_FILE = None
        return 1
    else:
        CURRENT_FILE = FILE(i)


"""
Call from interactive file when exiting
"""


def exit():
    p.terminate()


DISPATCHER_P = {"showf": showFFT, "show": showWav, "dec": decompose}
DISPATCHER_N = {"play": play, "set": setFile}
