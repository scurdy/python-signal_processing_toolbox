#!/usr/bin/env python
'''
Created on Aug 25, 2015

@author: curdys
'''
import os, sys
import numpy as np
import matplotlib as mtl
from  scipy.io import wavfile
from numpy import int16
    
class OpenWaveFileException(Exception):
    pass

def GetFileName(path):
    _,name = os.path.split(path)
    return name

def GetFilePath(path):
    fpath,_= os.path.split(path)
    return fpath

def MakeFrame(x, frame_length, opt=None):
    nframe = np.floor_divide(len(x),frame_length)
    if opt =='padding':
        npad = len(x) - nframe*frame_length
        pad = x[len(x - npad):len(x)]

if __name__ == '__main__':
    PROJECT_DIR ='/Users/curdys/Documents/workspace/Signal Processing ToolBox'
    SOURCE_DIR = os.path.join(PROJECT_DIR, 'src')
    BIN_DIR = os.path.join(PROJECT_DIR, 'bin')
    AUDIO_DATA_DIR = os.path.join(BIN_DIR, 'audio')
    AUDIO_DATA_MAD_DIR = os.path.join(AUDIO_DATA_DIR, 'mad')
    SIGNAL_PROCESSING_MODULE_DIR = os.path.join(SOURCE_DIR, 'signal_processing')
    
    audio_file_path = os.path.join(AUDIO_DATA_MAD_DIR,'wav/01 raavarer.wav')
    
    if os.path.isfile(audio_file_path) is True:
        try:
            samplerate, buff = wavfile.read(audio_file_path)
        except IOError:
            raise OpenWaveFileException("Cannot Open :%s"%(GetFileName(audio_file_path)))

    frametime = 0.01 # 10ms
    frame_length = np.floor(frametime * samplerate)  
    xframe = MakeFrame(buff, frame_length)
    
    print("Well done !")