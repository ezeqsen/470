import time;
x=0;  #initial value
y=1;   #initial value
while (x<10 and y==1):    #requires user input so less 
	tst=time.time();
	x+=1;
	print (x,"seconds");
	tsp=time.time();
	y=int(input("Enter 1 to continue: "));
	time.sleep(0.2-(tsp-tst));   #0.2 secs minues time of processes

