#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on August 17, 2021, at 11:56
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
    originPath='smb:\\localhost\\Google Drive\\My Drive\\UWO\\psychopy_Hitchcock\\Hitchcock_SoundCheck.py',
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

# Initialize components for Routine "play_sound"
play_soundClock = core.Clock()
hitchcock_sound = sound.Sound('TestClip.wav', secs=-1.0, stereo=True, hamming=True,
    name='hitchcock_sound')
hitchcock_sound.setVolume(1.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Set volume by pressing a number key:\n1: 100%, 4: 40%\n\nPress space to finish soundcheck',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
key_resp_vol = keyboard.Keyboard()

# Initialize components for Routine "volume_feedback"
volume_feedbackClock = core.Clock()
#msg variable just needs some value at start
playback_volume = 1.0
msg=f'Playing sound at {playback_volume*100:01}%'
dict_keypress_to_volume = {
'1': 1.0,
'4': 0.4}

# Initialize components for Routine "final"
finalClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);

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

    # ------Prepare to start Routine "play_sound"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    hitchcock_sound.setSound('TestClip.wav', secs=6.0, hamming=True)
    hitchcock_sound.setVolume(asarray(playback_volume), log=False)
    text_3.setText(msg)
    # keep track of which components have finished
    play_soundComponents = [hitchcock_sound, text_3]
    for thisComponent in play_soundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    play_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "play_sound"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = play_soundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=play_soundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop hitchcock_sound
        if hitchcock_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hitchcock_sound.frameNStart = frameN  # exact frame index
            hitchcock_sound.tStart = t  # local t and not account for scr refresh
            hitchcock_sound.tStartRefresh = tThisFlipGlobal  # on global time
            hitchcock_sound.play(when=win)  # sync with win flip
        if hitchcock_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hitchcock_sound.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                hitchcock_sound.tStop = t  # not accounting for scr refresh
                hitchcock_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hitchcock_sound, 'tStopRefresh')  # time at next scr refresh
                hitchcock_sound.stop()

        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in play_soundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "play_sound"-------
    for thisComponent in play_soundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    hitchcock_sound.stop()  # ensure sound has stopped at end of routine
    set_volume_loops.addData('hitchcock_sound.started', hitchcock_sound.tStartRefresh)
    set_volume_loops.addData('hitchcock_sound.stopped', hitchcock_sound.tStopRefresh)
    set_volume_loops.addData('text_3.started', text_3.tStartRefresh)
    set_volume_loops.addData('text_3.stopped', text_3.tStopRefresh)

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
    # update component parameters for each repeat
    key_pressed = key_resp_vol.keys[0]
    if key_pressed in dict_keypress_to_volume.keys():
        playback_volume = dict_keypress_to_volume[key_pressed]
        msg=f'Playing sound at {playback_volume*100:01}%'
    else:
        set_volume_loops.finished = True
        msg=f"Quitting soundcheck, last volume: {playback_volume*100:01}%"
    # keep track of which components have finished
    volume_feedbackComponents = []
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
    while continueRoutine:
        # get current time
        t = volume_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=volume_feedbackClock)
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
    # the Routine "volume_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5.0 repeats of 'set_volume_loops'


# ------Prepare to start Routine "final"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
text_2.setText(msg)
# keep track of which components have finished
finalComponents = [text_2]
for thisComponent in finalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalClock)
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
        if tThisFlipGlobal > text_2.tStartRefresh + 5.0-frameTolerance:
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
    for thisComponent in finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final"-------
for thisComponent in finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

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
