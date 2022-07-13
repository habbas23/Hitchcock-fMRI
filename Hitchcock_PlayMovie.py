#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on October 05, 2021, at 16:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'Hitchcock_Key_Press'  # from the Builder filename that created this script
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
    originPath='smb:\\localhost\\Google Drive\\My Drive\\UWO\\psychopy_Hitchcock\\Hitchcock_PlayMovie1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Set volume by pressing a number key:\n1 - 100%\n4 - 40%',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
key_resp_vol = keyboard.Keyboard()

# Initialize components for Routine "volume_feedback"
volume_feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
playback_volume = 1.0
dict_keypress_to_volume = {
'1': 1.0,
'4': 0.4}
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "scanner_TR"
scanner_TRClock = core.Clock()
scanner_F = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
total_dummy = 6
curr_dummy = 0
countdown_msg = f'dummy scans remaining: {total_dummy - curr_dummy}'

# Initialize components for Routine "movie"
movieClock = core.Clock()
hitchcock_video = visual.MovieStim3(
    win=win, name='hitchcock_video',
    noAudio = True,
    filename='BangBang.mov',
    ori=0.0, pos=(0, 0), opacity=0.0,
    loop=False,
    depth=0.0,
    )
hitchcock_sound = sound.Sound('BangBang.wav', secs=-1, stereo=True, hamming=True,
    name='hitchcock_sound')
hitchcock_sound.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# set up handler to look after randomisation of conditions etc
set_volume_loops = data.TrialHandler(nReps=5.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='set_volume_loops')
thisExp.addLoop(set_volume_loops)  # add the loop to the experiment
thisSet_volume_loop = set_volume_loops.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSet_volume_loop.rgb)
if thisSet_volume_loop != None:
    for paramName in thisSet_volume_loop:
        exec('{} = thisSet_volume_loop[paramName]'.format(paramName))

for thisSet_volume_loop in set_volume_loops:
    currentLoop = set_volume_loops
    # abbreviate parameter names if possible (e.g. rgb = thisSet_volume_loop.rgb)
    if thisSet_volume_loop != None:
        for paramName in thisSet_volume_loop:
            exec('{} = thisSet_volume_loop[paramName]'.format(paramName))

    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_vol.keys = []
    key_resp_vol.rt = []
    _key_resp_vol_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [text, key_resp_vol]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)

        # *key_resp_vol* updates
        waitOnFlip = False
        if key_resp_vol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_vol.frameNStart = frameN  # exact frame index
            key_resp_vol.tStart = t  # local t and not account for scr refresh
            key_resp_vol.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_vol, 'tStartRefresh')  # time at next scr refresh
            key_resp_vol.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_vol.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_vol.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_vol.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_vol.getKeys(keyList=None, waitRelease=False)
            _key_resp_vol_allKeys.extend(theseKeys)
            if len(_key_resp_vol_allKeys):
                key_resp_vol.keys = _key_resp_vol_allKeys[-1].name  # just the last key pressed
                key_resp_vol.rt = _key_resp_vol_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    set_volume_loops.addData('text.started', text.tStartRefresh)
    set_volume_loops.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp_vol.keys in ['', [], None]:  # No response was made
        key_resp_vol.keys = None
    set_volume_loops.addData('key_resp_vol.keys',key_resp_vol.keys)
    if key_resp_vol.keys != None:  # we had a response
        set_volume_loops.addData('key_resp_vol.rt', key_resp_vol.rt)
    set_volume_loops.addData('key_resp_vol.started', key_resp_vol.tStartRefresh)
    set_volume_loops.addData('key_resp_vol.stopped', key_resp_vol.tStopRefresh)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "volume_feedback"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    key_pressed = key_resp_vol.keys[0]
    if key_pressed in dict_keypress_to_volume.keys():
        playback_volume = dict_keypress_to_volume[key_pressed]
        set_volume_loops.finished = True
        msg=f'Setting volume to {playback_volume*100:01}%'
    else:
        msg="Incorrect key: use number keys to set volume"
    text_2.setText(msg)
    # keep track of which components have finished
    volume_feedbackComponents = [text_2]
    for thisComponent in volume_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    volume_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "volume_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = volume_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=volume_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in volume_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "volume_feedback"-------
    for thisComponent in volume_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    set_volume_loops.addData('text_2.started', text_2.tStartRefresh)
    set_volume_loops.addData('text_2.stopped', text_2.tStopRefresh)
# completed 5.0 repeats of 'set_volume_loops'

