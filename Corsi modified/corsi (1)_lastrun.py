#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on January 07, 2021, at 12:49
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
psychopyVersion = '2020.2.4'
expName = 'CorsiBlocksGrid'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='C:\\Users\\rmchugh\\Desktop\\Ellie Cullen_Maze_issue\\Ellie Cullen_Maze\\Corsi modified\\corsi (1)_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
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
Instructions_Start = visual.TextStim(win=win, name='Instructions_Start',
    text='Hello, this is the memory maze task! During this task pay attention to the order of the boxes flashing on screen and then try to remember the order and click on the boxes that flashed on your computer screen. This will become increasingly difficult with each attempt and very few people get all sequences correct so don’t worry if you can’t remember! Please press the space bar to begin a practice trial. \n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixCross = visual.TextStim(win=win, name='fixCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
blk1 = visual.Rect(
    win=win, name='blk1',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(-11.475,9.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
blk2 = visual.Rect(
    win=win, name='blk2',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(-1.85,11.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
blk3 = visual.Rect(
    win=win, name='blk3',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(16.84,5.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
blk4 = visual.Rect(
    win=win, name='blk4',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(5.475,5.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
blk5 = visual.Rect(
    win=win, name='blk5',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(-5.475,1.8),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
blk6 = visual.Rect(
    win=win, name='blk6',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(-16.85,1.8),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
blk7 = visual.Rect(
    win=win, name='blk7',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(6.85,-4.8),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
blk8 = visual.Rect(
    win=win, name='blk8',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(1.475,-2.8),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
blk9 = visual.Rect(
    win=win, name='blk9',units='cm', 
    width=(3.39,3.21)[0], height=(3.39,3.21)[1],
    ori=0, pos=(-12.475,-6.8),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "Thank_you"
Thank_youClock = core.Clock()
Thankyou = visual.TextStim(win=win, name='Thankyou',
    text='End text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instructionsComponents = [Instructions_Start, key_resp_2]
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
    
    # *Instructions_Start* updates
    if Instructions_Start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Start.frameNStart = frameN  # exact frame index
        Instructions_Start.tStart = t  # local t and not account for scr refresh
        Instructions_Start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Start, 'tStartRefresh')  # time at next scr refresh
        Instructions_Start.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
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
thisExp.addData('Instructions_Start.started', Instructions_Start.tStartRefresh)
thisExp.addData('Instructions_Start.stopped', Instructions_Start.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions (2).xlsx'),
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
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixCross]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixCross* updates
        if fixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross.frameNStart = frameN  # exact frame index
            fixCross.tStart = t  # local t and not account for scr refresh
            fixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
            fixCross.setAutoDraw(True)
        if fixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixCross.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                fixCross.tStop = t  # not accounting for scr refresh
                fixCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStopRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixCross.started', fixCross.tStartRefresh)
    trials.addData('fixCross.stopped', fixCross.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # initial state
    blkIndex = 0
    nextSwitch = blockDuration
    doingResponse = False
    currBlock = None
    
    # store blocks as a dictionary (to switch between name/object)
    blocks = {}
    blocks['blk1']=blk1
    blocks['blk2']=blk2
    blocks['blk3']=blk3
    blocks['blk4']=blk4
    blocks['blk5']=blk5
    blocks['blk6']=blk6
    blocks['blk7']=blk7
    blocks['blk8']=blk8
    blocks['blk9']=blk9
    
    for blockName in blocks:
        blocks[blockName].color="white"
    # keep track of which components have finished
    trialComponents = [blk1, blk2, blk3, blk4, blk5, blk6, blk7, blk8, blk9, mouse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blk1* updates
        if blk1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk1.frameNStart = frameN  # exact frame index
            blk1.tStart = t  # local t and not account for scr refresh
            blk1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk1, 'tStartRefresh')  # time at next scr refresh
            blk1.setAutoDraw(True)
        
        # *blk2* updates
        if blk2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk2.frameNStart = frameN  # exact frame index
            blk2.tStart = t  # local t and not account for scr refresh
            blk2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk2, 'tStartRefresh')  # time at next scr refresh
            blk2.setAutoDraw(True)
        
        # *blk3* updates
        if blk3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk3.frameNStart = frameN  # exact frame index
            blk3.tStart = t  # local t and not account for scr refresh
            blk3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk3, 'tStartRefresh')  # time at next scr refresh
            blk3.setAutoDraw(True)
        
        # *blk4* updates
        if blk4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk4.frameNStart = frameN  # exact frame index
            blk4.tStart = t  # local t and not account for scr refresh
            blk4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk4, 'tStartRefresh')  # time at next scr refresh
            blk4.setAutoDraw(True)
        
        # *blk5* updates
        if blk5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk5.frameNStart = frameN  # exact frame index
            blk5.tStart = t  # local t and not account for scr refresh
            blk5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk5, 'tStartRefresh')  # time at next scr refresh
            blk5.setAutoDraw(True)
        
        # *blk6* updates
        if blk6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk6.frameNStart = frameN  # exact frame index
            blk6.tStart = t  # local t and not account for scr refresh
            blk6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk6, 'tStartRefresh')  # time at next scr refresh
            blk6.setAutoDraw(True)
        
        # *blk7* updates
        if blk7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk7.frameNStart = frameN  # exact frame index
            blk7.tStart = t  # local t and not account for scr refresh
            blk7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk7, 'tStartRefresh')  # time at next scr refresh
            blk7.setAutoDraw(True)
        
        # *blk8* updates
        if blk8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk8.frameNStart = frameN  # exact frame index
            blk8.tStart = t  # local t and not account for scr refresh
            blk8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk8, 'tStartRefresh')  # time at next scr refresh
            blk8.setAutoDraw(True)
        
        # *blk9* updates
        if blk9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blk9.frameNStart = frameN  # exact frame index
            blk9.tStart = t  # local t and not account for scr refresh
            blk9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blk9, 'tStartRefresh')  # time at next scr refresh
            blk9.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= doingResponse-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [blk1, blk2, blk3, blk4, blk5, blk6, blk7, blk8, blk9]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        if not doingResponse and t > nextSwitch:
            if currBlock is not None:
                #reset color of current block
                currBlock.color = 'white'
        
            # then change current block and make that red
            if blkIndex >= len(sequence):
                doingResponse = True  # no more blocks to show
            else:
                currBlockName = sequence[blkIndex]
                currBlock = blocks[currBlockName]
                currBlock.color = 'red'
        
                # track time of this change
                nextSwitch += blockDuration
            blkIndex += 1
        
        # all clicked?
        if len(mouse.clicked_name) >= len(sequence):
            continueRoutine = False
        
        # update color of clicked
        for blockName in mouse.clicked_name:
            blocks[blockName].color = 'darkgrey'
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('blk1.started', blk1.tStartRefresh)
    trials.addData('blk1.stopped', blk1.tStopRefresh)
    trials.addData('blk2.started', blk2.tStartRefresh)
    trials.addData('blk2.stopped', blk2.tStopRefresh)
    trials.addData('blk3.started', blk3.tStartRefresh)
    trials.addData('blk3.stopped', blk3.tStopRefresh)
    trials.addData('blk4.started', blk4.tStartRefresh)
    trials.addData('blk4.stopped', blk4.tStopRefresh)
    trials.addData('blk5.started', blk5.tStartRefresh)
    trials.addData('blk5.stopped', blk5.tStopRefresh)
    trials.addData('blk6.started', blk6.tStartRefresh)
    trials.addData('blk6.stopped', blk6.tStopRefresh)
    trials.addData('blk7.started', blk7.tStartRefresh)
    trials.addData('blk7.stopped', blk7.tStopRefresh)
    trials.addData('blk8.started', blk8.tStartRefresh)
    trials.addData('blk8.stopped', blk8.tStopRefresh)
    trials.addData('blk9.started', blk9.tStartRefresh)
    trials.addData('blk9.stopped', blk9.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.clicked_name', mouse.clicked_name)
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Thank_you"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Thank_youComponents = [Thankyou]
for thisComponent in Thank_youComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Thank_youClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thank_you"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Thank_youClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Thank_youClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thankyou* updates
    if Thankyou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thankyou.frameNStart = frameN  # exact frame index
        Thankyou.tStart = t  # local t and not account for scr refresh
        Thankyou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thankyou, 'tStartRefresh')  # time at next scr refresh
        Thankyou.setAutoDraw(True)
    if Thankyou.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Thankyou.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Thankyou.tStop = t  # not accounting for scr refresh
            Thankyou.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Thankyou, 'tStopRefresh')  # time at next scr refresh
            Thankyou.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_you"-------
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Thankyou.started', Thankyou.tStartRefresh)
thisExp.addData('Thankyou.stopped', Thankyou.tStopRefresh)

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
