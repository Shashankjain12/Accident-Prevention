<h1 align="center"> AccidentPrevention</h1>

This project involves detection and prevention of road side accidents using the library known as OpenCv
This involves creation of some recognising technology that can detect the chances of collision if two cars
are close to each by buzzing of certain alarm if the two cars are close to each other this takes in 
consideration of fact that certain minimum velocity is required for the two cars to start detection
In this module which is set to minimum value of 50m/s to start the process of detection.
This approach involves certain steps for detection of certain cars

<h2>Step 1</h2>
<hr></hr>
This step involves detection of certain cars using certain datasets of images which when converted into
xml file of certain information about the file which is in the form of Haarcascade classifiers 
Then these Haars of certain images are taken from the dataset and then for detection of certain cars we 
turn on our camera for detection purpose we are using Ip camera for capturing of video
Then within the process of capturing certain videos we are converting every frame of certain image to 
grayscale inorder to detect the cars.

<h2>Step 2</h2>
<hr></hr>
After detection of certain cars we are finding edges where there are edges in that cars
by certain methods such as erosion for shrinking of borders of an image then dilation to expand borders
for perfect detection of certain canny edges in an image.Then after finding edges in an images we are 
plotting contours in order to find certain end points of that image so as to get sharp entries of an image
then we use imutils for grabbing of all contours regions in order to get all the points of an image
Then we sort all the contours of an image.Then based on all those contour areas we are plotting
all the box points of certain images.Then we minimze this area inorder to calculate the minimum area for that
certain image then after defining thos minimum area region we have taken a reference point in our case it is
our camera which is taken as one reference object from which the distance between object is calculated then
after calculating certain distance using euclidian distance formula for finding the distance between two refernce objects

<h4>Some steps that are needed to be implemented </h4>
After finding the distance from the reference object we need to calculate the distance between two objects so 
as to find the distance between then and in order to do that we also need to set certain velocity so as that 
threshold velocity os required for object detection to be started.And we also need to construct a code so as to
make kind of buzzer alarm code so as that will buz when car will reach at that certain minimum distance

This project is a direct implementation of team DARK KNIGHTS for geekathon 2019 which was not possible without
the help of other members:-
1. Ishank Tiwari ()
2. Sparsh Jain (sparshjain99) 


