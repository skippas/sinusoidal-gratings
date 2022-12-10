import math
import numpy
from psychopy import visual, core, event, monitors

viewing_d= 186
stim_size= 100

angular_subtense= 2*math.degrees(math.atan(0.5*stim_size/viewing_d))

cpd= numpy.linspace(0.0,0.4,9)
cycles = cpd*angular_subtense
print(cycles)

cpp = cycles / 4000

# are these michelson contrasts?
contrasts = [0,0.02,0.04,0.06,0.08,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

#deg_p_cm= angular_subtense / (stim_size/10)
#cpcm= cpd / deg_p_cm
#print(cpp)

# use cpp to make the gratings
for conts, spfreq in [(conts,spfreq) for conts in contrasts for spfreq in cpp]:
    win0 = visual.Window([4000,4000], screen=0, fullscr=False, units='pix')
    grat_stim= visual.GratingStim(win= win0, tex='sin', mask='circle', units='pix', anchor='center',
    pos=(0.0, 0.0), size=4000, sf= spfreq, ori=0.0, phase=(0.0, 0.0), texRes=4096, rgb=None, dkl=None,
    lms=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', contrast= conts, opacity=None, depth=0,
    rgbPedestal=(0.0, 0.0, 0.0), interpolate=False, blendmode='avg', name=None, autoLog=None,
    autoDraw=False, maskParams=None)
    
    grat_stim.draw()
    win0.flip()
    win0.getMovieFrame()
    name = "C:\\Users\\User\\Desktop\\learnpy\\gratings\\grating_"+ str(conts) + '_' + str(spfreq)+ ".tif"
    win0.saveMovieFrames(name)
    core.wait(2)
    # tidy up
    win0.close()

# other options for generating gratings:
# - psychotoolbox
# twitter thread, making own raster images
# cedric vd berg make stimuli prog, he may have exp