# set up handler to look after randomisation of conditions etc
dummy = data.TrialHandler(nReps=asarray(total_dummy), method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='dummy')
thisExp.addLoop(dummy)  # add the loop to the experiment
thisDummy = dummy.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDummy.rgb)
if thisDummy != None:
    for paramName in thisDummy:
        exec('{} = thisDummy[paramName]'.format(paramName))

for thisDummy in dummy:
    currentLoop = dummy
    # abbreviate parameter names if possible (e.g. rgb = thisDummy.rgb)
    if thisDummy != None:
        for paramName in thisDummy:
            exec('{} = thisDummy[paramName]'.format(paramName))

    # ------Prepare to start Routine "scanner_TR"-------
    continueRoutine = True
    # update component parameters for each repeat
    scanner_F.keys = []
    scanner_F.rt = []
    _scanner_F_allKeys = []
    text_4.setText(countdown_msg)
    # keep track of which components have finished
    scanner_TRComponents = [scanner_F, text_4]
    for thisComponent in scanner_TRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    scanner_TRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "scanner_TR"-------
    while continueRoutine:
        # get current time
        t = scanner_TRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=scanner_TRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *scanner_F* updates
        waitOnFlip = False
        if scanner_F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scanner_F.frameNStart = frameN  # exact frame index
            scanner_F.tStart = t  # local t and not account for scr refresh
            scanner_F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scanner_F, 'tStartRefresh')  # time at next scr refresh
            scanner_F.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(scanner_F.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(scanner_F.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if scanner_F.status == STARTED and not waitOnFlip:
            theseKeys = scanner_F.getKeys(keyList=['5'], waitRelease=False)
            _scanner_F_allKeys.extend(theseKeys)
            if len(_scanner_F_allKeys):
                scanner_F.keys = _scanner_F_allKeys[-1].name  # just the last key pressed
                scanner_F.rt = _scanner_F_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scanner_TRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

  # -------Ending Routine "scanner_TR"-------
    for thisComponent in scanner_TRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if scanner_F.keys in ['', [], None]:  # No response was made
        scanner_F.keys = None
    dummy.addData('scanner_F.keys',scanner_F.keys)
    if scanner_F.keys != None:  # we had a response
        dummy.addData('scanner_F.rt', scanner_F.rt)
    dummy.addData('scanner_F.started', scanner_F.tStartRefresh)
    dummy.addData('scanner_F.stopped', scanner_F.tStopRefresh)
    dummy.addData('text_4.started', text_4.tStartRefresh)
    dummy.addData('text_4.stopped', text_4.tStopRefresh)
    # the Routine "scanner_TR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "countdown"-------
    continueRoutine = True
    # update component parameters for each repeat
    curr_dummy = curr_dummy + 1
    if curr_dummy <= total_dummy:
        countdown_msg = f'dummy scans remaining: {total_dummy - curr_dummy}'

    # keep track of which components have finished
    countdownComponents = []
    for thisComponent in countdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "countdown"-------
    while continueRoutine:
        # get current time
        t = countdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "countdown"-------
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "countdown" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# ------Prepare to start Routine "movie"-------
continueRoutine = True
# update component parameters for each repeat
hitchcock_sound.setSound('BangBang.wav', hamming=True)
hitchcock_sound.setVolume(asarray(playback_volume), log=False)
# keep track of which components have finished
movieComponents = [hitchcock_video, hitchcock_sound]
for thisComponent in movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
movieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "movie"-------
while continueRoutine:
    # get current time
    t = movieClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=movieClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *hitchcock_video* updates
    if hitchcock_video.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hitchcock_video.frameNStart = frameN  # exact frame index
        hitchcock_video.tStart = t  # local t and not account for scr refresh
        hitchcock_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hitchcock_video, 'tStartRefresh')  # time at next scr refresh
        hitchcock_video.setAutoDraw(True)
    # start/stop hitchcock_sound
    if hitchcock_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hitchcock_sound.frameNStart = frameN  # exact frame index
        hitchcock_sound.tStart = t  # local t and not account for scr refresh
        hitchcock_sound.tStartRefresh = tThisFlipGlobal  # on global time
        hitchcock_sound.play(when=win)  # sync with win flip

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "movie"-------
for thisComponent in movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
hitchcock_video.stop()
hitchcock_sound.stop()  # ensure sound has stopped at end of routine
thisExp.addData('hitchcock_sound.started', hitchcock_sound.tStartRefresh)
thisExp.addData('hitchcock_sound.stopped', hitchcock_sound.tStopRefresh)
# the Routine "movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
