#! /bin/python3

import os

from src.sinSound import SIN
from src.fileSound import FILE

import matplotlib.pyplot as plt

import pyaudio

p = pyaudio.PyAudio()


def play(i=""):
    if i == "":
        print("Enter a built-in sound or a filepath to a .wav file")
    elif i == "sin":
        # for build-in sin function
        f = SIN()
        f.play(p)
    else:
        if not os.path.isfile(i):
            print(f"The file '{i}' does not exist.")
        else:
            f = FILE(i)
            f.play(p)


def showfft(i=""):
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


DISPATCHER_P = {"showf": showfft, "show": showWav, "dec": decompose}
DISPATCHER_N = {"play": play}
