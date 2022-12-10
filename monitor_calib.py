from psychopy import visual, core, event, monitors

mon = monitors.Monitor(name = 't480')
mon.setSizePix((1080,1920))
mon.setWidth(23.3934)

win0 = visual.Window(size=[10,10], screen=0, fullscr=False, units='cm', monitor = mon)

grat_stim= visual.GratingStim(win= win0, tex='sin', mask='circle', units='cm', anchor='center',
 pos=(0.0, 0.0), size=10, sf=1, ori=0.0, phase=(0.0, 0.0), texRes=1024, rgb=None, dkl=None,
  lms=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', contrast=1.0, opacity=None, depth=0,
   rgbPedestal=(0.0, 0.0, 0.0), interpolate=False, blendmode='avg', name=None, autoLog=None,
    autoDraw=False, maskParams=None)

grat_stim.draw()
win0.flip()
win0.getMovieFrame()
win0.saveMovieFrames("C:\\Users\\User\\Desktop\\learnpy\\gratings\\gratingNone.tif")

