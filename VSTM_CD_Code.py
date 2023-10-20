#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Sat Feb 20 12:12:02 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'THESIS'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/leahhurwitz/Desktop/FINAL THESIS/THESIS.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1900, 1200], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruc_5"
instruc_5Clock = core.Clock()
instruc = visual.TextStim(win=win, name='instruc',
    text='Hello, you are about to participate in a visual experiment. \n\nYou will see an array of colored shapes followed by a short interval, and then another array of shapes. Your job is to report whether you saw a change between the first and second arrays.\n\nIf you detect a change, press “c”\nIf you don’t, press “n”\n\nPress spacebar to continue. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Mask3_NC"
Mask3_NCClock = core.Clock()
fix_MNC3 = visual.ShapeStim(
    win=win, name='fix_MNC3', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
star_MNC3 = visual.ShapeStim(
    win=win, name='star_MNC3', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
tri_MNC3 = visual.ShapeStim(
    win=win, name='tri_MNC3',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
circ_MNC3 = visual.Polygon(
    win=win, name='circ_MNC3',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
starnoise3 = visual.NoiseStim(
    win=win, name='starnoise3',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-6.0)
starnoise3.buildNoise()
trinoise_MNC3 = visual.NoiseStim(
    win=win, name='trinoise_MNC3',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-7.0)
trinoise_MNC3.buildNoise()
circnoise_MNC3 = visual.NoiseStim(
    win=win, name='circnoise_MNC3',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
circnoise_MNC3.buildNoise()
star2 = visual.ShapeStim(
    win=win, name='star2', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
tri2 = visual.ShapeStim(
    win=win, name='tri2',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
circ2 = visual.Polygon(
    win=win, name='circ2',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
text_2 = visual.TextStim(win=win, name='text_2',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "Mask5_NC"
Mask5_NCClock = core.Clock()
fix5 = visual.ShapeStim(
    win=win, name='fix5', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
tri1 = visual.ShapeStim(
    win=win, name='tri1',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
rect1 = visual.Rect(
    win=win, name='rect1',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
star1 = visual.ShapeStim(
    win=win, name='star1', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
circ1 = visual.Polygon(
    win=win, name='circ1',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
oct1 = visual.Polygon(
    win=win, name='oct1',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
trinoise = visual.NoiseStim(
    win=win, name='trinoise',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
trinoise.buildNoise()
rectnoise = visual.NoiseStim(
    win=win, name='rectnoise',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-9.0)
rectnoise.buildNoise()
starnoise = visual.NoiseStim(
    win=win, name='starnoise',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
starnoise.buildNoise()
circnoise = visual.NoiseStim(
    win=win, name='circnoise',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-11.0)
circnoise.buildNoise()
octnoise = visual.NoiseStim(
    win=win, name='octnoise',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-12.0)
octnoise.buildNoise()
tri_5 = visual.ShapeStim(
    win=win, name='tri_5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
rect_5 = visual.Rect(
    win=win, name='rect_5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
star_5 = visual.ShapeStim(
    win=win, name='star_5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
circ_5 = visual.Polygon(
    win=win, name='circ_5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
oct_5 = visual.Polygon(
    win=win, name='oct_5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
text_11 = visual.TextStim(win=win, name='text_11',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "MaskSq_3"
MaskSq_3Clock = core.Clock()
fix_MS3 = visual.ShapeStim(
    win=win, name='fix_MS3', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Rect_MS3 = visual.Rect(
    win=win, name='Rect_MS3',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
Star_MS3 = visual.ShapeStim(
    win=win, name='Star_MS3', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
circ_MS3 = visual.Polygon(
    win=win, name='circ_MS3',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
noise_s = visual.NoiseStim(
    win=win, name='noise_s',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-6.0)
noise_s.buildNoise()
noise_t = visual.NoiseStim(
    win=win, name='noise_t',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-7.0)
noise_t.buildNoise()
noise_c = visual.NoiseStim(
    win=win, name='noise_c',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_c.buildNoise()
newRect_MS3 = visual.Rect(
    win=win, name='newRect_MS3',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
newStar_MS3 = visual.ShapeStim(
    win=win, name='newStar_MS3', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
newCirc_MS3 = visual.Polygon(
    win=win, name='newCirc_MS3',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
key_resp_11 = keyboard.Keyboard()
text_10 = visual.TextStim(win=win, name='text_10',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "MaskTri_3"
MaskTri_3Clock = core.Clock()
fixation_MT3 = visual.ShapeStim(
    win=win, name='fixation_MT3', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
rect1_MTC = visual.Rect(
    win=win, name='rect1_MTC',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
tri1_MTC = visual.ShapeStim(
    win=win, name='tri1_MTC',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
Oct1_MTC = visual.Polygon(
    win=win, name='Oct1_MTC',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
noise_rect_MTC = visual.NoiseStim(
    win=win, name='noise_rect_MTC',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-6.0)
noise_rect_MTC.buildNoise()
noise_tri_MTC = visual.NoiseStim(
    win=win, name='noise_tri_MTC',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-7.0)
noise_tri_MTC.buildNoise()
noise_circ_MTC = visual.NoiseStim(
    win=win, name='noise_circ_MTC',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_circ_MTC.buildNoise()
newRect_MTC = visual.Rect(
    win=win, name='newRect_MTC',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
newTri_MTC = visual.ShapeStim(
    win=win, name='newTri_MTC',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
newOct_MTC = visual.Polygon(
    win=win, name='newOct_MTC',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
text_4 = visual.TextStim(win=win, name='text_4',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "MaskCirc_3"
MaskCirc_3Clock = core.Clock()
fixation_MCC = visual.ShapeStim(
    win=win, name='fixation_MCC', vertices='cross',units='deg', 
    size=(1.5, 1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
circ_MCC = visual.Polygon(
    win=win, name='circ_MCC',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
rect_MCC = visual.Rect(
    win=win, name='rect_MCC',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
tri_MCC = visual.ShapeStim(
    win=win, name='tri_MCC',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
noise_circMCC = visual.NoiseStim(
    win=win, name='noise_circMCC',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-6.0)
noise_circMCC.buildNoise()
noise_rectMCC = visual.NoiseStim(
    win=win, name='noise_rectMCC',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-7.0)
noise_rectMCC.buildNoise()
noise_triMCC = visual.NoiseStim(
    win=win, name='noise_triMCC',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_triMCC.buildNoise()
newCirc_MCC = visual.Polygon(
    win=win, name='newCirc_MCC',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
newRect_MCC = visual.Rect(
    win=win, name='newRect_MCC',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
newTri_MCC = visual.ShapeStim(
    win=win, name='newTri_MCC',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
text_5 = visual.TextStim(win=win, name='text_5',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "MaskStar_5"
MaskStar_5Clock = core.Clock()
fix = visual.ShapeStim(
    win=win, name='fix', vertices='cross',units='deg', 
    size=(1.5, 1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Rect = visual.Rect(
    win=win, name='Rect',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=0.5, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.5, depth=-3.0, interpolate=True)
Tri = visual.ShapeStim(
    win=win, name='Tri',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=0.5, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.5, depth=-4.0, interpolate=True)
Circ = visual.Polygon(
    win=win, name='Circ',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=0.5, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.5, depth=-5.0, interpolate=True)
Oct = visual.Polygon(
    win=win, name='Oct',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=0.5, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.5, depth=-6.0, interpolate=True)
Star = visual.ShapeStim(
    win=win, name='Star', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=0.5, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.5, depth=-7.0, interpolate=True)
noise_Star_MSt5 = visual.NoiseStim(
    win=win, name='noise_Star_MSt5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_Star_MSt5.buildNoise()
noise_Rect_MSt5 = visual.NoiseStim(
    win=win, name='noise_Rect_MSt5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-9.0)
noise_Rect_MSt5.buildNoise()
noise_Tri_MSt5 = visual.NoiseStim(
    win=win, name='noise_Tri_MSt5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
noise_Tri_MSt5.buildNoise()
noise_Circ_MSt5 = visual.NoiseStim(
    win=win, name='noise_Circ_MSt5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-11.0)
noise_Circ_MSt5.buildNoise()
noise_Oct_MSt5 = visual.NoiseStim(
    win=win, name='noise_Oct_MSt5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-12.0)
noise_Oct_MSt5.buildNoise()
newRect = visual.Rect(
    win=win, name='newRect',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
newTri = visual.ShapeStim(
    win=win, name='newTri',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
newCirc = visual.Polygon(
    win=win, name='newCirc',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
newOct = visual.Polygon(
    win=win, name='newOct',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
newStar_CHNG = visual.ShapeStim(
    win=win, name='newStar_CHNG', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
cdInstruc = visual.TextStim(win=win, name='cdInstruc',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "MaskSq_5"
MaskSq_5Clock = core.Clock()
fixation_MSq5 = visual.ShapeStim(
    win=win, name='fixation_MSq5', vertices='cross',units='deg', 
    size=(1.5, 1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Tri_MSq5 = visual.ShapeStim(
    win=win, name='Tri_MSq5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
circ_MSq5 = visual.Polygon(
    win=win, name='circ_MSq5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
oct_MSq5 = visual.Polygon(
    win=win, name='oct_MSq5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
star_MSq5 = visual.ShapeStim(
    win=win, name='star_MSq5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
square_MSq5 = visual.Rect(
    win=win, name='square_MSq5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
noise_triMSq5 = visual.NoiseStim(
    win=win, name='noise_triMSq5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_triMSq5.buildNoise()
noise_CircMSq5 = visual.NoiseStim(
    win=win, name='noise_CircMSq5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-9.0)
noise_CircMSq5.buildNoise()
noise_OctMsq5 = visual.NoiseStim(
    win=win, name='noise_OctMsq5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
noise_OctMsq5.buildNoise()
noise_starMSq5 = visual.NoiseStim(
    win=win, name='noise_starMSq5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-11.0)
noise_starMSq5.buildNoise()
noise_RectMSq5 = visual.NoiseStim(
    win=win, name='noise_RectMSq5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-12.0)
noise_RectMSq5.buildNoise()
newTri_MSq5 = visual.ShapeStim(
    win=win, name='newTri_MSq5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
newCirc_MSq5 = visual.Polygon(
    win=win, name='newCirc_MSq5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
NewOct_MSq5 = visual.Polygon(
    win=win, name='NewOct_MSq5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
newStar_MSq5 = visual.ShapeStim(
    win=win, name='newStar_MSq5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
newRect_MSq5 = visual.Rect(
    win=win, name='newRect_MSq5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
text_6 = visual.TextStim(win=win, name='text_6',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "MaskCirc_5"
MaskCirc_5Clock = core.Clock()
fixation_MSC5 = visual.ShapeStim(
    win=win, name='fixation_MSC5', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Tri_MSC5 = visual.ShapeStim(
    win=win, name='Tri_MSC5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
Oct_MSC5 = visual.Polygon(
    win=win, name='Oct_MSC5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
Star_MSC5 = visual.ShapeStim(
    win=win, name='Star_MSC5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
Rect_MSC5 = visual.Rect(
    win=win, name='Rect_MSC5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Circ_MSC5 = visual.Polygon(
    win=win, name='Circ_MSC5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
noise_TriMSC5 = visual.NoiseStim(
    win=win, name='noise_TriMSC5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_TriMSC5.buildNoise()
noise_OctMSC5 = visual.NoiseStim(
    win=win, name='noise_OctMSC5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-9.0)
noise_OctMSC5.buildNoise()
noise_StarMSC5 = visual.NoiseStim(
    win=win, name='noise_StarMSC5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
noise_StarMSC5.buildNoise()
noise_RectMSC5 = visual.NoiseStim(
    win=win, name='noise_RectMSC5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-11.0)
noise_RectMSC5.buildNoise()
noise_CircMSC5 = visual.NoiseStim(
    win=win, name='noise_CircMSC5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-12.0)
noise_CircMSC5.buildNoise()
newTri_MSC5 = visual.ShapeStim(
    win=win, name='newTri_MSC5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
newOct_MSC5 = visual.Polygon(
    win=win, name='newOct_MSC5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
newStar_MSC5 = visual.ShapeStim(
    win=win, name='newStar_MSC5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
newRect_MSC5 = visual.Rect(
    win=win, name='newRect_MSC5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
newCirc_CHANGE = visual.Polygon(
    win=win, name='newCirc_CHANGE',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
text_7 = visual.TextStim(win=win, name='text_7',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "MaskTri_5"
MaskTri_5Clock = core.Clock()
colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
shuffle(colors)

if colors[0] == colors[1]:
    shuffle(colors)
if colors[0] == colors[2]:
    shuffle(colors)
if colors[0] == colors[3]:
    shuffle(colors)
if colors[0] == colors[4]:
    shuffle(colors)
if colors[1] == colors[2]:
    shuffle(colors)
if colors[1] == colors[3]:
    shuffle(colors)
if colors[1] == colors[4]:
    shuffle(colors)
if colors[2] == colors[3]:
    shuffle(colors)
if colors[2] == colors[4]:
    shuffle(colors)
if colors[3] == colors[4]:
    shuffle(colors)
fixation_MT5 = visual.ShapeStim(
    win=win, name='fixation_MT5', vertices='cross',units='deg', 
    size=(1.5, 1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Oct_MT5 = visual.Polygon(
    win=win, name='Oct_MT5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
Star_MT5 = visual.ShapeStim(
    win=win, name='Star_MT5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
Rect_MT5 = visual.Rect(
    win=win, name='Rect_MT5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
Circ_MT5 = visual.Polygon(
    win=win, name='Circ_MT5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Tri_MT5 = visual.ShapeStim(
    win=win, name='Tri_MT5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
noise_Oct = visual.NoiseStim(
    win=win, name='noise_Oct',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_Oct.buildNoise()
noise_star = visual.NoiseStim(
    win=win, name='noise_star',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-9.0)
noise_star.buildNoise()
noise_Rect = visual.NoiseStim(
    win=win, name='noise_Rect',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
noise_Rect.buildNoise()
noise_Circ = visual.NoiseStim(
    win=win, name='noise_Circ',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-11.0)
noise_Circ.buildNoise()
noise_Tri = visual.NoiseStim(
    win=win, name='noise_Tri',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-12.0)
noise_Tri.buildNoise()
newOct_MT5 = visual.Polygon(
    win=win, name='newOct_MT5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
newStar_MT5 = visual.ShapeStim(
    win=win, name='newStar_MT5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
newRect_MT5 = visual.Rect(
    win=win, name='newRect_MT5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
newCirc_MT5 = visual.Polygon(
    win=win, name='newCirc_MT5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
newTri_CHANGE = visual.ShapeStim(
    win=win, name='newTri_CHANGE',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
key_resp_9 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "MaskOct_5"
MaskOct_5Clock = core.Clock()
fixation_MO5 = visual.ShapeStim(
    win=win, name='fixation_MO5', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
star_MO5 = visual.ShapeStim(
    win=win, name='star_MO5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
circ_MO5 = visual.Polygon(
    win=win, name='circ_MO5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
rect_MO5 = visual.Rect(
    win=win, name='rect_MO5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
tri_MO5 = visual.ShapeStim(
    win=win, name='tri_MO5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
oct_MO5 = visual.Polygon(
    win=win, name='oct_MO5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
noise_starMO5 = visual.NoiseStim(
    win=win, name='noise_starMO5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-8.0)
noise_starMO5.buildNoise()
noise_circMO5 = visual.NoiseStim(
    win=win, name='noise_circMO5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-9.0)
noise_circMO5.buildNoise()
noise_rectMO5 = visual.NoiseStim(
    win=win, name='noise_rectMO5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-10.0)
noise_rectMO5.buildNoise()
noise_triMO5 = visual.NoiseStim(
    win=win, name='noise_triMO5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-11.0)
noise_triMO5.buildNoise()
noise_octMO5 = visual.NoiseStim(
    win=win, name='noise_octMO5',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=[0,0], size=(1.6,1.7), sf=None,
    phase=0.0,
    color='white', colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=1024, filter=None,
    noiseType='Uniform', noiseElementSize=0.08, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-12.0)
noise_octMO5.buildNoise()
newStar_MO5 = visual.ShapeStim(
    win=win, name='newStar_MO5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
newCirc_MO5 = visual.Polygon(
    win=win, name='newCirc_MO5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
newRect_MO5 = visual.Rect(
    win=win, name='newRect_MO5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
newTri_MO5 = visual.ShapeStim(
    win=win, name='newTri_MO5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
newOct_CHANGE = visual.Polygon(
    win=win, name='newOct_CHANGE',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
text_9 = visual.TextStim(win=win, name='text_9',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "NoMask3"
NoMask3Clock = core.Clock()
fixation_noChng = visual.ShapeStim(
    win=win, name='fixation_noChng', vertices='cross',units='deg', 
    size=(1.5, 1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
rect_1 = visual.Rect(
    win=win, name='rect_1',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=0.5, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.5, depth=-3.0, interpolate=True)
tri_1 = visual.ShapeStim(
    win=win, name='tri_1',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
circ_1 = visual.Polygon(
    win=win, name='circ_1',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
rect_noChng = visual.Rect(
    win=win, name='rect_noChng',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
tri_noChng = visual.ShapeStim(
    win=win, name='tri_noChng',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
circ_noChng = visual.Polygon(
    win=win, name='circ_noChng',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "NoMask5"
NoMask5Clock = core.Clock()
fix_noChng5 = visual.ShapeStim(
    win=win, name='fix_noChng5', vertices='cross',units='deg', 
    size=(1.5,1.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
rect_NC5 = visual.Rect(
    win=win, name='rect_NC5',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
tri_NC5 = visual.ShapeStim(
    win=win, name='tri_NC5',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
circ_NC5 = visual.Polygon(
    win=win, name='circ_NC5',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
oct_NC5 = visual.Polygon(
    win=win, name='oct_NC5',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
star_NC5 = visual.ShapeStim(
    win=win, name='star_NC5', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
rect_NC = visual.Rect(
    win=win, name='rect_NC',units='deg', 
    width=(1.6,1.7)[0], height=(1.6,1.7)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
tri_NC = visual.ShapeStim(
    win=win, name='tri_NC',units='deg', 
    vertices=[[-(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [+(1.6,1.7)[0]/2.0,-(1.6,1.7)[1]/2.0], [0,(1.6,1.7)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
circ_NC = visual.Polygon(
    win=win, name='circ_NC',units='deg', 
    edges=128, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
oct_NC = visual.Polygon(
    win=win, name='oct_NC',units='deg', 
    edges=8, size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
star_NC = visual.ShapeStim(
    win=win, name='star_NC', vertices='star7',units='deg', 
    size=(1.6,1.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='press “c” if you observed a change \npress “n” if you did not observe a change',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruc_5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instruc_5Components = [instruc, key_resp]
for thisComponent in instruc_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruc_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruc_5"-------
while continueRoutine:
    # get current time
    t = instruc_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruc_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruc* updates
    if instruc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruc.frameNStart = frameN  # exact frame index
        instruc.tStart = t  # local t and not account for scr refresh
        instruc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruc, 'tStartRefresh')  # time at next scr refresh
        instruc.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc_5"-------
for thisComponent in instruc_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruc.started', instruc.tStartRefresh)
thisExp.addData('instruc.stopped', instruc.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruc_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
randomize = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialConditions.xlsx'),
    seed=None, name='randomize')
thisExp.addLoop(randomize)  # add the loop to the experiment
thisRandomize = randomize.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRandomize.rgb)
if thisRandomize != None:
    for paramName in thisRandomize:
        exec('{} = thisRandomize[paramName]'.format(paramName))

for thisRandomize in randomize:
    currentLoop = randomize
    # abbreviate parameter names if possible (e.g. rgb = thisRandomize.rgb)
    if thisRandomize != None:
        for paramName in thisRandomize:
            exec('{} = thisRandomize[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=NCT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Mask3_NC"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        shuffle(newPositions)
        
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[0]
        if newPositions[0] == positions[2]:
             newPositions[0] = positions[0]
        star_MNC3.setPos(positions[0])
        star_MNC3.setFillColor(colors[0])
        star_MNC3.setLineColor([1,1,1])
        tri_MNC3.setPos(positions[1])
        tri_MNC3.setFillColor(colors[1])
        tri_MNC3.setLineColor([1,1,1])
        circ_MNC3.setPos(positions[2])
        circ_MNC3.setFillColor(colors[2])
        circ_MNC3.setLineColor([1,1,1])
        starnoise3.setColor(colors[0], colorSpace='rgb')
        starnoise3.setPos(positions[0])
        trinoise_MNC3.setColor(colors[1], colorSpace='rgb')
        trinoise_MNC3.setPos(positions[1])
        circnoise_MNC3.setColor(colors[2], colorSpace='rgb')
        circnoise_MNC3.setPos(positions[2])
        star2.setPos(positions[0])
        star2.setFillColor(colors[0])
        star2.setLineColor([1,1,1])
        tri2.setPos(positions[1])
        tri2.setFillColor(colors[1])
        tri2.setLineColor([1,1,1])
        circ2.setPos(positions[2])
        circ2.setFillColor(colors[2])
        circ2.setLineColor([1,1,1])
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # keep track of which components have finished
        Mask3_NCComponents = [fix_MNC3, star_MNC3, tri_MNC3, circ_MNC3, starnoise3, trinoise_MNC3, circnoise_MNC3, star2, tri2, circ2, text_2, key_resp_12]
        for thisComponent in Mask3_NCComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Mask3_NCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Mask3_NC"-------
        while continueRoutine:
            # get current time
            t = Mask3_NCClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Mask3_NCClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_MNC3* updates
            if fix_MNC3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_MNC3.frameNStart = frameN  # exact frame index
                fix_MNC3.tStart = t  # local t and not account for scr refresh
                fix_MNC3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_MNC3, 'tStartRefresh')  # time at next scr refresh
                fix_MNC3.setAutoDraw(True)
            if fix_MNC3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_MNC3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_MNC3.tStop = t  # not accounting for scr refresh
                    fix_MNC3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_MNC3, 'tStopRefresh')  # time at next scr refresh
                    fix_MNC3.setAutoDraw(False)
            
            # *star_MNC3* updates
            if star_MNC3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                star_MNC3.frameNStart = frameN  # exact frame index
                star_MNC3.tStart = t  # local t and not account for scr refresh
                star_MNC3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_MNC3, 'tStartRefresh')  # time at next scr refresh
                star_MNC3.setAutoDraw(True)
            if star_MNC3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_MNC3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    star_MNC3.tStop = t  # not accounting for scr refresh
                    star_MNC3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_MNC3, 'tStopRefresh')  # time at next scr refresh
                    star_MNC3.setAutoDraw(False)
            
            # *tri_MNC3* updates
            if tri_MNC3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri_MNC3.frameNStart = frameN  # exact frame index
                tri_MNC3.tStart = t  # local t and not account for scr refresh
                tri_MNC3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_MNC3, 'tStartRefresh')  # time at next scr refresh
                tri_MNC3.setAutoDraw(True)
            if tri_MNC3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri_MNC3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri_MNC3.tStop = t  # not accounting for scr refresh
                    tri_MNC3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri_MNC3, 'tStopRefresh')  # time at next scr refresh
                    tri_MNC3.setAutoDraw(False)
            
            # *circ_MNC3* updates
            if circ_MNC3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_MNC3.frameNStart = frameN  # exact frame index
                circ_MNC3.tStart = t  # local t and not account for scr refresh
                circ_MNC3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_MNC3, 'tStartRefresh')  # time at next scr refresh
                circ_MNC3.setAutoDraw(True)
            if circ_MNC3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_MNC3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_MNC3.tStop = t  # not accounting for scr refresh
                    circ_MNC3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_MNC3, 'tStopRefresh')  # time at next scr refresh
                    circ_MNC3.setAutoDraw(False)
            
            # *starnoise3* updates
            if starnoise3.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                starnoise3.frameNStart = frameN  # exact frame index
                starnoise3.tStart = t  # local t and not account for scr refresh
                starnoise3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(starnoise3, 'tStartRefresh')  # time at next scr refresh
                starnoise3.setAutoDraw(True)
            if starnoise3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > starnoise3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    starnoise3.tStop = t  # not accounting for scr refresh
                    starnoise3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(starnoise3, 'tStopRefresh')  # time at next scr refresh
                    starnoise3.setAutoDraw(False)
            if starnoise3.status == STARTED:
                if starnoise3._needBuild:
                    starnoise3.buildNoise()
            
            # *trinoise_MNC3* updates
            if trinoise_MNC3.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                trinoise_MNC3.frameNStart = frameN  # exact frame index
                trinoise_MNC3.tStart = t  # local t and not account for scr refresh
                trinoise_MNC3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trinoise_MNC3, 'tStartRefresh')  # time at next scr refresh
                trinoise_MNC3.setAutoDraw(True)
            if trinoise_MNC3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trinoise_MNC3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    trinoise_MNC3.tStop = t  # not accounting for scr refresh
                    trinoise_MNC3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trinoise_MNC3, 'tStopRefresh')  # time at next scr refresh
                    trinoise_MNC3.setAutoDraw(False)
            if trinoise_MNC3.status == STARTED:
                if trinoise_MNC3._needBuild:
                    trinoise_MNC3.buildNoise()
            
            # *circnoise_MNC3* updates
            if circnoise_MNC3.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                circnoise_MNC3.frameNStart = frameN  # exact frame index
                circnoise_MNC3.tStart = t  # local t and not account for scr refresh
                circnoise_MNC3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circnoise_MNC3, 'tStartRefresh')  # time at next scr refresh
                circnoise_MNC3.setAutoDraw(True)
            if circnoise_MNC3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circnoise_MNC3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circnoise_MNC3.tStop = t  # not accounting for scr refresh
                    circnoise_MNC3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circnoise_MNC3, 'tStopRefresh')  # time at next scr refresh
                    circnoise_MNC3.setAutoDraw(False)
            if circnoise_MNC3.status == STARTED:
                if circnoise_MNC3._needBuild:
                    circnoise_MNC3.buildNoise()
            
            # *star2* updates
            if star2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                star2.frameNStart = frameN  # exact frame index
                star2.tStart = t  # local t and not account for scr refresh
                star2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star2, 'tStartRefresh')  # time at next scr refresh
                star2.setAutoDraw(True)
            
            # *tri2* updates
            if tri2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                tri2.frameNStart = frameN  # exact frame index
                tri2.tStart = t  # local t and not account for scr refresh
                tri2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri2, 'tStartRefresh')  # time at next scr refresh
                tri2.setAutoDraw(True)
            
            # *circ2* updates
            if circ2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                circ2.frameNStart = frameN  # exact frame index
                circ2.tStart = t  # local t and not account for scr refresh
                circ2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ2, 'tStartRefresh')  # time at next scr refresh
                circ2.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # *key_resp_12* updates
            waitOnFlip = False
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Mask3_NCComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Mask3_NC"-------
        for thisComponent in Mask3_NCComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('fix_MNC3.started', fix_MNC3.tStartRefresh)
        trials.addData('fix_MNC3.stopped', fix_MNC3.tStopRefresh)
        trials.addData('star_MNC3.started', star_MNC3.tStartRefresh)
        trials.addData('star_MNC3.stopped', star_MNC3.tStopRefresh)
        trials.addData('tri_MNC3.started', tri_MNC3.tStartRefresh)
        trials.addData('tri_MNC3.stopped', tri_MNC3.tStopRefresh)
        trials.addData('circ_MNC3.started', circ_MNC3.tStartRefresh)
        trials.addData('circ_MNC3.stopped', circ_MNC3.tStopRefresh)
        trials.addData('starnoise3.started', starnoise3.tStartRefresh)
        trials.addData('starnoise3.stopped', starnoise3.tStopRefresh)
        trials.addData('trinoise_MNC3.started', trinoise_MNC3.tStartRefresh)
        trials.addData('trinoise_MNC3.stopped', trinoise_MNC3.tStopRefresh)
        trials.addData('circnoise_MNC3.started', circnoise_MNC3.tStartRefresh)
        trials.addData('circnoise_MNC3.stopped', circnoise_MNC3.tStopRefresh)
        trials.addData('star2.started', star2.tStartRefresh)
        trials.addData('star2.stopped', star2.tStopRefresh)
        trials.addData('tri2.started', tri2.tStartRefresh)
        trials.addData('tri2.stopped', tri2.tStopRefresh)
        trials.addData('circ2.started', circ2.tStartRefresh)
        trials.addData('circ2.stopped', circ2.tStopRefresh)
        trials.addData('text_2.started', text_2.tStartRefresh)
        trials.addData('text_2.stopped', text_2.tStopRefresh)
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        trials.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            trials.addData('key_resp_12.rt', key_resp_12.rt)
        trials.addData('key_resp_12.started', key_resp_12.tStartRefresh)
        trials.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
        # the Routine "Mask3_NC" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed NCT repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=NCF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Mask5_NC"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[3]:
            shuffle(colors)
        if colors[0] == colors[4]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[1] == colors[3]:
            shuffle(colors)
        if colors[1] == colors[4]:
            shuffle(colors)
        if colors[2] == colors[3]:
            shuffle(colors)
        if colors[2] == colors[4]:
            shuffle(colors)
        if colors[3] == colors[4]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        
        tri1.setPos(positions[0])
        tri1.setFillColor(colors[0])
        tri1.setLineColor([1,1,1])
        rect1.setPos(positions[1])
        rect1.setFillColor(colors[1])
        rect1.setLineColor([1,1,1])
        star1.setPos(positions[2])
        star1.setFillColor(colors[2])
        star1.setLineColor([1,1,1])
        circ1.setPos(positions[3])
        circ1.setFillColor(colors[3])
        circ1.setLineColor([1,1,1])
        oct1.setPos(positions[4])
        oct1.setFillColor(colors[4])
        oct1.setLineColor([1,1,1])
        trinoise.setColor(colors[0], colorSpace='rgb')
        trinoise.setPos(positions[0])
        rectnoise.setColor(colors[1], colorSpace='rgb')
        rectnoise.setPos(positions[1])
        starnoise.setColor(colors[2], colorSpace='rgb')
        starnoise.setPos(positions[2])
        circnoise.setColor(colors[3], colorSpace='rgb')
        circnoise.setPos(positions[3])
        octnoise.setColor(colors[4], colorSpace='rgb')
        octnoise.setPos(positions[4])
        tri_5.setPos(positions[0])
        tri_5.setFillColor(colors[0])
        tri_5.setLineColor([1,1,1])
        rect_5.setPos(positions[1])
        rect_5.setFillColor(colors[1])
        rect_5.setLineColor([1,1,1])
        star_5.setPos(positions[2])
        star_5.setFillColor(colors[2])
        star_5.setLineColor([1,1,1])
        circ_5.setPos(positions[3])
        circ_5.setFillColor(colors[3])
        circ_5.setLineColor([1,1,1])
        oct_5.setPos(positions[4])
        oct_5.setFillColor(colors[4])
        oct_5.setLineColor([1,1,1])
        key_resp_13.keys = []
        key_resp_13.rt = []
        _key_resp_13_allKeys = []
        # keep track of which components have finished
        Mask5_NCComponents = [fix5, tri1, rect1, star1, circ1, oct1, trinoise, rectnoise, starnoise, circnoise, octnoise, tri_5, rect_5, star_5, circ_5, oct_5, text_11, key_resp_13]
        for thisComponent in Mask5_NCComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Mask5_NCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Mask5_NC"-------
        while continueRoutine:
            # get current time
            t = Mask5_NCClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Mask5_NCClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix5* updates
            if fix5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix5.frameNStart = frameN  # exact frame index
                fix5.tStart = t  # local t and not account for scr refresh
                fix5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix5, 'tStartRefresh')  # time at next scr refresh
                fix5.setAutoDraw(True)
            if fix5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix5.tStop = t  # not accounting for scr refresh
                    fix5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix5, 'tStopRefresh')  # time at next scr refresh
                    fix5.setAutoDraw(False)
            
            # *tri1* updates
            if tri1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri1.frameNStart = frameN  # exact frame index
                tri1.tStart = t  # local t and not account for scr refresh
                tri1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri1, 'tStartRefresh')  # time at next scr refresh
                tri1.setAutoDraw(True)
            if tri1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri1.tStop = t  # not accounting for scr refresh
                    tri1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri1, 'tStopRefresh')  # time at next scr refresh
                    tri1.setAutoDraw(False)
            
            # *rect1* updates
            if rect1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                rect1.frameNStart = frameN  # exact frame index
                rect1.tStart = t  # local t and not account for scr refresh
                rect1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect1, 'tStartRefresh')  # time at next scr refresh
                rect1.setAutoDraw(True)
            if rect1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rect1.tStop = t  # not accounting for scr refresh
                    rect1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rect1, 'tStopRefresh')  # time at next scr refresh
                    rect1.setAutoDraw(False)
            
            # *star1* updates
            if star1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                star1.frameNStart = frameN  # exact frame index
                star1.tStart = t  # local t and not account for scr refresh
                star1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star1, 'tStartRefresh')  # time at next scr refresh
                star1.setAutoDraw(True)
            if star1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    star1.tStop = t  # not accounting for scr refresh
                    star1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star1, 'tStopRefresh')  # time at next scr refresh
                    star1.setAutoDraw(False)
            
            # *circ1* updates
            if circ1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ1.frameNStart = frameN  # exact frame index
                circ1.tStart = t  # local t and not account for scr refresh
                circ1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ1, 'tStartRefresh')  # time at next scr refresh
                circ1.setAutoDraw(True)
            if circ1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ1.tStop = t  # not accounting for scr refresh
                    circ1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ1, 'tStopRefresh')  # time at next scr refresh
                    circ1.setAutoDraw(False)
            
            # *oct1* updates
            if oct1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                oct1.frameNStart = frameN  # exact frame index
                oct1.tStart = t  # local t and not account for scr refresh
                oct1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(oct1, 'tStartRefresh')  # time at next scr refresh
                oct1.setAutoDraw(True)
            if oct1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > oct1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    oct1.tStop = t  # not accounting for scr refresh
                    oct1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(oct1, 'tStopRefresh')  # time at next scr refresh
                    oct1.setAutoDraw(False)
            
            # *trinoise* updates
            if trinoise.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                trinoise.frameNStart = frameN  # exact frame index
                trinoise.tStart = t  # local t and not account for scr refresh
                trinoise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trinoise, 'tStartRefresh')  # time at next scr refresh
                trinoise.setAutoDraw(True)
            if trinoise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trinoise.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    trinoise.tStop = t  # not accounting for scr refresh
                    trinoise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trinoise, 'tStopRefresh')  # time at next scr refresh
                    trinoise.setAutoDraw(False)
            if trinoise.status == STARTED:
                if trinoise._needBuild:
                    trinoise.buildNoise()
            
            # *rectnoise* updates
            if rectnoise.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                rectnoise.frameNStart = frameN  # exact frame index
                rectnoise.tStart = t  # local t and not account for scr refresh
                rectnoise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectnoise, 'tStartRefresh')  # time at next scr refresh
                rectnoise.setAutoDraw(True)
            if rectnoise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rectnoise.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rectnoise.tStop = t  # not accounting for scr refresh
                    rectnoise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rectnoise, 'tStopRefresh')  # time at next scr refresh
                    rectnoise.setAutoDraw(False)
            if rectnoise.status == STARTED:
                if rectnoise._needBuild:
                    rectnoise.buildNoise()
            
            # *starnoise* updates
            if starnoise.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                starnoise.frameNStart = frameN  # exact frame index
                starnoise.tStart = t  # local t and not account for scr refresh
                starnoise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(starnoise, 'tStartRefresh')  # time at next scr refresh
                starnoise.setAutoDraw(True)
            if starnoise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > starnoise.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    starnoise.tStop = t  # not accounting for scr refresh
                    starnoise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(starnoise, 'tStopRefresh')  # time at next scr refresh
                    starnoise.setAutoDraw(False)
            if starnoise.status == STARTED:
                if starnoise._needBuild:
                    starnoise.buildNoise()
            
            # *circnoise* updates
            if circnoise.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                circnoise.frameNStart = frameN  # exact frame index
                circnoise.tStart = t  # local t and not account for scr refresh
                circnoise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circnoise, 'tStartRefresh')  # time at next scr refresh
                circnoise.setAutoDraw(True)
            if circnoise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circnoise.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circnoise.tStop = t  # not accounting for scr refresh
                    circnoise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circnoise, 'tStopRefresh')  # time at next scr refresh
                    circnoise.setAutoDraw(False)
            if circnoise.status == STARTED:
                if circnoise._needBuild:
                    circnoise.buildNoise()
            
            # *octnoise* updates
            if octnoise.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                octnoise.frameNStart = frameN  # exact frame index
                octnoise.tStart = t  # local t and not account for scr refresh
                octnoise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(octnoise, 'tStartRefresh')  # time at next scr refresh
                octnoise.setAutoDraw(True)
            if octnoise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > octnoise.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    octnoise.tStop = t  # not accounting for scr refresh
                    octnoise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(octnoise, 'tStopRefresh')  # time at next scr refresh
                    octnoise.setAutoDraw(False)
            if octnoise.status == STARTED:
                if octnoise._needBuild:
                    octnoise.buildNoise()
            
            # *tri_5* updates
            if tri_5.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                tri_5.frameNStart = frameN  # exact frame index
                tri_5.tStart = t  # local t and not account for scr refresh
                tri_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_5, 'tStartRefresh')  # time at next scr refresh
                tri_5.setAutoDraw(True)
            
            # *rect_5* updates
            if rect_5.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                rect_5.frameNStart = frameN  # exact frame index
                rect_5.tStart = t  # local t and not account for scr refresh
                rect_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_5, 'tStartRefresh')  # time at next scr refresh
                rect_5.setAutoDraw(True)
            
            # *star_5* updates
            if star_5.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                star_5.frameNStart = frameN  # exact frame index
                star_5.tStart = t  # local t and not account for scr refresh
                star_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_5, 'tStartRefresh')  # time at next scr refresh
                star_5.setAutoDraw(True)
            
            # *circ_5* updates
            if circ_5.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                circ_5.frameNStart = frameN  # exact frame index
                circ_5.tStart = t  # local t and not account for scr refresh
                circ_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_5, 'tStartRefresh')  # time at next scr refresh
                circ_5.setAutoDraw(True)
            
            # *oct_5* updates
            if oct_5.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                oct_5.frameNStart = frameN  # exact frame index
                oct_5.tStart = t  # local t and not account for scr refresh
                oct_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(oct_5, 'tStartRefresh')  # time at next scr refresh
                oct_5.setAutoDraw(True)
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                text_11.setAutoDraw(True)
            
            # *key_resp_13* updates
            waitOnFlip = False
            if key_resp_13.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_13_allKeys.extend(theseKeys)
                if len(_key_resp_13_allKeys):
                    key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                    key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Mask5_NCComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Mask5_NC"-------
        for thisComponent in Mask5_NCComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('fix5.started', fix5.tStartRefresh)
        trials_2.addData('fix5.stopped', fix5.tStopRefresh)
        trials_2.addData('tri1.started', tri1.tStartRefresh)
        trials_2.addData('tri1.stopped', tri1.tStopRefresh)
        trials_2.addData('rect1.started', rect1.tStartRefresh)
        trials_2.addData('rect1.stopped', rect1.tStopRefresh)
        trials_2.addData('star1.started', star1.tStartRefresh)
        trials_2.addData('star1.stopped', star1.tStopRefresh)
        trials_2.addData('circ1.started', circ1.tStartRefresh)
        trials_2.addData('circ1.stopped', circ1.tStopRefresh)
        trials_2.addData('oct1.started', oct1.tStartRefresh)
        trials_2.addData('oct1.stopped', oct1.tStopRefresh)
        trials_2.addData('trinoise.started', trinoise.tStartRefresh)
        trials_2.addData('trinoise.stopped', trinoise.tStopRefresh)
        trials_2.addData('rectnoise.started', rectnoise.tStartRefresh)
        trials_2.addData('rectnoise.stopped', rectnoise.tStopRefresh)
        trials_2.addData('starnoise.started', starnoise.tStartRefresh)
        trials_2.addData('starnoise.stopped', starnoise.tStopRefresh)
        trials_2.addData('circnoise.started', circnoise.tStartRefresh)
        trials_2.addData('circnoise.stopped', circnoise.tStopRefresh)
        trials_2.addData('octnoise.started', octnoise.tStartRefresh)
        trials_2.addData('octnoise.stopped', octnoise.tStopRefresh)
        trials_2.addData('tri_5.started', tri_5.tStartRefresh)
        trials_2.addData('tri_5.stopped', tri_5.tStopRefresh)
        trials_2.addData('rect_5.started', rect_5.tStartRefresh)
        trials_2.addData('rect_5.stopped', rect_5.tStopRefresh)
        trials_2.addData('star_5.started', star_5.tStartRefresh)
        trials_2.addData('star_5.stopped', star_5.tStopRefresh)
        trials_2.addData('circ_5.started', circ_5.tStartRefresh)
        trials_2.addData('circ_5.stopped', circ_5.tStopRefresh)
        trials_2.addData('oct_5.started', oct_5.tStartRefresh)
        trials_2.addData('oct_5.stopped', oct_5.tStopRefresh)
        trials_2.addData('text_11.started', text_11.tStartRefresh)
        trials_2.addData('text_11.stopped', text_11.tStopRefresh)
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
        trials_2.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            trials_2.addData('key_resp_13.rt', key_resp_13.rt)
        trials_2.addData('key_resp_13.started', key_resp_13.tStartRefresh)
        trials_2.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
        # the Routine "Mask5_NC" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed NCF repeats of 'trials_2'
    
    
    # set up handler to look after randomisation of conditions etc
    SqLoopT = data.TrialHandler(nReps=MaskSqT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SqLoopT')
    thisExp.addLoop(SqLoopT)  # add the loop to the experiment
    thisSqLoopT = SqLoopT.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSqLoopT.rgb)
    if thisSqLoopT != None:
        for paramName in thisSqLoopT:
            exec('{} = thisSqLoopT[paramName]'.format(paramName))
    
    for thisSqLoopT in SqLoopT:
        currentLoop = SqLoopT
        # abbreviate parameter names if possible (e.g. rgb = thisSqLoopT.rgb)
        if thisSqLoopT != None:
            for paramName in thisSqLoopT:
                exec('{} = thisSqLoopT[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskSq_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        shuffle(newPositions)
        
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[0]
        if newPositions[0] == positions[2]:
             newPositions[0] = positions[0]
        Rect_MS3.setPos(positions[0])
        Rect_MS3.setFillColor(colors[0])
        Rect_MS3.setLineColor([1,1,1])
        Star_MS3.setPos(positions[1])
        Star_MS3.setFillColor(colors[1])
        Star_MS3.setLineColor([1,1,1])
        circ_MS3.setPos(positions[2])
        circ_MS3.setFillColor(colors[2])
        circ_MS3.setLineColor([1,1,1])
        noise_s.setColor(colors[0], colorSpace='rgb')
        noise_s.setPos(positions[0])
        noise_t.setColor(colors[1], colorSpace='rgb')
        noise_t.setPos(positions[1])
        noise_c.setColor(colors[2], colorSpace='rgb')
        noise_c.setPos(positions[2])
        newRect_MS3.setPos(newPositions[0])
        newRect_MS3.setFillColor(colors[0])
        newRect_MS3.setLineColor([1,1,1])
        newStar_MS3.setPos(positions[1])
        newStar_MS3.setFillColor(colors[1])
        newStar_MS3.setLineColor([1,1,1])
        newCirc_MS3.setPos(positions[2])
        newCirc_MS3.setFillColor(colors[2])
        newCirc_MS3.setLineColor([1,1,1])
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # keep track of which components have finished
        MaskSq_3Components = [fix_MS3, Rect_MS3, Star_MS3, circ_MS3, noise_s, noise_t, noise_c, newRect_MS3, newStar_MS3, newCirc_MS3, key_resp_11, text_10]
        for thisComponent in MaskSq_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskSq_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskSq_3"-------
        while continueRoutine:
            # get current time
            t = MaskSq_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskSq_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_MS3* updates
            if fix_MS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_MS3.frameNStart = frameN  # exact frame index
                fix_MS3.tStart = t  # local t and not account for scr refresh
                fix_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_MS3, 'tStartRefresh')  # time at next scr refresh
                fix_MS3.setAutoDraw(True)
            if fix_MS3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_MS3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_MS3.tStop = t  # not accounting for scr refresh
                    fix_MS3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_MS3, 'tStopRefresh')  # time at next scr refresh
                    fix_MS3.setAutoDraw(False)
            
            # *Rect_MS3* updates
            if Rect_MS3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Rect_MS3.frameNStart = frameN  # exact frame index
                Rect_MS3.tStart = t  # local t and not account for scr refresh
                Rect_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rect_MS3, 'tStartRefresh')  # time at next scr refresh
                Rect_MS3.setAutoDraw(True)
            if Rect_MS3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rect_MS3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Rect_MS3.tStop = t  # not accounting for scr refresh
                    Rect_MS3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Rect_MS3, 'tStopRefresh')  # time at next scr refresh
                    Rect_MS3.setAutoDraw(False)
            
            # *Star_MS3* updates
            if Star_MS3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Star_MS3.frameNStart = frameN  # exact frame index
                Star_MS3.tStart = t  # local t and not account for scr refresh
                Star_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Star_MS3, 'tStartRefresh')  # time at next scr refresh
                Star_MS3.setAutoDraw(True)
            if Star_MS3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Star_MS3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Star_MS3.tStop = t  # not accounting for scr refresh
                    Star_MS3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Star_MS3, 'tStopRefresh')  # time at next scr refresh
                    Star_MS3.setAutoDraw(False)
            
            # *circ_MS3* updates
            if circ_MS3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_MS3.frameNStart = frameN  # exact frame index
                circ_MS3.tStart = t  # local t and not account for scr refresh
                circ_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_MS3, 'tStartRefresh')  # time at next scr refresh
                circ_MS3.setAutoDraw(True)
            if circ_MS3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_MS3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_MS3.tStop = t  # not accounting for scr refresh
                    circ_MS3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_MS3, 'tStopRefresh')  # time at next scr refresh
                    circ_MS3.setAutoDraw(False)
            
            # *noise_s* updates
            if noise_s.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_s.frameNStart = frameN  # exact frame index
                noise_s.tStart = t  # local t and not account for scr refresh
                noise_s.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_s, 'tStartRefresh')  # time at next scr refresh
                noise_s.setAutoDraw(True)
            if noise_s.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_s.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_s.tStop = t  # not accounting for scr refresh
                    noise_s.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_s, 'tStopRefresh')  # time at next scr refresh
                    noise_s.setAutoDraw(False)
            if noise_s.status == STARTED:
                if noise_s._needBuild:
                    noise_s.buildNoise()
            
            # *noise_t* updates
            if noise_t.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_t.frameNStart = frameN  # exact frame index
                noise_t.tStart = t  # local t and not account for scr refresh
                noise_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_t, 'tStartRefresh')  # time at next scr refresh
                noise_t.setAutoDraw(True)
            if noise_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_t.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_t.tStop = t  # not accounting for scr refresh
                    noise_t.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_t, 'tStopRefresh')  # time at next scr refresh
                    noise_t.setAutoDraw(False)
            if noise_t.status == STARTED:
                if noise_t._needBuild:
                    noise_t.buildNoise()
            
            # *noise_c* updates
            if noise_c.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_c.frameNStart = frameN  # exact frame index
                noise_c.tStart = t  # local t and not account for scr refresh
                noise_c.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_c, 'tStartRefresh')  # time at next scr refresh
                noise_c.setAutoDraw(True)
            if noise_c.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_c.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_c.tStop = t  # not accounting for scr refresh
                    noise_c.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_c, 'tStopRefresh')  # time at next scr refresh
                    noise_c.setAutoDraw(False)
            if noise_c.status == STARTED:
                if noise_c._needBuild:
                    noise_c.buildNoise()
            
            # *newRect_MS3* updates
            if newRect_MS3.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                newRect_MS3.frameNStart = frameN  # exact frame index
                newRect_MS3.tStart = t  # local t and not account for scr refresh
                newRect_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MS3, 'tStartRefresh')  # time at next scr refresh
                newRect_MS3.setAutoDraw(True)
            
            # *newStar_MS3* updates
            if newStar_MS3.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                newStar_MS3.frameNStart = frameN  # exact frame index
                newStar_MS3.tStart = t  # local t and not account for scr refresh
                newStar_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newStar_MS3, 'tStartRefresh')  # time at next scr refresh
                newStar_MS3.setAutoDraw(True)
            
            # *newCirc_MS3* updates
            if newCirc_MS3.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                newCirc_MS3.frameNStart = frameN  # exact frame index
                newCirc_MS3.tStart = t  # local t and not account for scr refresh
                newCirc_MS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc_MS3, 'tStartRefresh')  # time at next scr refresh
                newCirc_MS3.setAutoDraw(True)
            
            # *key_resp_11* updates
            waitOnFlip = False
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                text_10.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskSq_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskSq_3"-------
        for thisComponent in MaskSq_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SqLoopT.addData('fix_MS3.started', fix_MS3.tStartRefresh)
        SqLoopT.addData('fix_MS3.stopped', fix_MS3.tStopRefresh)
        SqLoopT.addData('Rect_MS3.started', Rect_MS3.tStartRefresh)
        SqLoopT.addData('Rect_MS3.stopped', Rect_MS3.tStopRefresh)
        SqLoopT.addData('Star_MS3.started', Star_MS3.tStartRefresh)
        SqLoopT.addData('Star_MS3.stopped', Star_MS3.tStopRefresh)
        SqLoopT.addData('circ_MS3.started', circ_MS3.tStartRefresh)
        SqLoopT.addData('circ_MS3.stopped', circ_MS3.tStopRefresh)
        SqLoopT.addData('noise_s.started', noise_s.tStartRefresh)
        SqLoopT.addData('noise_s.stopped', noise_s.tStopRefresh)
        SqLoopT.addData('noise_t.started', noise_t.tStartRefresh)
        SqLoopT.addData('noise_t.stopped', noise_t.tStopRefresh)
        SqLoopT.addData('noise_c.started', noise_c.tStartRefresh)
        SqLoopT.addData('noise_c.stopped', noise_c.tStopRefresh)
        SqLoopT.addData('newRect_MS3.started', newRect_MS3.tStartRefresh)
        SqLoopT.addData('newRect_MS3.stopped', newRect_MS3.tStopRefresh)
        SqLoopT.addData('newStar_MS3.started', newStar_MS3.tStartRefresh)
        SqLoopT.addData('newStar_MS3.stopped', newStar_MS3.tStopRefresh)
        SqLoopT.addData('newCirc_MS3.started', newCirc_MS3.tStartRefresh)
        SqLoopT.addData('newCirc_MS3.stopped', newCirc_MS3.tStopRefresh)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        SqLoopT.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            SqLoopT.addData('key_resp_11.rt', key_resp_11.rt)
        SqLoopT.addData('key_resp_11.started', key_resp_11.tStartRefresh)
        SqLoopT.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
        SqLoopT.addData('text_10.started', text_10.tStartRefresh)
        SqLoopT.addData('text_10.stopped', text_10.tStopRefresh)
        # the Routine "MaskSq_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskSqT repeats of 'SqLoopT'
    
    
    # set up handler to look after randomisation of conditions etc
    TriLoopT = data.TrialHandler(nReps=MaskTriT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TriLoopT')
    thisExp.addLoop(TriLoopT)  # add the loop to the experiment
    thisTriLoopT = TriLoopT.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTriLoopT.rgb)
    if thisTriLoopT != None:
        for paramName in thisTriLoopT:
            exec('{} = thisTriLoopT[paramName]'.format(paramName))
    
    for thisTriLoopT in TriLoopT:
        currentLoop = TriLoopT
        # abbreviate parameter names if possible (e.g. rgb = thisTriLoopT.rgb)
        if thisTriLoopT != None:
            for paramName in thisTriLoopT:
                exec('{} = thisTriLoopT[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskTri_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        shuffle(newPositions)
        
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[0]
        if newPositions[0] == positions[2]:
             newPositions[0] = positions[0]
        rect1_MTC.setPos(positions[1])
        rect1_MTC.setFillColor(colors[1])
        rect1_MTC.setLineColor([1,1,1])
        tri1_MTC.setPos(positions[0])
        tri1_MTC.setFillColor(colors[0])
        tri1_MTC.setLineColor([1,1,1])
        Oct1_MTC.setPos(positions[2])
        Oct1_MTC.setFillColor(colors[2])
        Oct1_MTC.setLineColor([1,1,1])
        noise_rect_MTC.setColor(colors[1], colorSpace='rgb')
        noise_rect_MTC.setPos(positions[1])
        noise_tri_MTC.setColor(colors[0], colorSpace='rgb')
        noise_tri_MTC.setPos(positions[0])
        noise_circ_MTC.setColor(colors[2], colorSpace='rgb')
        noise_circ_MTC.setPos(positions[2])
        newRect_MTC.setPos(positions[1])
        newRect_MTC.setFillColor(colors[1])
        newRect_MTC.setLineColor([1,1,1])
        newTri_MTC.setPos(newPositions[0])
        newTri_MTC.setFillColor(colors[0])
        newTri_MTC.setLineColor([1,1,1])
        newOct_MTC.setPos(positions[2])
        newOct_MTC.setFillColor(colors[2])
        newOct_MTC.setLineColor([1,1,1])
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        MaskTri_3Components = [fixation_MT3, rect1_MTC, tri1_MTC, Oct1_MTC, noise_rect_MTC, noise_tri_MTC, noise_circ_MTC, newRect_MTC, newTri_MTC, newOct_MTC, text_4, key_resp_5]
        for thisComponent in MaskTri_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskTri_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskTri_3"-------
        while continueRoutine:
            # get current time
            t = MaskTri_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskTri_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_MT3* updates
            if fixation_MT3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_MT3.frameNStart = frameN  # exact frame index
                fixation_MT3.tStart = t  # local t and not account for scr refresh
                fixation_MT3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_MT3, 'tStartRefresh')  # time at next scr refresh
                fixation_MT3.setAutoDraw(True)
            if fixation_MT3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_MT3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_MT3.tStop = t  # not accounting for scr refresh
                    fixation_MT3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_MT3, 'tStopRefresh')  # time at next scr refresh
                    fixation_MT3.setAutoDraw(False)
            
            # *rect1_MTC* updates
            if rect1_MTC.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                rect1_MTC.frameNStart = frameN  # exact frame index
                rect1_MTC.tStart = t  # local t and not account for scr refresh
                rect1_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect1_MTC, 'tStartRefresh')  # time at next scr refresh
                rect1_MTC.setAutoDraw(True)
            if rect1_MTC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect1_MTC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rect1_MTC.tStop = t  # not accounting for scr refresh
                    rect1_MTC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rect1_MTC, 'tStopRefresh')  # time at next scr refresh
                    rect1_MTC.setAutoDraw(False)
            
            # *tri1_MTC* updates
            if tri1_MTC.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri1_MTC.frameNStart = frameN  # exact frame index
                tri1_MTC.tStart = t  # local t and not account for scr refresh
                tri1_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri1_MTC, 'tStartRefresh')  # time at next scr refresh
                tri1_MTC.setAutoDraw(True)
            if tri1_MTC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri1_MTC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri1_MTC.tStop = t  # not accounting for scr refresh
                    tri1_MTC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri1_MTC, 'tStopRefresh')  # time at next scr refresh
                    tri1_MTC.setAutoDraw(False)
            
            # *Oct1_MTC* updates
            if Oct1_MTC.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Oct1_MTC.frameNStart = frameN  # exact frame index
                Oct1_MTC.tStart = t  # local t and not account for scr refresh
                Oct1_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Oct1_MTC, 'tStartRefresh')  # time at next scr refresh
                Oct1_MTC.setAutoDraw(True)
            if Oct1_MTC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Oct1_MTC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Oct1_MTC.tStop = t  # not accounting for scr refresh
                    Oct1_MTC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Oct1_MTC, 'tStopRefresh')  # time at next scr refresh
                    Oct1_MTC.setAutoDraw(False)
            
            # *noise_rect_MTC* updates
            if noise_rect_MTC.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_rect_MTC.frameNStart = frameN  # exact frame index
                noise_rect_MTC.tStart = t  # local t and not account for scr refresh
                noise_rect_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_rect_MTC, 'tStartRefresh')  # time at next scr refresh
                noise_rect_MTC.setAutoDraw(True)
            if noise_rect_MTC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_rect_MTC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_rect_MTC.tStop = t  # not accounting for scr refresh
                    noise_rect_MTC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_rect_MTC, 'tStopRefresh')  # time at next scr refresh
                    noise_rect_MTC.setAutoDraw(False)
            if noise_rect_MTC.status == STARTED:
                if noise_rect_MTC._needBuild:
                    noise_rect_MTC.buildNoise()
            
            # *noise_tri_MTC* updates
            if noise_tri_MTC.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_tri_MTC.frameNStart = frameN  # exact frame index
                noise_tri_MTC.tStart = t  # local t and not account for scr refresh
                noise_tri_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_tri_MTC, 'tStartRefresh')  # time at next scr refresh
                noise_tri_MTC.setAutoDraw(True)
            if noise_tri_MTC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_tri_MTC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_tri_MTC.tStop = t  # not accounting for scr refresh
                    noise_tri_MTC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_tri_MTC, 'tStopRefresh')  # time at next scr refresh
                    noise_tri_MTC.setAutoDraw(False)
            if noise_tri_MTC.status == STARTED:
                if noise_tri_MTC._needBuild:
                    noise_tri_MTC.buildNoise()
            
            # *noise_circ_MTC* updates
            if noise_circ_MTC.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_circ_MTC.frameNStart = frameN  # exact frame index
                noise_circ_MTC.tStart = t  # local t and not account for scr refresh
                noise_circ_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_circ_MTC, 'tStartRefresh')  # time at next scr refresh
                noise_circ_MTC.setAutoDraw(True)
            if noise_circ_MTC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_circ_MTC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_circ_MTC.tStop = t  # not accounting for scr refresh
                    noise_circ_MTC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_circ_MTC, 'tStopRefresh')  # time at next scr refresh
                    noise_circ_MTC.setAutoDraw(False)
            if noise_circ_MTC.status == STARTED:
                if noise_circ_MTC._needBuild:
                    noise_circ_MTC.buildNoise()
            
            # *newRect_MTC* updates
            if newRect_MTC.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newRect_MTC.frameNStart = frameN  # exact frame index
                newRect_MTC.tStart = t  # local t and not account for scr refresh
                newRect_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MTC, 'tStartRefresh')  # time at next scr refresh
                newRect_MTC.setAutoDraw(True)
            
            # *newTri_MTC* updates
            if newTri_MTC.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newTri_MTC.frameNStart = frameN  # exact frame index
                newTri_MTC.tStart = t  # local t and not account for scr refresh
                newTri_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri_MTC, 'tStartRefresh')  # time at next scr refresh
                newTri_MTC.setAutoDraw(True)
            
            # *newOct_MTC* updates
            if newOct_MTC.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newOct_MTC.frameNStart = frameN  # exact frame index
                newOct_MTC.tStart = t  # local t and not account for scr refresh
                newOct_MTC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newOct_MTC, 'tStartRefresh')  # time at next scr refresh
                newOct_MTC.setAutoDraw(True)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskTri_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskTri_3"-------
        for thisComponent in MaskTri_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TriLoopT.addData('fixation_MT3.started', fixation_MT3.tStartRefresh)
        TriLoopT.addData('fixation_MT3.stopped', fixation_MT3.tStopRefresh)
        TriLoopT.addData('rect1_MTC.started', rect1_MTC.tStartRefresh)
        TriLoopT.addData('rect1_MTC.stopped', rect1_MTC.tStopRefresh)
        TriLoopT.addData('tri1_MTC.started', tri1_MTC.tStartRefresh)
        TriLoopT.addData('tri1_MTC.stopped', tri1_MTC.tStopRefresh)
        TriLoopT.addData('Oct1_MTC.started', Oct1_MTC.tStartRefresh)
        TriLoopT.addData('Oct1_MTC.stopped', Oct1_MTC.tStopRefresh)
        TriLoopT.addData('noise_rect_MTC.started', noise_rect_MTC.tStartRefresh)
        TriLoopT.addData('noise_rect_MTC.stopped', noise_rect_MTC.tStopRefresh)
        TriLoopT.addData('noise_tri_MTC.started', noise_tri_MTC.tStartRefresh)
        TriLoopT.addData('noise_tri_MTC.stopped', noise_tri_MTC.tStopRefresh)
        TriLoopT.addData('noise_circ_MTC.started', noise_circ_MTC.tStartRefresh)
        TriLoopT.addData('noise_circ_MTC.stopped', noise_circ_MTC.tStopRefresh)
        TriLoopT.addData('newRect_MTC.started', newRect_MTC.tStartRefresh)
        TriLoopT.addData('newRect_MTC.stopped', newRect_MTC.tStopRefresh)
        TriLoopT.addData('newTri_MTC.started', newTri_MTC.tStartRefresh)
        TriLoopT.addData('newTri_MTC.stopped', newTri_MTC.tStopRefresh)
        TriLoopT.addData('newOct_MTC.started', newOct_MTC.tStartRefresh)
        TriLoopT.addData('newOct_MTC.stopped', newOct_MTC.tStopRefresh)
        TriLoopT.addData('text_4.started', text_4.tStartRefresh)
        TriLoopT.addData('text_4.stopped', text_4.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        TriLoopT.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            TriLoopT.addData('key_resp_5.rt', key_resp_5.rt)
        TriLoopT.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        TriLoopT.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "MaskTri_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskTriT repeats of 'TriLoopT'
    
    
    # set up handler to look after randomisation of conditions etc
    CircLoopThree = data.TrialHandler(nReps=MaskCircT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='CircLoopThree')
    thisExp.addLoop(CircLoopThree)  # add the loop to the experiment
    thisCircLoopThree = CircLoopThree.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCircLoopThree.rgb)
    if thisCircLoopThree != None:
        for paramName in thisCircLoopThree:
            exec('{} = thisCircLoopThree[paramName]'.format(paramName))
    
    for thisCircLoopThree in CircLoopThree:
        currentLoop = CircLoopThree
        # abbreviate parameter names if possible (e.g. rgb = thisCircLoopThree.rgb)
        if thisCircLoopThree != None:
            for paramName in thisCircLoopThree:
                exec('{} = thisCircLoopThree[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskCirc_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        shuffle(newPositions)
        
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[0]
        if newPositions[0] == positions[2]:
             newPositions[0] = positions[0]
        circ_MCC.setPos(positions[0])
        circ_MCC.setFillColor(colors[0])
        circ_MCC.setLineColor([1,1,1])
        rect_MCC.setPos(positions[1])
        rect_MCC.setFillColor(colors[1])
        tri_MCC.setPos(positions[2])
        tri_MCC.setFillColor(colors[2])
        tri_MCC.setLineColor([1,1,1])
        noise_circMCC.setColor(colors[0], colorSpace='rgb')
        noise_circMCC.setPos(positions[0])
        noise_rectMCC.setColor(colors[1], colorSpace='rgb')
        noise_rectMCC.setPos(positions[1])
        noise_triMCC.setColor(colors[2], colorSpace='rgb')
        noise_triMCC.setPos(positions[2])
        newCirc_MCC.setPos(newPositions[0])
        newCirc_MCC.setFillColor(colors[0])
        newCirc_MCC.setLineColor([1,1,1])
        newRect_MCC.setPos(positions[1])
        newRect_MCC.setFillColor(colors[1])
        newRect_MCC.setLineColor([1,1,1])
        newTri_MCC.setPos(positions[2])
        newTri_MCC.setFillColor(colors[2])
        newTri_MCC.setLineColor([1,1,1])
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        MaskCirc_3Components = [fixation_MCC, circ_MCC, rect_MCC, tri_MCC, noise_circMCC, noise_rectMCC, noise_triMCC, newCirc_MCC, newRect_MCC, newTri_MCC, text_5, key_resp_6]
        for thisComponent in MaskCirc_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskCirc_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskCirc_3"-------
        while continueRoutine:
            # get current time
            t = MaskCirc_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskCirc_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_MCC* updates
            if fixation_MCC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_MCC.frameNStart = frameN  # exact frame index
                fixation_MCC.tStart = t  # local t and not account for scr refresh
                fixation_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_MCC, 'tStartRefresh')  # time at next scr refresh
                fixation_MCC.setAutoDraw(True)
            if fixation_MCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_MCC.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_MCC.tStop = t  # not accounting for scr refresh
                    fixation_MCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_MCC, 'tStopRefresh')  # time at next scr refresh
                    fixation_MCC.setAutoDraw(False)
            
            # *circ_MCC* updates
            if circ_MCC.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_MCC.frameNStart = frameN  # exact frame index
                circ_MCC.tStart = t  # local t and not account for scr refresh
                circ_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_MCC, 'tStartRefresh')  # time at next scr refresh
                circ_MCC.setAutoDraw(True)
            if circ_MCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_MCC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_MCC.tStop = t  # not accounting for scr refresh
                    circ_MCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_MCC, 'tStopRefresh')  # time at next scr refresh
                    circ_MCC.setAutoDraw(False)
            
            # *rect_MCC* updates
            if rect_MCC.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                rect_MCC.frameNStart = frameN  # exact frame index
                rect_MCC.tStart = t  # local t and not account for scr refresh
                rect_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_MCC, 'tStartRefresh')  # time at next scr refresh
                rect_MCC.setAutoDraw(True)
            if rect_MCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_MCC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_MCC.tStop = t  # not accounting for scr refresh
                    rect_MCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rect_MCC, 'tStopRefresh')  # time at next scr refresh
                    rect_MCC.setAutoDraw(False)
            
            # *tri_MCC* updates
            if tri_MCC.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri_MCC.frameNStart = frameN  # exact frame index
                tri_MCC.tStart = t  # local t and not account for scr refresh
                tri_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_MCC, 'tStartRefresh')  # time at next scr refresh
                tri_MCC.setAutoDraw(True)
            if tri_MCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri_MCC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri_MCC.tStop = t  # not accounting for scr refresh
                    tri_MCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri_MCC, 'tStopRefresh')  # time at next scr refresh
                    tri_MCC.setAutoDraw(False)
            
            # *noise_circMCC* updates
            if noise_circMCC.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_circMCC.frameNStart = frameN  # exact frame index
                noise_circMCC.tStart = t  # local t and not account for scr refresh
                noise_circMCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_circMCC, 'tStartRefresh')  # time at next scr refresh
                noise_circMCC.setAutoDraw(True)
            if noise_circMCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_circMCC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_circMCC.tStop = t  # not accounting for scr refresh
                    noise_circMCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_circMCC, 'tStopRefresh')  # time at next scr refresh
                    noise_circMCC.setAutoDraw(False)
            if noise_circMCC.status == STARTED:
                if noise_circMCC._needBuild:
                    noise_circMCC.buildNoise()
            
            # *noise_rectMCC* updates
            if noise_rectMCC.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_rectMCC.frameNStart = frameN  # exact frame index
                noise_rectMCC.tStart = t  # local t and not account for scr refresh
                noise_rectMCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_rectMCC, 'tStartRefresh')  # time at next scr refresh
                noise_rectMCC.setAutoDraw(True)
            if noise_rectMCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_rectMCC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_rectMCC.tStop = t  # not accounting for scr refresh
                    noise_rectMCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_rectMCC, 'tStopRefresh')  # time at next scr refresh
                    noise_rectMCC.setAutoDraw(False)
            if noise_rectMCC.status == STARTED:
                if noise_rectMCC._needBuild:
                    noise_rectMCC.buildNoise()
            
            # *noise_triMCC* updates
            if noise_triMCC.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_triMCC.frameNStart = frameN  # exact frame index
                noise_triMCC.tStart = t  # local t and not account for scr refresh
                noise_triMCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_triMCC, 'tStartRefresh')  # time at next scr refresh
                noise_triMCC.setAutoDraw(True)
            if noise_triMCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_triMCC.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_triMCC.tStop = t  # not accounting for scr refresh
                    noise_triMCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_triMCC, 'tStopRefresh')  # time at next scr refresh
                    noise_triMCC.setAutoDraw(False)
            if noise_triMCC.status == STARTED:
                if noise_triMCC._needBuild:
                    noise_triMCC.buildNoise()
            
            # *newCirc_MCC* updates
            if newCirc_MCC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newCirc_MCC.frameNStart = frameN  # exact frame index
                newCirc_MCC.tStart = t  # local t and not account for scr refresh
                newCirc_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc_MCC, 'tStartRefresh')  # time at next scr refresh
                newCirc_MCC.setAutoDraw(True)
            
            # *newRect_MCC* updates
            if newRect_MCC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newRect_MCC.frameNStart = frameN  # exact frame index
                newRect_MCC.tStart = t  # local t and not account for scr refresh
                newRect_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MCC, 'tStartRefresh')  # time at next scr refresh
                newRect_MCC.setAutoDraw(True)
            
            # *newTri_MCC* updates
            if newTri_MCC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newTri_MCC.frameNStart = frameN  # exact frame index
                newTri_MCC.tStart = t  # local t and not account for scr refresh
                newTri_MCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri_MCC, 'tStartRefresh')  # time at next scr refresh
                newTri_MCC.setAutoDraw(True)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_6* updates
            waitOnFlip = False
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskCirc_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskCirc_3"-------
        for thisComponent in MaskCirc_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CircLoopThree.addData('fixation_MCC.started', fixation_MCC.tStartRefresh)
        CircLoopThree.addData('fixation_MCC.stopped', fixation_MCC.tStopRefresh)
        CircLoopThree.addData('circ_MCC.started', circ_MCC.tStartRefresh)
        CircLoopThree.addData('circ_MCC.stopped', circ_MCC.tStopRefresh)
        CircLoopThree.addData('rect_MCC.started', rect_MCC.tStartRefresh)
        CircLoopThree.addData('rect_MCC.stopped', rect_MCC.tStopRefresh)
        CircLoopThree.addData('tri_MCC.started', tri_MCC.tStartRefresh)
        CircLoopThree.addData('tri_MCC.stopped', tri_MCC.tStopRefresh)
        CircLoopThree.addData('noise_circMCC.started', noise_circMCC.tStartRefresh)
        CircLoopThree.addData('noise_circMCC.stopped', noise_circMCC.tStopRefresh)
        CircLoopThree.addData('noise_rectMCC.started', noise_rectMCC.tStartRefresh)
        CircLoopThree.addData('noise_rectMCC.stopped', noise_rectMCC.tStopRefresh)
        CircLoopThree.addData('noise_triMCC.started', noise_triMCC.tStartRefresh)
        CircLoopThree.addData('noise_triMCC.stopped', noise_triMCC.tStopRefresh)
        CircLoopThree.addData('newCirc_MCC.started', newCirc_MCC.tStartRefresh)
        CircLoopThree.addData('newCirc_MCC.stopped', newCirc_MCC.tStopRefresh)
        CircLoopThree.addData('newRect_MCC.started', newRect_MCC.tStartRefresh)
        CircLoopThree.addData('newRect_MCC.stopped', newRect_MCC.tStopRefresh)
        CircLoopThree.addData('newTri_MCC.started', newTri_MCC.tStartRefresh)
        CircLoopThree.addData('newTri_MCC.stopped', newTri_MCC.tStopRefresh)
        CircLoopThree.addData('text_5.started', text_5.tStartRefresh)
        CircLoopThree.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        CircLoopThree.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            CircLoopThree.addData('key_resp_6.rt', key_resp_6.rt)
        CircLoopThree.addData('key_resp_6.started', key_resp_6.tStartRefresh)
        CircLoopThree.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
        # the Routine "MaskCirc_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskCircT repeats of 'CircLoopThree'
    
    
    # set up handler to look after randomisation of conditions etc
    SqLoopFive = data.TrialHandler(nReps=MaskStarF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SqLoopFive')
    thisExp.addLoop(SqLoopFive)  # add the loop to the experiment
    thisSqLoopFive = SqLoopFive.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSqLoopFive.rgb)
    if thisSqLoopFive != None:
        for paramName in thisSqLoopFive:
            exec('{} = thisSqLoopFive[paramName]'.format(paramName))
    
    for thisSqLoopFive in SqLoopFive:
        currentLoop = SqLoopFive
        # abbreviate parameter names if possible (e.g. rgb = thisSqLoopFive.rgb)
        if thisSqLoopFive != None:
            for paramName in thisSqLoopFive:
                exec('{} = thisSqLoopFive[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskStar_5"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[3]:
            shuffle(colors)
        if colors[0] == colors[4]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[1] == colors[3]:
            shuffle(colors)
        if colors[1] == colors[4]:
            shuffle(colors)
        if colors[2] == colors[3]:
            shuffle(colors)
        if colors[2] == colors[4]:
            shuffle(colors)
        if colors[3] == colors[4]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        
        Rect.setPos(positions[0])
        Rect.setFillColor(colors[0])
        Rect.setLineColor([1,1,1])
        Tri.setPos(positions[1])
        Tri.setFillColor(colors[1])
        Tri.setLineColor([1,1,1])
        Circ.setPos(positions[2])
        Circ.setFillColor(colors[2])
        Circ.setLineColor([1,1,1])
        Oct.setPos(positions[3])
        Oct.setFillColor(colors[3])
        Oct.setLineColor([1,1,1])
        Star.setPos(positions[4])
        Star.setFillColor(colors[4])
        Star.setLineColor([1,1,1])
        noise_Star_MSt5.setColor(colors[4], colorSpace='rgb')
        noise_Star_MSt5.setPos(positions[4])
        noise_Rect_MSt5.setColor(colors[0], colorSpace='rgb')
        noise_Rect_MSt5.setPos(positions[0])
        noise_Tri_MSt5.setColor(colors[1], colorSpace='rgb')
        noise_Tri_MSt5.setPos(positions[1])
        noise_Circ_MSt5.setColor(colors[2], colorSpace='rgb')
        noise_Circ_MSt5.setPos(positions[2])
        noise_Oct_MSt5.setColor(colors[3], colorSpace='rgb')
        noise_Oct_MSt5.setPos(positions[3])
        newRect.setPos(positions[0])
        newRect.setFillColor(colors[0])
        newRect.setLineColor([1,1,1])
        newTri.setPos(positions[1])
        newTri.setFillColor(colors[1])
        newTri.setLineColor([1,1,1])
        newCirc.setPos(positions[2])
        newCirc.setFillColor(colors[2])
        newCirc.setLineColor([1,1,1])
        newOct.setPos(positions[3])
        newOct.setFillColor(colors[3])
        newOct.setLineColor([1,1,1])
        newStar_CHNG.setPos(newPositions[0])
        newStar_CHNG.setFillColor(colors[4])
        newStar_CHNG.setLineColor([1,1,1])
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        MaskStar_5Components = [fix, Rect, Tri, Circ, Oct, Star, noise_Star_MSt5, noise_Rect_MSt5, noise_Tri_MSt5, noise_Circ_MSt5, noise_Oct_MSt5, newRect, newTri, newCirc, newOct, newStar_CHNG, cdInstruc, key_resp_2]
        for thisComponent in MaskStar_5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskStar_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskStar_5"-------
        while continueRoutine:
            # get current time
            t = MaskStar_5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskStar_5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                fix.setAutoDraw(True)
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                    fix.setAutoDraw(False)
            
            # *Rect* updates
            if Rect.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Rect.frameNStart = frameN  # exact frame index
                Rect.tStart = t  # local t and not account for scr refresh
                Rect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rect, 'tStartRefresh')  # time at next scr refresh
                Rect.setAutoDraw(True)
            if Rect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rect.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Rect.tStop = t  # not accounting for scr refresh
                    Rect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Rect, 'tStopRefresh')  # time at next scr refresh
                    Rect.setAutoDraw(False)
            
            # *Tri* updates
            if Tri.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Tri.frameNStart = frameN  # exact frame index
                Tri.tStart = t  # local t and not account for scr refresh
                Tri.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Tri, 'tStartRefresh')  # time at next scr refresh
                Tri.setAutoDraw(True)
            if Tri.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Tri.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Tri.tStop = t  # not accounting for scr refresh
                    Tri.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Tri, 'tStopRefresh')  # time at next scr refresh
                    Tri.setAutoDraw(False)
            
            # *Circ* updates
            if Circ.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Circ.frameNStart = frameN  # exact frame index
                Circ.tStart = t  # local t and not account for scr refresh
                Circ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circ, 'tStartRefresh')  # time at next scr refresh
                Circ.setAutoDraw(True)
            if Circ.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circ.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Circ.tStop = t  # not accounting for scr refresh
                    Circ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Circ, 'tStopRefresh')  # time at next scr refresh
                    Circ.setAutoDraw(False)
            
            # *Oct* updates
            if Oct.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Oct.frameNStart = frameN  # exact frame index
                Oct.tStart = t  # local t and not account for scr refresh
                Oct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Oct, 'tStartRefresh')  # time at next scr refresh
                Oct.setAutoDraw(True)
            if Oct.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Oct.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Oct.tStop = t  # not accounting for scr refresh
                    Oct.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Oct, 'tStopRefresh')  # time at next scr refresh
                    Oct.setAutoDraw(False)
            
            # *Star* updates
            if Star.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Star.frameNStart = frameN  # exact frame index
                Star.tStart = t  # local t and not account for scr refresh
                Star.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Star, 'tStartRefresh')  # time at next scr refresh
                Star.setAutoDraw(True)
            if Star.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Star.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Star.tStop = t  # not accounting for scr refresh
                    Star.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Star, 'tStopRefresh')  # time at next scr refresh
                    Star.setAutoDraw(False)
            
            # *noise_Star_MSt5* updates
            if noise_Star_MSt5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Star_MSt5.frameNStart = frameN  # exact frame index
                noise_Star_MSt5.tStart = t  # local t and not account for scr refresh
                noise_Star_MSt5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Star_MSt5, 'tStartRefresh')  # time at next scr refresh
                noise_Star_MSt5.setAutoDraw(True)
            if noise_Star_MSt5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Star_MSt5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Star_MSt5.tStop = t  # not accounting for scr refresh
                    noise_Star_MSt5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Star_MSt5, 'tStopRefresh')  # time at next scr refresh
                    noise_Star_MSt5.setAutoDraw(False)
            if noise_Star_MSt5.status == STARTED:
                if noise_Star_MSt5._needBuild:
                    noise_Star_MSt5.buildNoise()
            
            # *noise_Rect_MSt5* updates
            if noise_Rect_MSt5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Rect_MSt5.frameNStart = frameN  # exact frame index
                noise_Rect_MSt5.tStart = t  # local t and not account for scr refresh
                noise_Rect_MSt5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Rect_MSt5, 'tStartRefresh')  # time at next scr refresh
                noise_Rect_MSt5.setAutoDraw(True)
            if noise_Rect_MSt5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Rect_MSt5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Rect_MSt5.tStop = t  # not accounting for scr refresh
                    noise_Rect_MSt5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Rect_MSt5, 'tStopRefresh')  # time at next scr refresh
                    noise_Rect_MSt5.setAutoDraw(False)
            if noise_Rect_MSt5.status == STARTED:
                if noise_Rect_MSt5._needBuild:
                    noise_Rect_MSt5.buildNoise()
            
            # *noise_Tri_MSt5* updates
            if noise_Tri_MSt5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Tri_MSt5.frameNStart = frameN  # exact frame index
                noise_Tri_MSt5.tStart = t  # local t and not account for scr refresh
                noise_Tri_MSt5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Tri_MSt5, 'tStartRefresh')  # time at next scr refresh
                noise_Tri_MSt5.setAutoDraw(True)
            if noise_Tri_MSt5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Tri_MSt5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Tri_MSt5.tStop = t  # not accounting for scr refresh
                    noise_Tri_MSt5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Tri_MSt5, 'tStopRefresh')  # time at next scr refresh
                    noise_Tri_MSt5.setAutoDraw(False)
            if noise_Tri_MSt5.status == STARTED:
                if noise_Tri_MSt5._needBuild:
                    noise_Tri_MSt5.buildNoise()
            
            # *noise_Circ_MSt5* updates
            if noise_Circ_MSt5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Circ_MSt5.frameNStart = frameN  # exact frame index
                noise_Circ_MSt5.tStart = t  # local t and not account for scr refresh
                noise_Circ_MSt5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Circ_MSt5, 'tStartRefresh')  # time at next scr refresh
                noise_Circ_MSt5.setAutoDraw(True)
            if noise_Circ_MSt5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Circ_MSt5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Circ_MSt5.tStop = t  # not accounting for scr refresh
                    noise_Circ_MSt5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Circ_MSt5, 'tStopRefresh')  # time at next scr refresh
                    noise_Circ_MSt5.setAutoDraw(False)
            if noise_Circ_MSt5.status == STARTED:
                if noise_Circ_MSt5._needBuild:
                    noise_Circ_MSt5.buildNoise()
            
            # *noise_Oct_MSt5* updates
            if noise_Oct_MSt5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Oct_MSt5.frameNStart = frameN  # exact frame index
                noise_Oct_MSt5.tStart = t  # local t and not account for scr refresh
                noise_Oct_MSt5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Oct_MSt5, 'tStartRefresh')  # time at next scr refresh
                noise_Oct_MSt5.setAutoDraw(True)
            if noise_Oct_MSt5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Oct_MSt5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Oct_MSt5.tStop = t  # not accounting for scr refresh
                    noise_Oct_MSt5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Oct_MSt5, 'tStopRefresh')  # time at next scr refresh
                    noise_Oct_MSt5.setAutoDraw(False)
            if noise_Oct_MSt5.status == STARTED:
                if noise_Oct_MSt5._needBuild:
                    noise_Oct_MSt5.buildNoise()
            
            # *newRect* updates
            if newRect.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                newRect.frameNStart = frameN  # exact frame index
                newRect.tStart = t  # local t and not account for scr refresh
                newRect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect, 'tStartRefresh')  # time at next scr refresh
                newRect.setAutoDraw(True)
            
            # *newTri* updates
            if newTri.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                newTri.frameNStart = frameN  # exact frame index
                newTri.tStart = t  # local t and not account for scr refresh
                newTri.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri, 'tStartRefresh')  # time at next scr refresh
                newTri.setAutoDraw(True)
            
            # *newCirc* updates
            if newCirc.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                newCirc.frameNStart = frameN  # exact frame index
                newCirc.tStart = t  # local t and not account for scr refresh
                newCirc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc, 'tStartRefresh')  # time at next scr refresh
                newCirc.setAutoDraw(True)
            
            # *newOct* updates
            if newOct.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                newOct.frameNStart = frameN  # exact frame index
                newOct.tStart = t  # local t and not account for scr refresh
                newOct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newOct, 'tStartRefresh')  # time at next scr refresh
                newOct.setAutoDraw(True)
            
            # *newStar_CHNG* updates
            if newStar_CHNG.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                newStar_CHNG.frameNStart = frameN  # exact frame index
                newStar_CHNG.tStart = t  # local t and not account for scr refresh
                newStar_CHNG.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newStar_CHNG, 'tStartRefresh')  # time at next scr refresh
                newStar_CHNG.setAutoDraw(True)
            
            # *cdInstruc* updates
            if cdInstruc.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                cdInstruc.frameNStart = frameN  # exact frame index
                cdInstruc.tStart = t  # local t and not account for scr refresh
                cdInstruc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cdInstruc, 'tStartRefresh')  # time at next scr refresh
                cdInstruc.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['c', 'n'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskStar_5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskStar_5"-------
        for thisComponent in MaskStar_5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SqLoopFive.addData('fix.started', fix.tStartRefresh)
        SqLoopFive.addData('fix.stopped', fix.tStopRefresh)
        SqLoopFive.addData('Rect.started', Rect.tStartRefresh)
        SqLoopFive.addData('Rect.stopped', Rect.tStopRefresh)
        SqLoopFive.addData('Tri.started', Tri.tStartRefresh)
        SqLoopFive.addData('Tri.stopped', Tri.tStopRefresh)
        SqLoopFive.addData('Circ.started', Circ.tStartRefresh)
        SqLoopFive.addData('Circ.stopped', Circ.tStopRefresh)
        SqLoopFive.addData('Oct.started', Oct.tStartRefresh)
        SqLoopFive.addData('Oct.stopped', Oct.tStopRefresh)
        SqLoopFive.addData('Star.started', Star.tStartRefresh)
        SqLoopFive.addData('Star.stopped', Star.tStopRefresh)
        SqLoopFive.addData('noise_Star_MSt5.started', noise_Star_MSt5.tStartRefresh)
        SqLoopFive.addData('noise_Star_MSt5.stopped', noise_Star_MSt5.tStopRefresh)
        SqLoopFive.addData('noise_Rect_MSt5.started', noise_Rect_MSt5.tStartRefresh)
        SqLoopFive.addData('noise_Rect_MSt5.stopped', noise_Rect_MSt5.tStopRefresh)
        SqLoopFive.addData('noise_Tri_MSt5.started', noise_Tri_MSt5.tStartRefresh)
        SqLoopFive.addData('noise_Tri_MSt5.stopped', noise_Tri_MSt5.tStopRefresh)
        SqLoopFive.addData('noise_Circ_MSt5.started', noise_Circ_MSt5.tStartRefresh)
        SqLoopFive.addData('noise_Circ_MSt5.stopped', noise_Circ_MSt5.tStopRefresh)
        SqLoopFive.addData('noise_Oct_MSt5.started', noise_Oct_MSt5.tStartRefresh)
        SqLoopFive.addData('noise_Oct_MSt5.stopped', noise_Oct_MSt5.tStopRefresh)
        SqLoopFive.addData('newRect.started', newRect.tStartRefresh)
        SqLoopFive.addData('newRect.stopped', newRect.tStopRefresh)
        SqLoopFive.addData('newTri.started', newTri.tStartRefresh)
        SqLoopFive.addData('newTri.stopped', newTri.tStopRefresh)
        SqLoopFive.addData('newCirc.started', newCirc.tStartRefresh)
        SqLoopFive.addData('newCirc.stopped', newCirc.tStopRefresh)
        SqLoopFive.addData('newOct.started', newOct.tStartRefresh)
        SqLoopFive.addData('newOct.stopped', newOct.tStopRefresh)
        SqLoopFive.addData('newStar_CHNG.started', newStar_CHNG.tStartRefresh)
        SqLoopFive.addData('newStar_CHNG.stopped', newStar_CHNG.tStopRefresh)
        SqLoopFive.addData('cdInstruc.started', cdInstruc.tStartRefresh)
        SqLoopFive.addData('cdInstruc.stopped', cdInstruc.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        SqLoopFive.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            SqLoopFive.addData('key_resp_2.rt', key_resp_2.rt)
        SqLoopFive.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        SqLoopFive.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "MaskStar_5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskStarF repeats of 'SqLoopFive'
    
    
    # set up handler to look after randomisation of conditions etc
    SqLoopF = data.TrialHandler(nReps=MaskSqF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SqLoopF')
    thisExp.addLoop(SqLoopF)  # add the loop to the experiment
    thisSqLoopF = SqLoopF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSqLoopF.rgb)
    if thisSqLoopF != None:
        for paramName in thisSqLoopF:
            exec('{} = thisSqLoopF[paramName]'.format(paramName))
    
    for thisSqLoopF in SqLoopF:
        currentLoop = SqLoopF
        # abbreviate parameter names if possible (e.g. rgb = thisSqLoopF.rgb)
        if thisSqLoopF != None:
            for paramName in thisSqLoopF:
                exec('{} = thisSqLoopF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskSq_5"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[3]:
            shuffle(colors)
        if colors[0] == colors[4]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[1] == colors[3]:
            shuffle(colors)
        if colors[1] == colors[4]:
            shuffle(colors)
        if colors[2] == colors[3]:
            shuffle(colors)
        if colors[2] == colors[4]:
            shuffle(colors)
        if colors[3] == colors[4]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        Tri_MSq5.setPos(positions[0])
        Tri_MSq5.setFillColor(colors[0])
        Tri_MSq5.setLineColor([1,1,1])
        circ_MSq5.setPos(positions[1])
        circ_MSq5.setFillColor(colors[1])
        circ_MSq5.setLineColor([1,1,1])
        oct_MSq5.setPos(positions[2])
        oct_MSq5.setFillColor(colors[2])
        oct_MSq5.setLineColor([1,1,1])
        star_MSq5.setPos(positions[3])
        star_MSq5.setFillColor(colors[3])
        star_MSq5.setLineColor([1,1,1])
        square_MSq5.setPos(positions[4])
        square_MSq5.setFillColor(colors[4])
        square_MSq5.setLineColor([1,1,1])
        noise_triMSq5.setColor(colors[0], colorSpace='rgb')
        noise_triMSq5.setPos(positions[0])
        noise_CircMSq5.setColor(colors[1], colorSpace='rgb')
        noise_CircMSq5.setPos(positions[1])
        noise_OctMsq5.setColor(colors[2], colorSpace='rgb')
        noise_OctMsq5.setPos(positions[2])
        noise_starMSq5.setColor(colors[3], colorSpace='rgb')
        noise_starMSq5.setPos(positions[3])
        noise_RectMSq5.setColor(colors[4], colorSpace='rgb')
        noise_RectMSq5.setPos(positions[4])
        newTri_MSq5.setPos(positions[0])
        newTri_MSq5.setFillColor(colors[0])
        newTri_MSq5.setLineColor([1,1,1])
        newCirc_MSq5.setPos(positions[1])
        newCirc_MSq5.setFillColor(colors[1])
        newCirc_MSq5.setLineColor([1,1,1])
        NewOct_MSq5.setPos(positions[2])
        NewOct_MSq5.setFillColor(colors[2])
        NewOct_MSq5.setLineColor([1,1,1])
        newStar_MSq5.setPos(newPositions[0])
        newStar_MSq5.setFillColor(colors[3])
        newStar_MSq5.setLineColor([1,1,1])
        newRect_MSq5.setPos(newPositions[1])
        newRect_MSq5.setFillColor(colors[4])
        newRect_MSq5.setLineColor([1,1,1])
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # keep track of which components have finished
        MaskSq_5Components = [fixation_MSq5, Tri_MSq5, circ_MSq5, oct_MSq5, star_MSq5, square_MSq5, noise_triMSq5, noise_CircMSq5, noise_OctMsq5, noise_starMSq5, noise_RectMSq5, newTri_MSq5, newCirc_MSq5, NewOct_MSq5, newStar_MSq5, newRect_MSq5, text_6, key_resp_7]
        for thisComponent in MaskSq_5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskSq_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskSq_5"-------
        while continueRoutine:
            # get current time
            t = MaskSq_5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskSq_5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_MSq5* updates
            if fixation_MSq5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_MSq5.frameNStart = frameN  # exact frame index
                fixation_MSq5.tStart = t  # local t and not account for scr refresh
                fixation_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_MSq5, 'tStartRefresh')  # time at next scr refresh
                fixation_MSq5.setAutoDraw(True)
            if fixation_MSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_MSq5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_MSq5.tStop = t  # not accounting for scr refresh
                    fixation_MSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_MSq5, 'tStopRefresh')  # time at next scr refresh
                    fixation_MSq5.setAutoDraw(False)
            
            # *Tri_MSq5* updates
            if Tri_MSq5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Tri_MSq5.frameNStart = frameN  # exact frame index
                Tri_MSq5.tStart = t  # local t and not account for scr refresh
                Tri_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Tri_MSq5, 'tStartRefresh')  # time at next scr refresh
                Tri_MSq5.setAutoDraw(True)
            if Tri_MSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Tri_MSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Tri_MSq5.tStop = t  # not accounting for scr refresh
                    Tri_MSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Tri_MSq5, 'tStopRefresh')  # time at next scr refresh
                    Tri_MSq5.setAutoDraw(False)
            
            # *circ_MSq5* updates
            if circ_MSq5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_MSq5.frameNStart = frameN  # exact frame index
                circ_MSq5.tStart = t  # local t and not account for scr refresh
                circ_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_MSq5, 'tStartRefresh')  # time at next scr refresh
                circ_MSq5.setAutoDraw(True)
            if circ_MSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_MSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_MSq5.tStop = t  # not accounting for scr refresh
                    circ_MSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_MSq5, 'tStopRefresh')  # time at next scr refresh
                    circ_MSq5.setAutoDraw(False)
            
            # *oct_MSq5* updates
            if oct_MSq5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                oct_MSq5.frameNStart = frameN  # exact frame index
                oct_MSq5.tStart = t  # local t and not account for scr refresh
                oct_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(oct_MSq5, 'tStartRefresh')  # time at next scr refresh
                oct_MSq5.setAutoDraw(True)
            if oct_MSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > oct_MSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    oct_MSq5.tStop = t  # not accounting for scr refresh
                    oct_MSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(oct_MSq5, 'tStopRefresh')  # time at next scr refresh
                    oct_MSq5.setAutoDraw(False)
            
            # *star_MSq5* updates
            if star_MSq5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                star_MSq5.frameNStart = frameN  # exact frame index
                star_MSq5.tStart = t  # local t and not account for scr refresh
                star_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_MSq5, 'tStartRefresh')  # time at next scr refresh
                star_MSq5.setAutoDraw(True)
            if star_MSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_MSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    star_MSq5.tStop = t  # not accounting for scr refresh
                    star_MSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_MSq5, 'tStopRefresh')  # time at next scr refresh
                    star_MSq5.setAutoDraw(False)
            
            # *square_MSq5* updates
            if square_MSq5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                square_MSq5.frameNStart = frameN  # exact frame index
                square_MSq5.tStart = t  # local t and not account for scr refresh
                square_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_MSq5, 'tStartRefresh')  # time at next scr refresh
                square_MSq5.setAutoDraw(True)
            if square_MSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_MSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    square_MSq5.tStop = t  # not accounting for scr refresh
                    square_MSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_MSq5, 'tStopRefresh')  # time at next scr refresh
                    square_MSq5.setAutoDraw(False)
            
            # *noise_triMSq5* updates
            if noise_triMSq5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_triMSq5.frameNStart = frameN  # exact frame index
                noise_triMSq5.tStart = t  # local t and not account for scr refresh
                noise_triMSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_triMSq5, 'tStartRefresh')  # time at next scr refresh
                noise_triMSq5.setAutoDraw(True)
            if noise_triMSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_triMSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_triMSq5.tStop = t  # not accounting for scr refresh
                    noise_triMSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_triMSq5, 'tStopRefresh')  # time at next scr refresh
                    noise_triMSq5.setAutoDraw(False)
            if noise_triMSq5.status == STARTED:
                if noise_triMSq5._needBuild:
                    noise_triMSq5.buildNoise()
            
            # *noise_CircMSq5* updates
            if noise_CircMSq5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_CircMSq5.frameNStart = frameN  # exact frame index
                noise_CircMSq5.tStart = t  # local t and not account for scr refresh
                noise_CircMSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_CircMSq5, 'tStartRefresh')  # time at next scr refresh
                noise_CircMSq5.setAutoDraw(True)
            if noise_CircMSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_CircMSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_CircMSq5.tStop = t  # not accounting for scr refresh
                    noise_CircMSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_CircMSq5, 'tStopRefresh')  # time at next scr refresh
                    noise_CircMSq5.setAutoDraw(False)
            if noise_CircMSq5.status == STARTED:
                if noise_CircMSq5._needBuild:
                    noise_CircMSq5.buildNoise()
            
            # *noise_OctMsq5* updates
            if noise_OctMsq5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_OctMsq5.frameNStart = frameN  # exact frame index
                noise_OctMsq5.tStart = t  # local t and not account for scr refresh
                noise_OctMsq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_OctMsq5, 'tStartRefresh')  # time at next scr refresh
                noise_OctMsq5.setAutoDraw(True)
            if noise_OctMsq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_OctMsq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_OctMsq5.tStop = t  # not accounting for scr refresh
                    noise_OctMsq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_OctMsq5, 'tStopRefresh')  # time at next scr refresh
                    noise_OctMsq5.setAutoDraw(False)
            if noise_OctMsq5.status == STARTED:
                if noise_OctMsq5._needBuild:
                    noise_OctMsq5.buildNoise()
            
            # *noise_starMSq5* updates
            if noise_starMSq5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_starMSq5.frameNStart = frameN  # exact frame index
                noise_starMSq5.tStart = t  # local t and not account for scr refresh
                noise_starMSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_starMSq5, 'tStartRefresh')  # time at next scr refresh
                noise_starMSq5.setAutoDraw(True)
            if noise_starMSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_starMSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_starMSq5.tStop = t  # not accounting for scr refresh
                    noise_starMSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_starMSq5, 'tStopRefresh')  # time at next scr refresh
                    noise_starMSq5.setAutoDraw(False)
            if noise_starMSq5.status == STARTED:
                if noise_starMSq5._needBuild:
                    noise_starMSq5.buildNoise()
            
            # *noise_RectMSq5* updates
            if noise_RectMSq5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_RectMSq5.frameNStart = frameN  # exact frame index
                noise_RectMSq5.tStart = t  # local t and not account for scr refresh
                noise_RectMSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_RectMSq5, 'tStartRefresh')  # time at next scr refresh
                noise_RectMSq5.setAutoDraw(True)
            if noise_RectMSq5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_RectMSq5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_RectMSq5.tStop = t  # not accounting for scr refresh
                    noise_RectMSq5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_RectMSq5, 'tStopRefresh')  # time at next scr refresh
                    noise_RectMSq5.setAutoDraw(False)
            if noise_RectMSq5.status == STARTED:
                if noise_RectMSq5._needBuild:
                    noise_RectMSq5.buildNoise()
            
            # *newTri_MSq5* updates
            if newTri_MSq5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                newTri_MSq5.frameNStart = frameN  # exact frame index
                newTri_MSq5.tStart = t  # local t and not account for scr refresh
                newTri_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri_MSq5, 'tStartRefresh')  # time at next scr refresh
                newTri_MSq5.setAutoDraw(True)
            
            # *newCirc_MSq5* updates
            if newCirc_MSq5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                newCirc_MSq5.frameNStart = frameN  # exact frame index
                newCirc_MSq5.tStart = t  # local t and not account for scr refresh
                newCirc_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc_MSq5, 'tStartRefresh')  # time at next scr refresh
                newCirc_MSq5.setAutoDraw(True)
            
            # *NewOct_MSq5* updates
            if NewOct_MSq5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                NewOct_MSq5.frameNStart = frameN  # exact frame index
                NewOct_MSq5.tStart = t  # local t and not account for scr refresh
                NewOct_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NewOct_MSq5, 'tStartRefresh')  # time at next scr refresh
                NewOct_MSq5.setAutoDraw(True)
            
            # *newStar_MSq5* updates
            if newStar_MSq5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                newStar_MSq5.frameNStart = frameN  # exact frame index
                newStar_MSq5.tStart = t  # local t and not account for scr refresh
                newStar_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newStar_MSq5, 'tStartRefresh')  # time at next scr refresh
                newStar_MSq5.setAutoDraw(True)
            
            # *newRect_MSq5* updates
            if newRect_MSq5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                newRect_MSq5.frameNStart = frameN  # exact frame index
                newRect_MSq5.tStart = t  # local t and not account for scr refresh
                newRect_MSq5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MSq5, 'tStartRefresh')  # time at next scr refresh
                newRect_MSq5.setAutoDraw(True)
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            
            # *key_resp_7* updates
            waitOnFlip = False
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskSq_5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskSq_5"-------
        for thisComponent in MaskSq_5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SqLoopF.addData('fixation_MSq5.started', fixation_MSq5.tStartRefresh)
        SqLoopF.addData('fixation_MSq5.stopped', fixation_MSq5.tStopRefresh)
        SqLoopF.addData('Tri_MSq5.started', Tri_MSq5.tStartRefresh)
        SqLoopF.addData('Tri_MSq5.stopped', Tri_MSq5.tStopRefresh)
        SqLoopF.addData('circ_MSq5.started', circ_MSq5.tStartRefresh)
        SqLoopF.addData('circ_MSq5.stopped', circ_MSq5.tStopRefresh)
        SqLoopF.addData('oct_MSq5.started', oct_MSq5.tStartRefresh)
        SqLoopF.addData('oct_MSq5.stopped', oct_MSq5.tStopRefresh)
        SqLoopF.addData('star_MSq5.started', star_MSq5.tStartRefresh)
        SqLoopF.addData('star_MSq5.stopped', star_MSq5.tStopRefresh)
        SqLoopF.addData('square_MSq5.started', square_MSq5.tStartRefresh)
        SqLoopF.addData('square_MSq5.stopped', square_MSq5.tStopRefresh)
        SqLoopF.addData('noise_triMSq5.started', noise_triMSq5.tStartRefresh)
        SqLoopF.addData('noise_triMSq5.stopped', noise_triMSq5.tStopRefresh)
        SqLoopF.addData('noise_CircMSq5.started', noise_CircMSq5.tStartRefresh)
        SqLoopF.addData('noise_CircMSq5.stopped', noise_CircMSq5.tStopRefresh)
        SqLoopF.addData('noise_OctMsq5.started', noise_OctMsq5.tStartRefresh)
        SqLoopF.addData('noise_OctMsq5.stopped', noise_OctMsq5.tStopRefresh)
        SqLoopF.addData('noise_starMSq5.started', noise_starMSq5.tStartRefresh)
        SqLoopF.addData('noise_starMSq5.stopped', noise_starMSq5.tStopRefresh)
        SqLoopF.addData('noise_RectMSq5.started', noise_RectMSq5.tStartRefresh)
        SqLoopF.addData('noise_RectMSq5.stopped', noise_RectMSq5.tStopRefresh)
        SqLoopF.addData('newTri_MSq5.started', newTri_MSq5.tStartRefresh)
        SqLoopF.addData('newTri_MSq5.stopped', newTri_MSq5.tStopRefresh)
        SqLoopF.addData('newCirc_MSq5.started', newCirc_MSq5.tStartRefresh)
        SqLoopF.addData('newCirc_MSq5.stopped', newCirc_MSq5.tStopRefresh)
        SqLoopF.addData('NewOct_MSq5.started', NewOct_MSq5.tStartRefresh)
        SqLoopF.addData('NewOct_MSq5.stopped', NewOct_MSq5.tStopRefresh)
        SqLoopF.addData('newStar_MSq5.started', newStar_MSq5.tStartRefresh)
        SqLoopF.addData('newStar_MSq5.stopped', newStar_MSq5.tStopRefresh)
        SqLoopF.addData('newRect_MSq5.started', newRect_MSq5.tStartRefresh)
        SqLoopF.addData('newRect_MSq5.stopped', newRect_MSq5.tStopRefresh)
        SqLoopF.addData('text_6.started', text_6.tStartRefresh)
        SqLoopF.addData('text_6.stopped', text_6.tStopRefresh)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        SqLoopF.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            SqLoopF.addData('key_resp_7.rt', key_resp_7.rt)
        SqLoopF.addData('key_resp_7.started', key_resp_7.tStartRefresh)
        SqLoopF.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
        # the Routine "MaskSq_5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskSqF repeats of 'SqLoopF'
    
    
    # set up handler to look after randomisation of conditions etc
    CircLoopF = data.TrialHandler(nReps=MaskCircF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='CircLoopF')
    thisExp.addLoop(CircLoopF)  # add the loop to the experiment
    thisCircLoopF = CircLoopF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCircLoopF.rgb)
    if thisCircLoopF != None:
        for paramName in thisCircLoopF:
            exec('{} = thisCircLoopF[paramName]'.format(paramName))
    
    for thisCircLoopF in CircLoopF:
        currentLoop = CircLoopF
        # abbreviate parameter names if possible (e.g. rgb = thisCircLoopF.rgb)
        if thisCircLoopF != None:
            for paramName in thisCircLoopF:
                exec('{} = thisCircLoopF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskCirc_5"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[3]:
            shuffle(colors)
        if colors[0] == colors[4]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[1] == colors[3]:
            shuffle(colors)
        if colors[1] == colors[4]:
            shuffle(colors)
        if colors[2] == colors[3]:
            shuffle(colors)
        if colors[2] == colors[4]:
            shuffle(colors)
        if colors[3] == colors[4]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        
        Tri_MSC5.setPos(positions[0])
        Tri_MSC5.setFillColor(colors[0])
        Tri_MSC5.setLineColor([1,1,1])
        Oct_MSC5.setPos(positions[1])
        Oct_MSC5.setFillColor(colors[1])
        Oct_MSC5.setLineColor([1,1,1])
        Star_MSC5.setPos(positions[2])
        Star_MSC5.setFillColor(colors[2])
        Star_MSC5.setLineColor([1,1,1])
        Rect_MSC5.setPos(positions[3])
        Rect_MSC5.setFillColor(colors[3])
        Rect_MSC5.setLineColor([1,1,1])
        Circ_MSC5.setPos(positions[4])
        Circ_MSC5.setFillColor(colors[4])
        Circ_MSC5.setLineColor([1,1,1])
        noise_TriMSC5.setColor(colors[0], colorSpace='rgb')
        noise_TriMSC5.setPos(positions[0])
        noise_OctMSC5.setColor(colors[1], colorSpace='rgb')
        noise_OctMSC5.setPos(positions[1])
        noise_StarMSC5.setColor(colors[2], colorSpace='rgb')
        noise_StarMSC5.setPos(positions[2])
        noise_RectMSC5.setColor(colors[3], colorSpace='rgb')
        noise_RectMSC5.setPos(positions[3])
        noise_CircMSC5.setColor(colors[4], colorSpace='rgb')
        noise_CircMSC5.setPos(positions[4])
        newTri_MSC5.setPos(positions[0])
        newTri_MSC5.setFillColor(colors[0])
        newTri_MSC5.setLineColor([1,1,1])
        newOct_MSC5.setPos(positions[1])
        newOct_MSC5.setFillColor(colors[1])
        newOct_MSC5.setLineColor([1,1,1])
        newStar_MSC5.setPos(positions[2])
        newStar_MSC5.setFillColor(colors[2])
        newStar_MSC5.setLineColor([1,1,1])
        newRect_MSC5.setPos(newPositions[0])
        newRect_MSC5.setFillColor(colors[3])
        newRect_MSC5.setLineColor([1,1,1])
        newCirc_CHANGE.setPos(newPositions[1])
        newCirc_CHANGE.setFillColor(colors[4])
        newCirc_CHANGE.setLineColor([1,1,1])
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # keep track of which components have finished
        MaskCirc_5Components = [fixation_MSC5, Tri_MSC5, Oct_MSC5, Star_MSC5, Rect_MSC5, Circ_MSC5, noise_TriMSC5, noise_OctMSC5, noise_StarMSC5, noise_RectMSC5, noise_CircMSC5, newTri_MSC5, newOct_MSC5, newStar_MSC5, newRect_MSC5, newCirc_CHANGE, text_7, key_resp_8]
        for thisComponent in MaskCirc_5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskCirc_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskCirc_5"-------
        while continueRoutine:
            # get current time
            t = MaskCirc_5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskCirc_5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_MSC5* updates
            if fixation_MSC5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_MSC5.frameNStart = frameN  # exact frame index
                fixation_MSC5.tStart = t  # local t and not account for scr refresh
                fixation_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_MSC5, 'tStartRefresh')  # time at next scr refresh
                fixation_MSC5.setAutoDraw(True)
            if fixation_MSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_MSC5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_MSC5.tStop = t  # not accounting for scr refresh
                    fixation_MSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_MSC5, 'tStopRefresh')  # time at next scr refresh
                    fixation_MSC5.setAutoDraw(False)
            
            # *Tri_MSC5* updates
            if Tri_MSC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Tri_MSC5.frameNStart = frameN  # exact frame index
                Tri_MSC5.tStart = t  # local t and not account for scr refresh
                Tri_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Tri_MSC5, 'tStartRefresh')  # time at next scr refresh
                Tri_MSC5.setAutoDraw(True)
            if Tri_MSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Tri_MSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Tri_MSC5.tStop = t  # not accounting for scr refresh
                    Tri_MSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Tri_MSC5, 'tStopRefresh')  # time at next scr refresh
                    Tri_MSC5.setAutoDraw(False)
            
            # *Oct_MSC5* updates
            if Oct_MSC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Oct_MSC5.frameNStart = frameN  # exact frame index
                Oct_MSC5.tStart = t  # local t and not account for scr refresh
                Oct_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Oct_MSC5, 'tStartRefresh')  # time at next scr refresh
                Oct_MSC5.setAutoDraw(True)
            if Oct_MSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Oct_MSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Oct_MSC5.tStop = t  # not accounting for scr refresh
                    Oct_MSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Oct_MSC5, 'tStopRefresh')  # time at next scr refresh
                    Oct_MSC5.setAutoDraw(False)
            
            # *Star_MSC5* updates
            if Star_MSC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Star_MSC5.frameNStart = frameN  # exact frame index
                Star_MSC5.tStart = t  # local t and not account for scr refresh
                Star_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Star_MSC5, 'tStartRefresh')  # time at next scr refresh
                Star_MSC5.setAutoDraw(True)
            if Star_MSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Star_MSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Star_MSC5.tStop = t  # not accounting for scr refresh
                    Star_MSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Star_MSC5, 'tStopRefresh')  # time at next scr refresh
                    Star_MSC5.setAutoDraw(False)
            
            # *Rect_MSC5* updates
            if Rect_MSC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Rect_MSC5.frameNStart = frameN  # exact frame index
                Rect_MSC5.tStart = t  # local t and not account for scr refresh
                Rect_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rect_MSC5, 'tStartRefresh')  # time at next scr refresh
                Rect_MSC5.setAutoDraw(True)
            if Rect_MSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rect_MSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Rect_MSC5.tStop = t  # not accounting for scr refresh
                    Rect_MSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Rect_MSC5, 'tStopRefresh')  # time at next scr refresh
                    Rect_MSC5.setAutoDraw(False)
            
            # *Circ_MSC5* updates
            if Circ_MSC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Circ_MSC5.frameNStart = frameN  # exact frame index
                Circ_MSC5.tStart = t  # local t and not account for scr refresh
                Circ_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circ_MSC5, 'tStartRefresh')  # time at next scr refresh
                Circ_MSC5.setAutoDraw(True)
            if Circ_MSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circ_MSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Circ_MSC5.tStop = t  # not accounting for scr refresh
                    Circ_MSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Circ_MSC5, 'tStopRefresh')  # time at next scr refresh
                    Circ_MSC5.setAutoDraw(False)
            
            # *noise_TriMSC5* updates
            if noise_TriMSC5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_TriMSC5.frameNStart = frameN  # exact frame index
                noise_TriMSC5.tStart = t  # local t and not account for scr refresh
                noise_TriMSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_TriMSC5, 'tStartRefresh')  # time at next scr refresh
                noise_TriMSC5.setAutoDraw(True)
            if noise_TriMSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_TriMSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_TriMSC5.tStop = t  # not accounting for scr refresh
                    noise_TriMSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_TriMSC5, 'tStopRefresh')  # time at next scr refresh
                    noise_TriMSC5.setAutoDraw(False)
            if noise_TriMSC5.status == STARTED:
                if noise_TriMSC5._needBuild:
                    noise_TriMSC5.buildNoise()
            
            # *noise_OctMSC5* updates
            if noise_OctMSC5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_OctMSC5.frameNStart = frameN  # exact frame index
                noise_OctMSC5.tStart = t  # local t and not account for scr refresh
                noise_OctMSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_OctMSC5, 'tStartRefresh')  # time at next scr refresh
                noise_OctMSC5.setAutoDraw(True)
            if noise_OctMSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_OctMSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_OctMSC5.tStop = t  # not accounting for scr refresh
                    noise_OctMSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_OctMSC5, 'tStopRefresh')  # time at next scr refresh
                    noise_OctMSC5.setAutoDraw(False)
            if noise_OctMSC5.status == STARTED:
                if noise_OctMSC5._needBuild:
                    noise_OctMSC5.buildNoise()
            
            # *noise_StarMSC5* updates
            if noise_StarMSC5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_StarMSC5.frameNStart = frameN  # exact frame index
                noise_StarMSC5.tStart = t  # local t and not account for scr refresh
                noise_StarMSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_StarMSC5, 'tStartRefresh')  # time at next scr refresh
                noise_StarMSC5.setAutoDraw(True)
            if noise_StarMSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_StarMSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_StarMSC5.tStop = t  # not accounting for scr refresh
                    noise_StarMSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_StarMSC5, 'tStopRefresh')  # time at next scr refresh
                    noise_StarMSC5.setAutoDraw(False)
            if noise_StarMSC5.status == STARTED:
                if noise_StarMSC5._needBuild:
                    noise_StarMSC5.buildNoise()
            
            # *noise_RectMSC5* updates
            if noise_RectMSC5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_RectMSC5.frameNStart = frameN  # exact frame index
                noise_RectMSC5.tStart = t  # local t and not account for scr refresh
                noise_RectMSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_RectMSC5, 'tStartRefresh')  # time at next scr refresh
                noise_RectMSC5.setAutoDraw(True)
            if noise_RectMSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_RectMSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_RectMSC5.tStop = t  # not accounting for scr refresh
                    noise_RectMSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_RectMSC5, 'tStopRefresh')  # time at next scr refresh
                    noise_RectMSC5.setAutoDraw(False)
            if noise_RectMSC5.status == STARTED:
                if noise_RectMSC5._needBuild:
                    noise_RectMSC5.buildNoise()
            
            # *noise_CircMSC5* updates
            if noise_CircMSC5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_CircMSC5.frameNStart = frameN  # exact frame index
                noise_CircMSC5.tStart = t  # local t and not account for scr refresh
                noise_CircMSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_CircMSC5, 'tStartRefresh')  # time at next scr refresh
                noise_CircMSC5.setAutoDraw(True)
            if noise_CircMSC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_CircMSC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_CircMSC5.tStop = t  # not accounting for scr refresh
                    noise_CircMSC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_CircMSC5, 'tStopRefresh')  # time at next scr refresh
                    noise_CircMSC5.setAutoDraw(False)
            if noise_CircMSC5.status == STARTED:
                if noise_CircMSC5._needBuild:
                    noise_CircMSC5.buildNoise()
            
            # *newTri_MSC5* updates
            if newTri_MSC5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newTri_MSC5.frameNStart = frameN  # exact frame index
                newTri_MSC5.tStart = t  # local t and not account for scr refresh
                newTri_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri_MSC5, 'tStartRefresh')  # time at next scr refresh
                newTri_MSC5.setAutoDraw(True)
            
            # *newOct_MSC5* updates
            if newOct_MSC5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newOct_MSC5.frameNStart = frameN  # exact frame index
                newOct_MSC5.tStart = t  # local t and not account for scr refresh
                newOct_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newOct_MSC5, 'tStartRefresh')  # time at next scr refresh
                newOct_MSC5.setAutoDraw(True)
            
            # *newStar_MSC5* updates
            if newStar_MSC5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newStar_MSC5.frameNStart = frameN  # exact frame index
                newStar_MSC5.tStart = t  # local t and not account for scr refresh
                newStar_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newStar_MSC5, 'tStartRefresh')  # time at next scr refresh
                newStar_MSC5.setAutoDraw(True)
            
            # *newRect_MSC5* updates
            if newRect_MSC5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newRect_MSC5.frameNStart = frameN  # exact frame index
                newRect_MSC5.tStart = t  # local t and not account for scr refresh
                newRect_MSC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MSC5, 'tStartRefresh')  # time at next scr refresh
                newRect_MSC5.setAutoDraw(True)
            
            # *newCirc_CHANGE* updates
            if newCirc_CHANGE.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newCirc_CHANGE.frameNStart = frameN  # exact frame index
                newCirc_CHANGE.tStart = t  # local t and not account for scr refresh
                newCirc_CHANGE.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc_CHANGE, 'tStartRefresh')  # time at next scr refresh
                newCirc_CHANGE.setAutoDraw(True)
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskCirc_5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskCirc_5"-------
        for thisComponent in MaskCirc_5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CircLoopF.addData('fixation_MSC5.started', fixation_MSC5.tStartRefresh)
        CircLoopF.addData('fixation_MSC5.stopped', fixation_MSC5.tStopRefresh)
        CircLoopF.addData('Tri_MSC5.started', Tri_MSC5.tStartRefresh)
        CircLoopF.addData('Tri_MSC5.stopped', Tri_MSC5.tStopRefresh)
        CircLoopF.addData('Oct_MSC5.started', Oct_MSC5.tStartRefresh)
        CircLoopF.addData('Oct_MSC5.stopped', Oct_MSC5.tStopRefresh)
        CircLoopF.addData('Star_MSC5.started', Star_MSC5.tStartRefresh)
        CircLoopF.addData('Star_MSC5.stopped', Star_MSC5.tStopRefresh)
        CircLoopF.addData('Rect_MSC5.started', Rect_MSC5.tStartRefresh)
        CircLoopF.addData('Rect_MSC5.stopped', Rect_MSC5.tStopRefresh)
        CircLoopF.addData('Circ_MSC5.started', Circ_MSC5.tStartRefresh)
        CircLoopF.addData('Circ_MSC5.stopped', Circ_MSC5.tStopRefresh)
        CircLoopF.addData('noise_TriMSC5.started', noise_TriMSC5.tStartRefresh)
        CircLoopF.addData('noise_TriMSC5.stopped', noise_TriMSC5.tStopRefresh)
        CircLoopF.addData('noise_OctMSC5.started', noise_OctMSC5.tStartRefresh)
        CircLoopF.addData('noise_OctMSC5.stopped', noise_OctMSC5.tStopRefresh)
        CircLoopF.addData('noise_StarMSC5.started', noise_StarMSC5.tStartRefresh)
        CircLoopF.addData('noise_StarMSC5.stopped', noise_StarMSC5.tStopRefresh)
        CircLoopF.addData('noise_RectMSC5.started', noise_RectMSC5.tStartRefresh)
        CircLoopF.addData('noise_RectMSC5.stopped', noise_RectMSC5.tStopRefresh)
        CircLoopF.addData('noise_CircMSC5.started', noise_CircMSC5.tStartRefresh)
        CircLoopF.addData('noise_CircMSC5.stopped', noise_CircMSC5.tStopRefresh)
        CircLoopF.addData('newTri_MSC5.started', newTri_MSC5.tStartRefresh)
        CircLoopF.addData('newTri_MSC5.stopped', newTri_MSC5.tStopRefresh)
        CircLoopF.addData('newOct_MSC5.started', newOct_MSC5.tStartRefresh)
        CircLoopF.addData('newOct_MSC5.stopped', newOct_MSC5.tStopRefresh)
        CircLoopF.addData('newStar_MSC5.started', newStar_MSC5.tStartRefresh)
        CircLoopF.addData('newStar_MSC5.stopped', newStar_MSC5.tStopRefresh)
        CircLoopF.addData('newRect_MSC5.started', newRect_MSC5.tStartRefresh)
        CircLoopF.addData('newRect_MSC5.stopped', newRect_MSC5.tStopRefresh)
        CircLoopF.addData('newCirc_CHANGE.started', newCirc_CHANGE.tStartRefresh)
        CircLoopF.addData('newCirc_CHANGE.stopped', newCirc_CHANGE.tStopRefresh)
        CircLoopF.addData('text_7.started', text_7.tStartRefresh)
        CircLoopF.addData('text_7.stopped', text_7.tStopRefresh)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        CircLoopF.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            CircLoopF.addData('key_resp_8.rt', key_resp_8.rt)
        CircLoopF.addData('key_resp_8.started', key_resp_8.tStartRefresh)
        CircLoopF.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
        # the Routine "MaskCirc_5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskCircF repeats of 'CircLoopF'
    
    
    # set up handler to look after randomisation of conditions etc
    TriLoopF = data.TrialHandler(nReps=MaskTriF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TriLoopF')
    thisExp.addLoop(TriLoopF)  # add the loop to the experiment
    thisTriLoopF = TriLoopF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTriLoopF.rgb)
    if thisTriLoopF != None:
        for paramName in thisTriLoopF:
            exec('{} = thisTriLoopF[paramName]'.format(paramName))
    
    for thisTriLoopF in TriLoopF:
        currentLoop = TriLoopF
        # abbreviate parameter names if possible (e.g. rgb = thisTriLoopF.rgb)
        if thisTriLoopF != None:
            for paramName in thisTriLoopF:
                exec('{} = thisTriLoopF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskTri_5"-------
        continueRoutine = True
        # update component parameters for each repeat
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        
        Oct_MT5.setPos(positions[0])
        Oct_MT5.setFillColor(colors[0])
        Oct_MT5.setLineColor([1,1,1])
        Star_MT5.setPos(positions[1])
        Star_MT5.setFillColor(colors[1])
        Star_MT5.setLineColor([1,1,1])
        Rect_MT5.setPos(positions[2])
        Rect_MT5.setFillColor(colors[2])
        Rect_MT5.setLineColor([1,1,1])
        Circ_MT5.setPos(positions[3])
        Circ_MT5.setFillColor(colors[3])
        Circ_MT5.setLineColor([1,1,1])
        Tri_MT5.setPos(positions[4])
        Tri_MT5.setFillColor(colors[4])
        Tri_MT5.setLineColor([1,1,1])
        noise_Oct.setColor(colors[0], colorSpace='rgb')
        noise_Oct.setPos(positions[0])
        noise_star.setColor(colors[1], colorSpace='rgb')
        noise_star.setPos(positions[1])
        noise_Rect.setColor(colors[2], colorSpace='rgb')
        noise_Rect.setPos(positions[2])
        noise_Circ.setColor(colors[3], colorSpace='rgb')
        noise_Circ.setPos(positions[3])
        noise_Tri.setColor(colors[4], colorSpace='rgb')
        noise_Tri.setPos(positions[4])
        newOct_MT5.setPos(positions[0])
        newOct_MT5.setFillColor(colors[0])
        newOct_MT5.setLineColor([1,1,1])
        newStar_MT5.setPos(positions[1])
        newStar_MT5.setFillColor(colors[1])
        newStar_MT5.setLineColor([1,1,1])
        newRect_MT5.setPos(positions[2])
        newRect_MT5.setFillColor(colors[2])
        newRect_MT5.setLineColor([1,1,1])
        newCirc_MT5.setPos(newPositions[0])
        newCirc_MT5.setFillColor(colors[3])
        newCirc_MT5.setLineColor([1,1,1])
        newTri_CHANGE.setPos(newPositions[1])
        newTri_CHANGE.setFillColor(colors[4])
        newTri_CHANGE.setLineColor([1,1,1])
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # keep track of which components have finished
        MaskTri_5Components = [fixation_MT5, Oct_MT5, Star_MT5, Rect_MT5, Circ_MT5, Tri_MT5, noise_Oct, noise_star, noise_Rect, noise_Circ, noise_Tri, newOct_MT5, newStar_MT5, newRect_MT5, newCirc_MT5, newTri_CHANGE, key_resp_9, text_8]
        for thisComponent in MaskTri_5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskTri_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskTri_5"-------
        while continueRoutine:
            # get current time
            t = MaskTri_5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskTri_5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_MT5* updates
            if fixation_MT5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_MT5.frameNStart = frameN  # exact frame index
                fixation_MT5.tStart = t  # local t and not account for scr refresh
                fixation_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_MT5, 'tStartRefresh')  # time at next scr refresh
                fixation_MT5.setAutoDraw(True)
            if fixation_MT5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_MT5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_MT5.tStop = t  # not accounting for scr refresh
                    fixation_MT5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_MT5, 'tStopRefresh')  # time at next scr refresh
                    fixation_MT5.setAutoDraw(False)
            
            # *Oct_MT5* updates
            if Oct_MT5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Oct_MT5.frameNStart = frameN  # exact frame index
                Oct_MT5.tStart = t  # local t and not account for scr refresh
                Oct_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Oct_MT5, 'tStartRefresh')  # time at next scr refresh
                Oct_MT5.setAutoDraw(True)
            if Oct_MT5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Oct_MT5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Oct_MT5.tStop = t  # not accounting for scr refresh
                    Oct_MT5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Oct_MT5, 'tStopRefresh')  # time at next scr refresh
                    Oct_MT5.setAutoDraw(False)
            
            # *Star_MT5* updates
            if Star_MT5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Star_MT5.frameNStart = frameN  # exact frame index
                Star_MT5.tStart = t  # local t and not account for scr refresh
                Star_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Star_MT5, 'tStartRefresh')  # time at next scr refresh
                Star_MT5.setAutoDraw(True)
            if Star_MT5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Star_MT5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Star_MT5.tStop = t  # not accounting for scr refresh
                    Star_MT5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Star_MT5, 'tStopRefresh')  # time at next scr refresh
                    Star_MT5.setAutoDraw(False)
            
            # *Rect_MT5* updates
            if Rect_MT5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Rect_MT5.frameNStart = frameN  # exact frame index
                Rect_MT5.tStart = t  # local t and not account for scr refresh
                Rect_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rect_MT5, 'tStartRefresh')  # time at next scr refresh
                Rect_MT5.setAutoDraw(True)
            if Rect_MT5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rect_MT5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Rect_MT5.tStop = t  # not accounting for scr refresh
                    Rect_MT5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Rect_MT5, 'tStopRefresh')  # time at next scr refresh
                    Rect_MT5.setAutoDraw(False)
            
            # *Circ_MT5* updates
            if Circ_MT5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Circ_MT5.frameNStart = frameN  # exact frame index
                Circ_MT5.tStart = t  # local t and not account for scr refresh
                Circ_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circ_MT5, 'tStartRefresh')  # time at next scr refresh
                Circ_MT5.setAutoDraw(True)
            if Circ_MT5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circ_MT5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Circ_MT5.tStop = t  # not accounting for scr refresh
                    Circ_MT5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Circ_MT5, 'tStopRefresh')  # time at next scr refresh
                    Circ_MT5.setAutoDraw(False)
            
            # *Tri_MT5* updates
            if Tri_MT5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Tri_MT5.frameNStart = frameN  # exact frame index
                Tri_MT5.tStart = t  # local t and not account for scr refresh
                Tri_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Tri_MT5, 'tStartRefresh')  # time at next scr refresh
                Tri_MT5.setAutoDraw(True)
            if Tri_MT5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Tri_MT5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Tri_MT5.tStop = t  # not accounting for scr refresh
                    Tri_MT5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Tri_MT5, 'tStopRefresh')  # time at next scr refresh
                    Tri_MT5.setAutoDraw(False)
            
            # *noise_Oct* updates
            if noise_Oct.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Oct.frameNStart = frameN  # exact frame index
                noise_Oct.tStart = t  # local t and not account for scr refresh
                noise_Oct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Oct, 'tStartRefresh')  # time at next scr refresh
                noise_Oct.setAutoDraw(True)
            if noise_Oct.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Oct.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Oct.tStop = t  # not accounting for scr refresh
                    noise_Oct.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Oct, 'tStopRefresh')  # time at next scr refresh
                    noise_Oct.setAutoDraw(False)
            if noise_Oct.status == STARTED:
                if noise_Oct._needBuild:
                    noise_Oct.buildNoise()
            
            # *noise_star* updates
            if noise_star.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_star.frameNStart = frameN  # exact frame index
                noise_star.tStart = t  # local t and not account for scr refresh
                noise_star.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_star, 'tStartRefresh')  # time at next scr refresh
                noise_star.setAutoDraw(True)
            if noise_star.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_star.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_star.tStop = t  # not accounting for scr refresh
                    noise_star.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_star, 'tStopRefresh')  # time at next scr refresh
                    noise_star.setAutoDraw(False)
            if noise_star.status == STARTED:
                if noise_star._needBuild:
                    noise_star.buildNoise()
            
            # *noise_Rect* updates
            if noise_Rect.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Rect.frameNStart = frameN  # exact frame index
                noise_Rect.tStart = t  # local t and not account for scr refresh
                noise_Rect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Rect, 'tStartRefresh')  # time at next scr refresh
                noise_Rect.setAutoDraw(True)
            if noise_Rect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Rect.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Rect.tStop = t  # not accounting for scr refresh
                    noise_Rect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Rect, 'tStopRefresh')  # time at next scr refresh
                    noise_Rect.setAutoDraw(False)
            if noise_Rect.status == STARTED:
                if noise_Rect._needBuild:
                    noise_Rect.buildNoise()
            
            # *noise_Circ* updates
            if noise_Circ.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Circ.frameNStart = frameN  # exact frame index
                noise_Circ.tStart = t  # local t and not account for scr refresh
                noise_Circ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Circ, 'tStartRefresh')  # time at next scr refresh
                noise_Circ.setAutoDraw(True)
            if noise_Circ.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Circ.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Circ.tStop = t  # not accounting for scr refresh
                    noise_Circ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Circ, 'tStopRefresh')  # time at next scr refresh
                    noise_Circ.setAutoDraw(False)
            if noise_Circ.status == STARTED:
                if noise_Circ._needBuild:
                    noise_Circ.buildNoise()
            
            # *noise_Tri* updates
            if noise_Tri.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_Tri.frameNStart = frameN  # exact frame index
                noise_Tri.tStart = t  # local t and not account for scr refresh
                noise_Tri.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_Tri, 'tStartRefresh')  # time at next scr refresh
                noise_Tri.setAutoDraw(True)
            if noise_Tri.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_Tri.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_Tri.tStop = t  # not accounting for scr refresh
                    noise_Tri.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_Tri, 'tStopRefresh')  # time at next scr refresh
                    noise_Tri.setAutoDraw(False)
            if noise_Tri.status == STARTED:
                if noise_Tri._needBuild:
                    noise_Tri.buildNoise()
            
            # *newOct_MT5* updates
            if newOct_MT5.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newOct_MT5.frameNStart = frameN  # exact frame index
                newOct_MT5.tStart = t  # local t and not account for scr refresh
                newOct_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newOct_MT5, 'tStartRefresh')  # time at next scr refresh
                newOct_MT5.setAutoDraw(True)
            
            # *newStar_MT5* updates
            if newStar_MT5.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newStar_MT5.frameNStart = frameN  # exact frame index
                newStar_MT5.tStart = t  # local t and not account for scr refresh
                newStar_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newStar_MT5, 'tStartRefresh')  # time at next scr refresh
                newStar_MT5.setAutoDraw(True)
            
            # *newRect_MT5* updates
            if newRect_MT5.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newRect_MT5.frameNStart = frameN  # exact frame index
                newRect_MT5.tStart = t  # local t and not account for scr refresh
                newRect_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MT5, 'tStartRefresh')  # time at next scr refresh
                newRect_MT5.setAutoDraw(True)
            
            # *newCirc_MT5* updates
            if newCirc_MT5.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newCirc_MT5.frameNStart = frameN  # exact frame index
                newCirc_MT5.tStart = t  # local t and not account for scr refresh
                newCirc_MT5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc_MT5, 'tStartRefresh')  # time at next scr refresh
                newCirc_MT5.setAutoDraw(True)
            
            # *newTri_CHANGE* updates
            if newTri_CHANGE.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                newTri_CHANGE.frameNStart = frameN  # exact frame index
                newTri_CHANGE.tStart = t  # local t and not account for scr refresh
                newTri_CHANGE.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri_CHANGE, 'tStartRefresh')  # time at next scr refresh
                newTri_CHANGE.setAutoDraw(True)
            
            # *key_resp_9* updates
            waitOnFlip = False
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskTri_5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskTri_5"-------
        for thisComponent in MaskTri_5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TriLoopF.addData('fixation_MT5.started', fixation_MT5.tStartRefresh)
        TriLoopF.addData('fixation_MT5.stopped', fixation_MT5.tStopRefresh)
        TriLoopF.addData('Oct_MT5.started', Oct_MT5.tStartRefresh)
        TriLoopF.addData('Oct_MT5.stopped', Oct_MT5.tStopRefresh)
        TriLoopF.addData('Star_MT5.started', Star_MT5.tStartRefresh)
        TriLoopF.addData('Star_MT5.stopped', Star_MT5.tStopRefresh)
        TriLoopF.addData('Rect_MT5.started', Rect_MT5.tStartRefresh)
        TriLoopF.addData('Rect_MT5.stopped', Rect_MT5.tStopRefresh)
        TriLoopF.addData('Circ_MT5.started', Circ_MT5.tStartRefresh)
        TriLoopF.addData('Circ_MT5.stopped', Circ_MT5.tStopRefresh)
        TriLoopF.addData('Tri_MT5.started', Tri_MT5.tStartRefresh)
        TriLoopF.addData('Tri_MT5.stopped', Tri_MT5.tStopRefresh)
        TriLoopF.addData('noise_Oct.started', noise_Oct.tStartRefresh)
        TriLoopF.addData('noise_Oct.stopped', noise_Oct.tStopRefresh)
        TriLoopF.addData('noise_star.started', noise_star.tStartRefresh)
        TriLoopF.addData('noise_star.stopped', noise_star.tStopRefresh)
        TriLoopF.addData('noise_Rect.started', noise_Rect.tStartRefresh)
        TriLoopF.addData('noise_Rect.stopped', noise_Rect.tStopRefresh)
        TriLoopF.addData('noise_Circ.started', noise_Circ.tStartRefresh)
        TriLoopF.addData('noise_Circ.stopped', noise_Circ.tStopRefresh)
        TriLoopF.addData('noise_Tri.started', noise_Tri.tStartRefresh)
        TriLoopF.addData('noise_Tri.stopped', noise_Tri.tStopRefresh)
        TriLoopF.addData('newOct_MT5.started', newOct_MT5.tStartRefresh)
        TriLoopF.addData('newOct_MT5.stopped', newOct_MT5.tStopRefresh)
        TriLoopF.addData('newStar_MT5.started', newStar_MT5.tStartRefresh)
        TriLoopF.addData('newStar_MT5.stopped', newStar_MT5.tStopRefresh)
        TriLoopF.addData('newRect_MT5.started', newRect_MT5.tStartRefresh)
        TriLoopF.addData('newRect_MT5.stopped', newRect_MT5.tStopRefresh)
        TriLoopF.addData('newCirc_MT5.started', newCirc_MT5.tStartRefresh)
        TriLoopF.addData('newCirc_MT5.stopped', newCirc_MT5.tStopRefresh)
        TriLoopF.addData('newTri_CHANGE.started', newTri_CHANGE.tStartRefresh)
        TriLoopF.addData('newTri_CHANGE.stopped', newTri_CHANGE.tStopRefresh)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        TriLoopF.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            TriLoopF.addData('key_resp_9.rt', key_resp_9.rt)
        TriLoopF.addData('key_resp_9.started', key_resp_9.tStartRefresh)
        TriLoopF.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
        TriLoopF.addData('text_8.started', text_8.tStartRefresh)
        TriLoopF.addData('text_8.stopped', text_8.tStopRefresh)
        # the Routine "MaskTri_5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskTriF repeats of 'TriLoopF'
    
    
    # set up handler to look after randomisation of conditions etc
    OctLoopF = data.TrialHandler(nReps=MaskOctF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='OctLoopF')
    thisExp.addLoop(OctLoopF)  # add the loop to the experiment
    thisOctLoopF = OctLoopF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOctLoopF.rgb)
    if thisOctLoopF != None:
        for paramName in thisOctLoopF:
            exec('{} = thisOctLoopF[paramName]'.format(paramName))
    
    for thisOctLoopF in OctLoopF:
        currentLoop = OctLoopF
        # abbreviate parameter names if possible (e.g. rgb = thisOctLoopF.rgb)
        if thisOctLoopF != None:
            for paramName in thisOctLoopF:
                exec('{} = thisOctLoopF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MaskOct_5"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[3]:
            shuffle(colors)
        if colors[0] == colors[4]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[1] == colors[3]:
            shuffle(colors)
        if colors[1] == colors[4]:
            shuffle(colors)
        if colors[2] == colors[3]:
            shuffle(colors)
        if colors[2] == colors[4]:
            shuffle(colors)
        if colors[3] == colors[4]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        
        star_MO5.setPos(positions[0])
        star_MO5.setFillColor(colors[0])
        star_MO5.setLineColor([1,1,1])
        circ_MO5.setPos(positions[1])
        circ_MO5.setFillColor(colors[1])
        circ_MO5.setLineColor([1,1,1])
        rect_MO5.setPos(positions[2])
        rect_MO5.setFillColor(colors[2])
        rect_MO5.setLineColor([1,1,1])
        tri_MO5.setPos(positions[3])
        tri_MO5.setFillColor(colors[3])
        tri_MO5.setLineColor([1,1,1])
        oct_MO5.setPos(positions[4])
        oct_MO5.setFillColor(colors[4])
        oct_MO5.setLineColor([1,1,1])
        noise_starMO5.setColor(colors[0], colorSpace='rgb')
        noise_starMO5.setPos(positions[0])
        noise_circMO5.setColor(colors[1], colorSpace='rgb')
        noise_circMO5.setPos(positions[1])
        noise_rectMO5.setColor(colors[2], colorSpace='rgb')
        noise_rectMO5.setPos(positions[2])
        noise_triMO5.setColor(colors[3], colorSpace='rgb')
        noise_triMO5.setPos(positions[3])
        noise_octMO5.setColor(colors[3], colorSpace='rgb')
        noise_octMO5.setPos(positions[3])
        newStar_MO5.setPos(positions[0])
        newStar_MO5.setFillColor(colors[0])
        newStar_MO5.setLineColor([1,1,1])
        newCirc_MO5.setPos(positions[1])
        newCirc_MO5.setFillColor(colors[1])
        newCirc_MO5.setLineColor([1,1,1])
        newRect_MO5.setPos(positions[2])
        newRect_MO5.setFillColor(colors[2])
        newRect_MO5.setLineColor([1,1,1])
        newTri_MO5.setPos(positions[3])
        newTri_MO5.setFillColor(colors[3])
        newTri_MO5.setLineColor([1,1,1])
        newOct_CHANGE.setPos(newPositions[0])
        newOct_CHANGE.setFillColor(colors[4])
        newOct_CHANGE.setLineColor([1,1,1])
        key_resp_10.keys = []
        key_resp_10.rt = []
        _key_resp_10_allKeys = []
        # keep track of which components have finished
        MaskOct_5Components = [fixation_MO5, star_MO5, circ_MO5, rect_MO5, tri_MO5, oct_MO5, noise_starMO5, noise_circMO5, noise_rectMO5, noise_triMO5, noise_octMO5, newStar_MO5, newCirc_MO5, newRect_MO5, newTri_MO5, newOct_CHANGE, text_9, key_resp_10]
        for thisComponent in MaskOct_5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MaskOct_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MaskOct_5"-------
        while continueRoutine:
            # get current time
            t = MaskOct_5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MaskOct_5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_MO5* updates
            if fixation_MO5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_MO5.frameNStart = frameN  # exact frame index
                fixation_MO5.tStart = t  # local t and not account for scr refresh
                fixation_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_MO5, 'tStartRefresh')  # time at next scr refresh
                fixation_MO5.setAutoDraw(True)
            if fixation_MO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_MO5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_MO5.tStop = t  # not accounting for scr refresh
                    fixation_MO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_MO5, 'tStopRefresh')  # time at next scr refresh
                    fixation_MO5.setAutoDraw(False)
            
            # *star_MO5* updates
            if star_MO5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                star_MO5.frameNStart = frameN  # exact frame index
                star_MO5.tStart = t  # local t and not account for scr refresh
                star_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_MO5, 'tStartRefresh')  # time at next scr refresh
                star_MO5.setAutoDraw(True)
            if star_MO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_MO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    star_MO5.tStop = t  # not accounting for scr refresh
                    star_MO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_MO5, 'tStopRefresh')  # time at next scr refresh
                    star_MO5.setAutoDraw(False)
            
            # *circ_MO5* updates
            if circ_MO5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_MO5.frameNStart = frameN  # exact frame index
                circ_MO5.tStart = t  # local t and not account for scr refresh
                circ_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_MO5, 'tStartRefresh')  # time at next scr refresh
                circ_MO5.setAutoDraw(True)
            if circ_MO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_MO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_MO5.tStop = t  # not accounting for scr refresh
                    circ_MO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_MO5, 'tStopRefresh')  # time at next scr refresh
                    circ_MO5.setAutoDraw(False)
            
            # *rect_MO5* updates
            if rect_MO5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                rect_MO5.frameNStart = frameN  # exact frame index
                rect_MO5.tStart = t  # local t and not account for scr refresh
                rect_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_MO5, 'tStartRefresh')  # time at next scr refresh
                rect_MO5.setAutoDraw(True)
            if rect_MO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_MO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_MO5.tStop = t  # not accounting for scr refresh
                    rect_MO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rect_MO5, 'tStopRefresh')  # time at next scr refresh
                    rect_MO5.setAutoDraw(False)
            
            # *tri_MO5* updates
            if tri_MO5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri_MO5.frameNStart = frameN  # exact frame index
                tri_MO5.tStart = t  # local t and not account for scr refresh
                tri_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_MO5, 'tStartRefresh')  # time at next scr refresh
                tri_MO5.setAutoDraw(True)
            if tri_MO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri_MO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri_MO5.tStop = t  # not accounting for scr refresh
                    tri_MO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri_MO5, 'tStopRefresh')  # time at next scr refresh
                    tri_MO5.setAutoDraw(False)
            
            # *oct_MO5* updates
            if oct_MO5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                oct_MO5.frameNStart = frameN  # exact frame index
                oct_MO5.tStart = t  # local t and not account for scr refresh
                oct_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(oct_MO5, 'tStartRefresh')  # time at next scr refresh
                oct_MO5.setAutoDraw(True)
            if oct_MO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > oct_MO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    oct_MO5.tStop = t  # not accounting for scr refresh
                    oct_MO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(oct_MO5, 'tStopRefresh')  # time at next scr refresh
                    oct_MO5.setAutoDraw(False)
            
            # *noise_starMO5* updates
            if noise_starMO5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_starMO5.frameNStart = frameN  # exact frame index
                noise_starMO5.tStart = t  # local t and not account for scr refresh
                noise_starMO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_starMO5, 'tStartRefresh')  # time at next scr refresh
                noise_starMO5.setAutoDraw(True)
            if noise_starMO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_starMO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_starMO5.tStop = t  # not accounting for scr refresh
                    noise_starMO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_starMO5, 'tStopRefresh')  # time at next scr refresh
                    noise_starMO5.setAutoDraw(False)
            if noise_starMO5.status == STARTED:
                if noise_starMO5._needBuild:
                    noise_starMO5.buildNoise()
            
            # *noise_circMO5* updates
            if noise_circMO5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_circMO5.frameNStart = frameN  # exact frame index
                noise_circMO5.tStart = t  # local t and not account for scr refresh
                noise_circMO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_circMO5, 'tStartRefresh')  # time at next scr refresh
                noise_circMO5.setAutoDraw(True)
            if noise_circMO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_circMO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_circMO5.tStop = t  # not accounting for scr refresh
                    noise_circMO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_circMO5, 'tStopRefresh')  # time at next scr refresh
                    noise_circMO5.setAutoDraw(False)
            if noise_circMO5.status == STARTED:
                if noise_circMO5._needBuild:
                    noise_circMO5.buildNoise()
            
            # *noise_rectMO5* updates
            if noise_rectMO5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_rectMO5.frameNStart = frameN  # exact frame index
                noise_rectMO5.tStart = t  # local t and not account for scr refresh
                noise_rectMO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_rectMO5, 'tStartRefresh')  # time at next scr refresh
                noise_rectMO5.setAutoDraw(True)
            if noise_rectMO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_rectMO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_rectMO5.tStop = t  # not accounting for scr refresh
                    noise_rectMO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_rectMO5, 'tStopRefresh')  # time at next scr refresh
                    noise_rectMO5.setAutoDraw(False)
            if noise_rectMO5.status == STARTED:
                if noise_rectMO5._needBuild:
                    noise_rectMO5.buildNoise()
            
            # *noise_triMO5* updates
            if noise_triMO5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_triMO5.frameNStart = frameN  # exact frame index
                noise_triMO5.tStart = t  # local t and not account for scr refresh
                noise_triMO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_triMO5, 'tStartRefresh')  # time at next scr refresh
                noise_triMO5.setAutoDraw(True)
            if noise_triMO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_triMO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_triMO5.tStop = t  # not accounting for scr refresh
                    noise_triMO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_triMO5, 'tStopRefresh')  # time at next scr refresh
                    noise_triMO5.setAutoDraw(False)
            if noise_triMO5.status == STARTED:
                if noise_triMO5._needBuild:
                    noise_triMO5.buildNoise()
            
            # *noise_octMO5* updates
            if noise_octMO5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                noise_octMO5.frameNStart = frameN  # exact frame index
                noise_octMO5.tStart = t  # local t and not account for scr refresh
                noise_octMO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_octMO5, 'tStartRefresh')  # time at next scr refresh
                noise_octMO5.setAutoDraw(True)
            if noise_octMO5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_octMO5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_octMO5.tStop = t  # not accounting for scr refresh
                    noise_octMO5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_octMO5, 'tStopRefresh')  # time at next scr refresh
                    noise_octMO5.setAutoDraw(False)
            if noise_octMO5.status == STARTED:
                if noise_octMO5._needBuild:
                    noise_octMO5.buildNoise()
            
            # *newStar_MO5* updates
            if newStar_MO5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newStar_MO5.frameNStart = frameN  # exact frame index
                newStar_MO5.tStart = t  # local t and not account for scr refresh
                newStar_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newStar_MO5, 'tStartRefresh')  # time at next scr refresh
                newStar_MO5.setAutoDraw(True)
            
            # *newCirc_MO5* updates
            if newCirc_MO5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newCirc_MO5.frameNStart = frameN  # exact frame index
                newCirc_MO5.tStart = t  # local t and not account for scr refresh
                newCirc_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newCirc_MO5, 'tStartRefresh')  # time at next scr refresh
                newCirc_MO5.setAutoDraw(True)
            
            # *newRect_MO5* updates
            if newRect_MO5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newRect_MO5.frameNStart = frameN  # exact frame index
                newRect_MO5.tStart = t  # local t and not account for scr refresh
                newRect_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newRect_MO5, 'tStartRefresh')  # time at next scr refresh
                newRect_MO5.setAutoDraw(True)
            
            # *newTri_MO5* updates
            if newTri_MO5.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newTri_MO5.frameNStart = frameN  # exact frame index
                newTri_MO5.tStart = t  # local t and not account for scr refresh
                newTri_MO5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newTri_MO5, 'tStartRefresh')  # time at next scr refresh
                newTri_MO5.setAutoDraw(True)
            
            # *newOct_CHANGE* updates
            if newOct_CHANGE.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                newOct_CHANGE.frameNStart = frameN  # exact frame index
                newOct_CHANGE.tStart = t  # local t and not account for scr refresh
                newOct_CHANGE.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(newOct_CHANGE, 'tStartRefresh')  # time at next scr refresh
                newOct_CHANGE.setAutoDraw(True)
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            
            # *key_resp_10* updates
            waitOnFlip = False
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['n', 'c'], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MaskOct_5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MaskOct_5"-------
        for thisComponent in MaskOct_5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OctLoopF.addData('fixation_MO5.started', fixation_MO5.tStartRefresh)
        OctLoopF.addData('fixation_MO5.stopped', fixation_MO5.tStopRefresh)
        OctLoopF.addData('star_MO5.started', star_MO5.tStartRefresh)
        OctLoopF.addData('star_MO5.stopped', star_MO5.tStopRefresh)
        OctLoopF.addData('circ_MO5.started', circ_MO5.tStartRefresh)
        OctLoopF.addData('circ_MO5.stopped', circ_MO5.tStopRefresh)
        OctLoopF.addData('rect_MO5.started', rect_MO5.tStartRefresh)
        OctLoopF.addData('rect_MO5.stopped', rect_MO5.tStopRefresh)
        OctLoopF.addData('tri_MO5.started', tri_MO5.tStartRefresh)
        OctLoopF.addData('tri_MO5.stopped', tri_MO5.tStopRefresh)
        OctLoopF.addData('oct_MO5.started', oct_MO5.tStartRefresh)
        OctLoopF.addData('oct_MO5.stopped', oct_MO5.tStopRefresh)
        OctLoopF.addData('noise_starMO5.started', noise_starMO5.tStartRefresh)
        OctLoopF.addData('noise_starMO5.stopped', noise_starMO5.tStopRefresh)
        OctLoopF.addData('noise_circMO5.started', noise_circMO5.tStartRefresh)
        OctLoopF.addData('noise_circMO5.stopped', noise_circMO5.tStopRefresh)
        OctLoopF.addData('noise_rectMO5.started', noise_rectMO5.tStartRefresh)
        OctLoopF.addData('noise_rectMO5.stopped', noise_rectMO5.tStopRefresh)
        OctLoopF.addData('noise_triMO5.started', noise_triMO5.tStartRefresh)
        OctLoopF.addData('noise_triMO5.stopped', noise_triMO5.tStopRefresh)
        OctLoopF.addData('noise_octMO5.started', noise_octMO5.tStartRefresh)
        OctLoopF.addData('noise_octMO5.stopped', noise_octMO5.tStopRefresh)
        OctLoopF.addData('newStar_MO5.started', newStar_MO5.tStartRefresh)
        OctLoopF.addData('newStar_MO5.stopped', newStar_MO5.tStopRefresh)
        OctLoopF.addData('newCirc_MO5.started', newCirc_MO5.tStartRefresh)
        OctLoopF.addData('newCirc_MO5.stopped', newCirc_MO5.tStopRefresh)
        OctLoopF.addData('newRect_MO5.started', newRect_MO5.tStartRefresh)
        OctLoopF.addData('newRect_MO5.stopped', newRect_MO5.tStopRefresh)
        OctLoopF.addData('newTri_MO5.started', newTri_MO5.tStartRefresh)
        OctLoopF.addData('newTri_MO5.stopped', newTri_MO5.tStopRefresh)
        OctLoopF.addData('newOct_CHANGE.started', newOct_CHANGE.tStartRefresh)
        OctLoopF.addData('newOct_CHANGE.stopped', newOct_CHANGE.tStopRefresh)
        OctLoopF.addData('text_9.started', text_9.tStartRefresh)
        OctLoopF.addData('text_9.stopped', text_9.tStopRefresh)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
        OctLoopF.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            OctLoopF.addData('key_resp_10.rt', key_resp_10.rt)
        OctLoopF.addData('key_resp_10.started', key_resp_10.tStartRefresh)
        OctLoopF.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
        # the Routine "MaskOct_5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed MaskOctF repeats of 'OctLoopF'
    
    
    # set up handler to look after randomisation of conditions etc
    noChangeT = data.TrialHandler(nReps=NoChangeT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='noChangeT')
    thisExp.addLoop(noChangeT)  # add the loop to the experiment
    thisNoChangeT = noChangeT.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNoChangeT.rgb)
    if thisNoChangeT != None:
        for paramName in thisNoChangeT:
            exec('{} = thisNoChangeT[paramName]'.format(paramName))
    
    for thisNoChangeT in noChangeT:
        currentLoop = noChangeT
        # abbreviate parameter names if possible (e.g. rgb = thisNoChangeT.rgb)
        if thisNoChangeT != None:
            for paramName in thisNoChangeT:
                exec('{} = thisNoChangeT[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "NoMask3"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        shuffle(newPositions)
        
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[0]
        if newPositions[0] == positions[2]:
             newPositions[0] = positions[0]
        rect_1.setPos(positions[0])
        rect_1.setFillColor(colors[0])
        rect_1.setLineColor([1,1,1])
        tri_1.setPos(positions[1])
        tri_1.setFillColor(colors[1])
        tri_1.setLineColor([1,1,1])
        circ_1.setPos(positions[2])
        circ_1.setFillColor(colors[2])
        circ_1.setLineColor([1,1,1])
        rect_noChng.setPos(newPositions[0])
        rect_noChng.setFillColor(colors[0])
        rect_noChng.setLineColor([1,1,1])
        tri_noChng.setPos(positions[1])
        tri_noChng.setFillColor(colors[1])
        tri_noChng.setLineColor([1,1,1])
        circ_noChng.setPos(positions[2])
        circ_noChng.setFillColor(colors[2])
        circ_noChng.setLineColor([1,1,1])
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        NoMask3Components = [fixation_noChng, rect_1, tri_1, circ_1, rect_noChng, tri_noChng, circ_noChng, text, key_resp_3]
        for thisComponent in NoMask3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NoMask3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "NoMask3"-------
        while continueRoutine:
            # get current time
            t = NoMask3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NoMask3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_noChng* updates
            if fixation_noChng.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_noChng.frameNStart = frameN  # exact frame index
                fixation_noChng.tStart = t  # local t and not account for scr refresh
                fixation_noChng.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_noChng, 'tStartRefresh')  # time at next scr refresh
                fixation_noChng.setAutoDraw(True)
            if fixation_noChng.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_noChng.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_noChng.tStop = t  # not accounting for scr refresh
                    fixation_noChng.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_noChng, 'tStopRefresh')  # time at next scr refresh
                    fixation_noChng.setAutoDraw(False)
            
            # *rect_1* updates
            if rect_1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                rect_1.frameNStart = frameN  # exact frame index
                rect_1.tStart = t  # local t and not account for scr refresh
                rect_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_1, 'tStartRefresh')  # time at next scr refresh
                rect_1.setAutoDraw(True)
            if rect_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_1.tStop = t  # not accounting for scr refresh
                    rect_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rect_1, 'tStopRefresh')  # time at next scr refresh
                    rect_1.setAutoDraw(False)
            
            # *tri_1* updates
            if tri_1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri_1.frameNStart = frameN  # exact frame index
                tri_1.tStart = t  # local t and not account for scr refresh
                tri_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_1, 'tStartRefresh')  # time at next scr refresh
                tri_1.setAutoDraw(True)
            if tri_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri_1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri_1.tStop = t  # not accounting for scr refresh
                    tri_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri_1, 'tStopRefresh')  # time at next scr refresh
                    tri_1.setAutoDraw(False)
            
            # *circ_1* updates
            if circ_1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_1.frameNStart = frameN  # exact frame index
                circ_1.tStart = t  # local t and not account for scr refresh
                circ_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_1, 'tStartRefresh')  # time at next scr refresh
                circ_1.setAutoDraw(True)
            if circ_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_1.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_1.tStop = t  # not accounting for scr refresh
                    circ_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_1, 'tStopRefresh')  # time at next scr refresh
                    circ_1.setAutoDraw(False)
            
            # *rect_noChng* updates
            if rect_noChng.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                rect_noChng.frameNStart = frameN  # exact frame index
                rect_noChng.tStart = t  # local t and not account for scr refresh
                rect_noChng.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_noChng, 'tStartRefresh')  # time at next scr refresh
                rect_noChng.setAutoDraw(True)
            
            # *tri_noChng* updates
            if tri_noChng.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                tri_noChng.frameNStart = frameN  # exact frame index
                tri_noChng.tStart = t  # local t and not account for scr refresh
                tri_noChng.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_noChng, 'tStartRefresh')  # time at next scr refresh
                tri_noChng.setAutoDraw(True)
            
            # *circ_noChng* updates
            if circ_noChng.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                circ_noChng.frameNStart = frameN  # exact frame index
                circ_noChng.tStart = t  # local t and not account for scr refresh
                circ_noChng.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_noChng, 'tStartRefresh')  # time at next scr refresh
                circ_noChng.setAutoDraw(True)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['c', 'n'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NoMask3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "NoMask3"-------
        for thisComponent in NoMask3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        noChangeT.addData('fixation_noChng.started', fixation_noChng.tStartRefresh)
        noChangeT.addData('fixation_noChng.stopped', fixation_noChng.tStopRefresh)
        noChangeT.addData('rect_1.started', rect_1.tStartRefresh)
        noChangeT.addData('rect_1.stopped', rect_1.tStopRefresh)
        noChangeT.addData('tri_1.started', tri_1.tStartRefresh)
        noChangeT.addData('tri_1.stopped', tri_1.tStopRefresh)
        noChangeT.addData('circ_1.started', circ_1.tStartRefresh)
        noChangeT.addData('circ_1.stopped', circ_1.tStopRefresh)
        noChangeT.addData('rect_noChng.started', rect_noChng.tStartRefresh)
        noChangeT.addData('rect_noChng.stopped', rect_noChng.tStopRefresh)
        noChangeT.addData('tri_noChng.started', tri_noChng.tStartRefresh)
        noChangeT.addData('tri_noChng.stopped', tri_noChng.tStopRefresh)
        noChangeT.addData('circ_noChng.started', circ_noChng.tStartRefresh)
        noChangeT.addData('circ_noChng.stopped', circ_noChng.tStopRefresh)
        noChangeT.addData('text.started', text.tStartRefresh)
        noChangeT.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        noChangeT.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            noChangeT.addData('key_resp_3.rt', key_resp_3.rt)
        noChangeT.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        noChangeT.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "NoMask3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed NoChangeT repeats of 'noChangeT'
    
    
    # set up handler to look after randomisation of conditions etc
    noChangeF = data.TrialHandler(nReps=NoChangeF, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='noChangeF')
    thisExp.addLoop(noChangeF)  # add the loop to the experiment
    thisNoChangeF = noChangeF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNoChangeF.rgb)
    if thisNoChangeF != None:
        for paramName in thisNoChangeF:
            exec('{} = thisNoChangeF[paramName]'.format(paramName))
    
    for thisNoChangeF in noChangeF:
        currentLoop = noChangeF
        # abbreviate parameter names if possible (e.g. rgb = thisNoChangeF.rgb)
        if thisNoChangeF != None:
            for paramName in thisNoChangeF:
                exec('{} = thisNoChangeF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "NoMask5"-------
        continueRoutine = True
        # update component parameters for each repeat
        colors = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [0,1,1]]
        shuffle(colors)
        
        if colors[0] == colors[1]:
            shuffle(colors)
        if colors[0] == colors[2]:
            shuffle(colors)
        if colors[0] == colors[3]:
            shuffle(colors)
        if colors[0] == colors[4]:
            shuffle(colors)
        if colors[1] == colors[2]:
            shuffle(colors)
        if colors[1] == colors[3]:
            shuffle(colors)
        if colors[1] == colors[4]:
            shuffle(colors)
        if colors[2] == colors[3]:
            shuffle(colors)
        if colors[2] == colors[4]:
            shuffle(colors)
        if colors[3] == colors[4]:
            shuffle(colors)
        positions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5), (-9,9), (-9,0), (-9,-9), (0,9), (0,9), (9,0), (9,9), (9,-9), (9,-9)]
        shuffle(positions)
        
        if positions[0] == positions[1]:
            shuffle(positions)
        if positions[0] == positions[2]:
            shuffle(positions)
        if positions[0] == positions[3]:
            shuffle(positions)
        if positions[0] == positions[4]:
            shuffle(positions)
        if positions[1] == positions[2]:
            shuffle(positions)
        if positions[1] == positions[3]:
            shuffle(positions)
        if positions[1] == positions[4]:
            shuffle(positions)
        if positions[2] == positions[3]:
            shuffle(positions)
        if positions[2] == positions[4]:
            shuffle(positions)
        if positions[3] == positions[4]:
            shuffle(positions)
        
        newPositions = [(-5,5), (-5,0), (-5, -5), (0,5), (0,0), (0,5), (5,0), (5,5,), (5,-5)]
        if newPositions[0] == positions[0]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[1]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[2]:
            newPositions[0] = positions[4]
        if newPositions[0] == positions[3]:
            newPositions[0] = positions[4]
        if newPositions[0] == newPositions[1]:
            newPositions[0] = positions[4]
            
        if newPositions[1] == positions[0]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[1]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[2]:
            newPositions[1] = positions[1]
        if newPositions[1] == positions[3]:
            newPositions[1] = positions[1]
        if newPositions[1] == newPositions[0]:
            newPositions[1] = positions[1]
        
        rect_NC5.setPos(positions[0])
        rect_NC5.setFillColor(colors[0])
        rect_NC5.setLineColor([1,1,1])
        tri_NC5.setPos(positions[1])
        tri_NC5.setFillColor(colors[1])
        tri_NC5.setLineColor([1,1,1])
        circ_NC5.setPos(positions[2])
        circ_NC5.setFillColor(colors[2])
        circ_NC5.setLineColor([1,1,1])
        oct_NC5.setPos(positions[3])
        oct_NC5.setFillColor(colors[3])
        oct_NC5.setLineColor([1,1,1])
        star_NC5.setPos(positions[4])
        star_NC5.setFillColor(colors[4])
        star_NC5.setLineColor([1,1,1])
        rect_NC.setPos(positions[0])
        rect_NC.setFillColor(colors[0])
        rect_NC.setLineColor([1,1,1])
        tri_NC.setPos(positions[1])
        tri_NC.setFillColor(colors[1])
        tri_NC.setLineColor([1,1,1])
        circ_NC.setPos(positions[2])
        circ_NC.setFillColor(colors[2])
        circ_NC.setLineColor([1,1,1])
        oct_NC.setPos(newPositions[0])
        oct_NC.setFillColor(colors[3])
        oct_NC.setLineColor([1,1,1])
        star_NC.setPos(newPositions[1])
        star_NC.setFillColor(colors[4])
        star_NC.setLineColor([1,1,1])
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        NoMask5Components = [fix_noChng5, rect_NC5, tri_NC5, circ_NC5, oct_NC5, star_NC5, rect_NC, tri_NC, circ_NC, oct_NC, star_NC, text_3, key_resp_4]
        for thisComponent in NoMask5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NoMask5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "NoMask5"-------
        while continueRoutine:
            # get current time
            t = NoMask5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NoMask5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_noChng5* updates
            if fix_noChng5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_noChng5.frameNStart = frameN  # exact frame index
                fix_noChng5.tStart = t  # local t and not account for scr refresh
                fix_noChng5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_noChng5, 'tStartRefresh')  # time at next scr refresh
                fix_noChng5.setAutoDraw(True)
            if fix_noChng5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_noChng5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_noChng5.tStop = t  # not accounting for scr refresh
                    fix_noChng5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_noChng5, 'tStopRefresh')  # time at next scr refresh
                    fix_noChng5.setAutoDraw(False)
            
            # *rect_NC5* updates
            if rect_NC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                rect_NC5.frameNStart = frameN  # exact frame index
                rect_NC5.tStart = t  # local t and not account for scr refresh
                rect_NC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_NC5, 'tStartRefresh')  # time at next scr refresh
                rect_NC5.setAutoDraw(True)
            if rect_NC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_NC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_NC5.tStop = t  # not accounting for scr refresh
                    rect_NC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rect_NC5, 'tStopRefresh')  # time at next scr refresh
                    rect_NC5.setAutoDraw(False)
            
            # *tri_NC5* updates
            if tri_NC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tri_NC5.frameNStart = frameN  # exact frame index
                tri_NC5.tStart = t  # local t and not account for scr refresh
                tri_NC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_NC5, 'tStartRefresh')  # time at next scr refresh
                tri_NC5.setAutoDraw(True)
            if tri_NC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tri_NC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tri_NC5.tStop = t  # not accounting for scr refresh
                    tri_NC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tri_NC5, 'tStopRefresh')  # time at next scr refresh
                    tri_NC5.setAutoDraw(False)
            
            # *circ_NC5* updates
            if circ_NC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                circ_NC5.frameNStart = frameN  # exact frame index
                circ_NC5.tStart = t  # local t and not account for scr refresh
                circ_NC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_NC5, 'tStartRefresh')  # time at next scr refresh
                circ_NC5.setAutoDraw(True)
            if circ_NC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circ_NC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circ_NC5.tStop = t  # not accounting for scr refresh
                    circ_NC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circ_NC5, 'tStopRefresh')  # time at next scr refresh
                    circ_NC5.setAutoDraw(False)
            
            # *oct_NC5* updates
            if oct_NC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                oct_NC5.frameNStart = frameN  # exact frame index
                oct_NC5.tStart = t  # local t and not account for scr refresh
                oct_NC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(oct_NC5, 'tStartRefresh')  # time at next scr refresh
                oct_NC5.setAutoDraw(True)
            if oct_NC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > oct_NC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    oct_NC5.tStop = t  # not accounting for scr refresh
                    oct_NC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(oct_NC5, 'tStopRefresh')  # time at next scr refresh
                    oct_NC5.setAutoDraw(False)
            
            # *star_NC5* updates
            if star_NC5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                star_NC5.frameNStart = frameN  # exact frame index
                star_NC5.tStart = t  # local t and not account for scr refresh
                star_NC5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_NC5, 'tStartRefresh')  # time at next scr refresh
                star_NC5.setAutoDraw(True)
            if star_NC5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_NC5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    star_NC5.tStop = t  # not accounting for scr refresh
                    star_NC5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_NC5, 'tStopRefresh')  # time at next scr refresh
                    star_NC5.setAutoDraw(False)
            
            # *rect_NC* updates
            if rect_NC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                rect_NC.frameNStart = frameN  # exact frame index
                rect_NC.tStart = t  # local t and not account for scr refresh
                rect_NC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_NC, 'tStartRefresh')  # time at next scr refresh
                rect_NC.setAutoDraw(True)
            
            # *tri_NC* updates
            if tri_NC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                tri_NC.frameNStart = frameN  # exact frame index
                tri_NC.tStart = t  # local t and not account for scr refresh
                tri_NC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tri_NC, 'tStartRefresh')  # time at next scr refresh
                tri_NC.setAutoDraw(True)
            
            # *circ_NC* updates
            if circ_NC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                circ_NC.frameNStart = frameN  # exact frame index
                circ_NC.tStart = t  # local t and not account for scr refresh
                circ_NC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circ_NC, 'tStartRefresh')  # time at next scr refresh
                circ_NC.setAutoDraw(True)
            
            # *oct_NC* updates
            if oct_NC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                oct_NC.frameNStart = frameN  # exact frame index
                oct_NC.tStart = t  # local t and not account for scr refresh
                oct_NC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(oct_NC, 'tStartRefresh')  # time at next scr refresh
                oct_NC.setAutoDraw(True)
            
            # *star_NC* updates
            if star_NC.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                star_NC.frameNStart = frameN  # exact frame index
                star_NC.tStart = t  # local t and not account for scr refresh
                star_NC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_NC, 'tStartRefresh')  # time at next scr refresh
                star_NC.setAutoDraw(True)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['c', 'n'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NoMask5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "NoMask5"-------
        for thisComponent in NoMask5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        noChangeF.addData('fix_noChng5.started', fix_noChng5.tStartRefresh)
        noChangeF.addData('fix_noChng5.stopped', fix_noChng5.tStopRefresh)
        noChangeF.addData('rect_NC5.started', rect_NC5.tStartRefresh)
        noChangeF.addData('rect_NC5.stopped', rect_NC5.tStopRefresh)
        noChangeF.addData('tri_NC5.started', tri_NC5.tStartRefresh)
        noChangeF.addData('tri_NC5.stopped', tri_NC5.tStopRefresh)
        noChangeF.addData('circ_NC5.started', circ_NC5.tStartRefresh)
        noChangeF.addData('circ_NC5.stopped', circ_NC5.tStopRefresh)
        noChangeF.addData('oct_NC5.started', oct_NC5.tStartRefresh)
        noChangeF.addData('oct_NC5.stopped', oct_NC5.tStopRefresh)
        noChangeF.addData('star_NC5.started', star_NC5.tStartRefresh)
        noChangeF.addData('star_NC5.stopped', star_NC5.tStopRefresh)
        noChangeF.addData('rect_NC.started', rect_NC.tStartRefresh)
        noChangeF.addData('rect_NC.stopped', rect_NC.tStopRefresh)
        noChangeF.addData('tri_NC.started', tri_NC.tStartRefresh)
        noChangeF.addData('tri_NC.stopped', tri_NC.tStopRefresh)
        noChangeF.addData('circ_NC.started', circ_NC.tStartRefresh)
        noChangeF.addData('circ_NC.stopped', circ_NC.tStopRefresh)
        noChangeF.addData('oct_NC.started', oct_NC.tStartRefresh)
        noChangeF.addData('oct_NC.stopped', oct_NC.tStopRefresh)
        noChangeF.addData('star_NC.started', star_NC.tStartRefresh)
        noChangeF.addData('star_NC.stopped', star_NC.tStopRefresh)
        noChangeF.addData('text_3.started', text_3.tStartRefresh)
        noChangeF.addData('text_3.stopped', text_3.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        noChangeF.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            noChangeF.addData('key_resp_4.rt', key_resp_4.rt)
        noChangeF.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        noChangeF.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "NoMask5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed NoChangeF repeats of 'noChangeF'
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'randomize'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
