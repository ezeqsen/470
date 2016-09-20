import hubo_ach as ha
import ach
import sys
import time 
from ctypes import *
import math


s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)

state = ha.HUBO_STATE()
ref = ha.HUBO_REF()

[statuss, framesizes]=s.get(state, wait=True, last=False)
one=True;
s.get(state);
tick1=state.time
while (one==True):
	ref.ref[ha.RHP]=-.8;
	ref.ref[ha.LHP]=-.8;
	ref.ref[ha.RKN]=1.6;
	ref.ref[ha.LKN]=1.6;
	ref.ref[ha.RAP]=-.8;
	ref.ref[ha.LAP]=-.8;
	r.put(ref)
	s.get(state)
	if ((state.time-tick1)>1.2):
		one=False;
two=True;
s.get(state);
tick2=state.time;
print(state.time);
while (two==True):
	ref.ref[ha.RHR]=-.2;
	ref.ref[ha.LHR]=-.2;
	ref.ref[ha.RAR]=.2;
	ref.ref[ha.LAR]=.2;
	r.put(ref);
	s.get(state);
	if ((state.time-tick2)>4):
		two=False;
three=True;
s.get(state);
tick3=state.time;
print(state.time);
while (three==True):
	ref.ref[ha.LHR]=-.3;
	ref.ref[ha.LAR]=.3;
	ref.ref[ha.RHP]=-1.4;
	ref.ref[ha.RKN]=1.6;
	ref.ref[ha.RAP]=-.3;
	r.put(ref);
	s.get(state);
	if ((state.time-tick3)>1):
		three=False;
four=True;
s.get(state);
tick4=state.time;
print(state.time);
while (four==True):
	ref.ref[ha.RHP]=-1.4;
	ref.ref[ha.RPH]=-.3;
	ref.ref[ha.RKN]=1.6;
	ref.ref[ha.LPH]=-.3;
	ref.ref[ha.RAP]=-0;
	#ref.ref[ha.LAP]=1;
	r.put(ref);
	s.get(state);
	if ((state.time-tick4)>1.2):
		four=False;

r.close()
s.close()
