import time;
x=0;   #starting value
while (x<50):
	tst=time.time();
	x+=1;
	print(x, "seconds");
	tsp=time.time();
	time.sleep(0.2-(tsp-tst));  #0.2 sec or 5Hz minus the time of the processes

