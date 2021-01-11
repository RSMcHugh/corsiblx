/****************** 
 * Corsi (1) Test *
 ******************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'corsi (1)';  // from the Builder filename that created this script
let expInfo = {'session': '001', 'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(Thank_youRoutineBegin());
flowScheduler.add(Thank_youRoutineEachFrame());
flowScheduler.add(Thank_youRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionsClock;
var Instructions_Start;
var key_resp_2;
var ISIClock;
var fixCross;
var trialClock;
var blk1;
var blk2;
var blk3;
var blk4;
var blk5;
var blk6;
var blk7;
var blk8;
var blk9;
var mouse;
var Thank_youClock;
var Thankyou;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  Instructions_Start = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions_Start',
    text: 'Hello, this is the memory maze task! During this task pay attention to the order of the boxes flashing on screen and then try to remember the order and click on the boxes that flashed on your computer screen. This will become increasingly difficult with each attempt and very few people get all sequences correct so don’t worry if you can’t remember! Please press the space bar to begin a practice trial. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  fixCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  blk1 = new visual.Rect ({
    win: psychoJS.window, name: 'blk1', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [(- 11.475), 9.4],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  blk2 = new visual.Rect ({
    win: psychoJS.window, name: 'blk2', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [(- 1.85), 11.4],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  blk3 = new visual.Rect ({
    win: psychoJS.window, name: 'blk3', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [16.84, 5.4],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  blk4 = new visual.Rect ({
    win: psychoJS.window, name: 'blk4', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [5.475, 5.4],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  blk5 = new visual.Rect ({
    win: psychoJS.window, name: 'blk5', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [(- 5.475), 1.8],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  blk6 = new visual.Rect ({
    win: psychoJS.window, name: 'blk6', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [(- 16.85), 1.8],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  blk7 = new visual.Rect ({
    win: psychoJS.window, name: 'blk7', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [6.85, (- 4.8)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  blk8 = new visual.Rect ({
    win: psychoJS.window, name: 'blk8', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [1.475, (- 2.8)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  blk9 = new visual.Rect ({
    win: psychoJS.window, name: 'blk9', units : 'height', 
    width: [3.39, 3.21][0], height: [3.39, 3.21][1],
    ori: 0, pos: [(- 12.475), (- 6.8)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Thank_you"
  Thank_youClock = new util.Clock();
  Thankyou = new visual.TextStim({
    win: psychoJS.window,
    name: 'Thankyou',
    text: 'End text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_2_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(Instructions_Start);
    instructionsComponents.push(key_resp_2);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instructions_Start* updates
    if (t >= 0.0 && Instructions_Start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_Start.tStart = t;  // (not accounting for frame time here)
      Instructions_Start.frameNStart = frameN;  // exact frame index
      
      Instructions_Start.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions'-------
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'conditions (2).xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(ISIRoutineBegin(snapshot));
    trialsLoopScheduler.add(ISIRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(ISIRoutineEnd(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var ISIComponents;
function ISIRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ISI'-------
    t = 0;
    ISIClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.600000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(fixCross);
    
    ISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function ISIRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ISI'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixCross* updates
    if (t >= 0.0 && fixCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixCross.tStart = t;  // (not accounting for frame time here)
      fixCross.frameNStart = frameN;  // exact frame index
      
      fixCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixCross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixCross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ISI'-------
    ISIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(blk1);
    trialComponents.push(blk2);
    trialComponents.push(blk3);
    trialComponents.push(blk4);
    trialComponents.push(blk5);
    trialComponents.push(blk6);
    trialComponents.push(blk7);
    trialComponents.push(blk8);
    trialComponents.push(blk9);
    trialComponents.push(mouse);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blk1* updates
    if (t >= 0.0 && blk1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk1.tStart = t;  // (not accounting for frame time here)
      blk1.frameNStart = frameN;  // exact frame index
      
      blk1.setAutoDraw(true);
    }

    
    // *blk2* updates
    if (t >= 0.0 && blk2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk2.tStart = t;  // (not accounting for frame time here)
      blk2.frameNStart = frameN;  // exact frame index
      
      blk2.setAutoDraw(true);
    }

    
    // *blk3* updates
    if (t >= 0.0 && blk3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk3.tStart = t;  // (not accounting for frame time here)
      blk3.frameNStart = frameN;  // exact frame index
      
      blk3.setAutoDraw(true);
    }

    
    // *blk4* updates
    if (t >= 0.0 && blk4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk4.tStart = t;  // (not accounting for frame time here)
      blk4.frameNStart = frameN;  // exact frame index
      
      blk4.setAutoDraw(true);
    }

    
    // *blk5* updates
    if (t >= 0.0 && blk5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk5.tStart = t;  // (not accounting for frame time here)
      blk5.frameNStart = frameN;  // exact frame index
      
      blk5.setAutoDraw(true);
    }

    
    // *blk6* updates
    if (t >= 0.0 && blk6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk6.tStart = t;  // (not accounting for frame time here)
      blk6.frameNStart = frameN;  // exact frame index
      
      blk6.setAutoDraw(true);
    }

    
    // *blk7* updates
    if (t >= 0.0 && blk7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk7.tStart = t;  // (not accounting for frame time here)
      blk7.frameNStart = frameN;  // exact frame index
      
      blk7.setAutoDraw(true);
    }

    
    // *blk8* updates
    if (t >= 0.0 && blk8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk8.tStart = t;  // (not accounting for frame time here)
      blk8.frameNStart = frameN;  // exact frame index
      
      blk8.setAutoDraw(true);
    }

    
    // *blk9* updates
    if (t >= 0.0 && blk9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blk9.tStart = t;  // (not accounting for frame time here)
      blk9.frameNStart = frameN;  // exact frame index
      
      blk9.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= doingResponse && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [blk1, blk2, blk3, blk4, blk5, blk6, blk7, blk8, blk9]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Thank_youComponents;
function Thank_youRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Thank_you'-------
    t = 0;
    Thank_youClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Thank_youComponents = [];
    Thank_youComponents.push(Thankyou);
    
    Thank_youComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Thank_youRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Thank_you'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Thank_youClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Thankyou* updates
    if (t >= 0.0 && Thankyou.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Thankyou.tStart = t;  // (not accounting for frame time here)
      Thankyou.frameNStart = frameN;  // exact frame index
      
      Thankyou.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Thankyou.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Thankyou.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Thank_youComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Thank_youRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Thank_you'-------
    Thank_youComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
