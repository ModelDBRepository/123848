#!/usr/bin/python

import sys, string, os

def writecmd(comment):
    print 'Running: ', comment
    os.system('python sprout_run.py %s\n' % comment)
    
for sprout in [0.3, 0.4, 0.5, 0.6, 1]:
    cmd = 'sprout=%g' % sprout
    writecmd(cmd)
    cmd = 'Vhalfm=-4.2 Ah=0.9 sprout=%g' % sprout
    writecmd(cmd)
    cmd = 'Vhalfm=-4.2 sprout=%g' % sprout
    writecmd(cmd)

