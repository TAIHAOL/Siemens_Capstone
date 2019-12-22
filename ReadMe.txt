Problem Statement:Calculating Total Particle Volume in Large Particle Dispensing Silo Bins

Calculate Volume using Sensors

Build GUI to display Results

Store Data on Database

1.The team started with research of silos and general material behavior 
2.Next, the case of a silo with one mound was looked at with manually entered sample points 
3.A code was written in MATLAB to calculate the volume of material underneath one mound using a parabolic mathematical model, regression analysis, and integration in 3D space 
4.Next, a simulation was run using salt and a Coke bottle, and it was determined that a hyperboloid surface model was a better representation of mound geometry 
5.Then, the code implemented the use of the convex hull command in MATLAB to calculate volume instead of integration. An iterative sampling point removal procedure was also implemented. This iterative procedure removes one point at a time from a predetermined location of the sample points based on the parameters until the desired error is met 
6.Finally, the code was expanded to account for up to 5 fill and 5 draw points 
