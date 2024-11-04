#! /bin/python3

"""
Functions :
  play()
  showFFT()
  showWave()
  decompose()
"""

import os

from src.sinSound import SIN
from src.fileSound import FILE

import matplotlib.pyplot as plt

import pyaudio

p = pyaudio.PyAudio()


def play(i=""):
    """
    play a sound using PyAudio
    """
    if i == "":
        print("Enter a built-in sound or a filepath to a .wav file")
    elif i == "sin":
        # for build-in sin function
        f = SIN()
        f.play(p)
    else:
        # file
        if not os.path.isfile(i):
            print(f"The file '{i}' does not exist.")
        else:
            f = FILE(i)
            f.play(p)


def showFFT(i=""):
    """
    Plot the given sound Fast Fourier Transfrom function
    """
    if i == "":
        print("Enter a built-in sound or a filepath to a .wav file")
    elif i == "sin":
        # for build-in sin function
        f = SIN()
        f.plot(plt)
    else:
        # for file
        if not os.path.isfile(i):
            print(f"The file '{i}' does not exist.")
        else:
            f = FILE(i)
            f.plotFFT(plt)


def showWav(i=""):
    """
    Plot the wave of the given sound
    """
    if i == "":
        print("Enter a built-in sound or a filepath to a .wav file")
    elif i == "sin":
        # for build-in sin function
        f = SIN()
        f.plot(plt)
    else:
        # for file
        if not os.path.isfile(i):
            print(f"The file '{i}' does not exist.")
        else:
            f = FILE(i)
            f.plot(plt)


def decompose(i=""):
    """
    Plot the given sound's elemental sinusoidal fucntions with the
    help of the Fast Fourier Transform function
    """
    # TO DO - in FILE class
    if i == "":
        print("Enter a built-in sound or a filepath to a .wav file")
    elif i == "sin":
        # for build-in sin function
        print("Noting to do here")
    else:
        # for file
        if not os.path.isfile(i):
            print(f"The file '{i}' does not exist.")
        else:
            f = FILE(i)
            f.decompose(plt)


"""
Call from interactive file when exiting
"""


def exit():
    p.terminate()


DISPATCHER_P = {"showf": showFFT, "show": showWav, "dec": decompose}
DISPATCHER_N = {"play": play}
