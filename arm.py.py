#Arturo Senzano
#Base of the arm is on wheels. This allows for movement along the x axis only
#First bar of arm is 20 cm (center of motion to center of motion).  
#Movement is from 0 degrees to 180 degrees
#Second bar of arm is 20 cm long (center of motion to end-effector).  
#Movement if from 0 degrees to 180 degrees
#Wheel radius is 3 cm.
#Starting origin for arm is x=30, y=36, angle of bar A=40, angle of bar B=60
import math
WR=int(input("Enter number of wheel rotations (negative left, positive right):  "));
#allows user to enter the number of rotations of the wheel either to the left or right.
BAA=int(input("Enter the angle in degrees bar A:   "));
BBA=int(input("Enter the angle in degrees bar B:   "));
#calculating the position of the end factor in the x,y coordinates
WRx=WR*(2*3.1416*3);        #The movement of the wheels
BAAr=math.radians(BAA+50);  #converts angle of bar A to radians
BAAx=20*(math.cos(BAAr));   #gives the x distance of bar A
BBAr=math.radians(BBA+30);  #converts angle of bar B
BBAx=20*(math.cos(BBAr));   #gives the x distance of bar B
x=WRx+BAAx+BBAx;         #sum of the changes cause by each DOF
BAAy=20*(math.sin(BAAr));   #gives the y distance of bar A
BBAy=20*(math.sin(BBAr));   #gives the y distance of bar B
y=12+BAAy+BBAy;              #sum of changes cause by each DOF
print ("Current position after movement is x-coord:",x," y-coord:", y);
