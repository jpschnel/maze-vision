# maze-vision
To find the fastest way around a set of obstacles by analyzing a bird's eye perspective

Follow these steps for first time use and when entering a completely new environment.

**Setup the pi**

Download the maze vision foilder to your pi

Connect your pi car to a monitor.

Go to the terminal and enter the following:

         hostname -I

**Getting your computer ready**
         
On your computer navigate to the maze-vision folder

Inside the config file write the number the pi returned. It should look somewhat like this:

         192.168.43.113
         
In the maze vision folder enter the commands:

         chmod +x install
         ./install
       
**Setting up the Maze**

Place the Robot on the surface (with the white wheel facing toward you when you take the picture) and pick a random object to represent the end goal-something with many varying colors and easily discernible usually works best. You can look at the files in the folder named Samples to get an idea. 

Place these in the maze

Take a picture from overhead

Upload the picture file inside the maze-vision directory as mazeinput.jpg

**Creating Templates**

Open the file with GIMP.

Use the rectangle tool (the box in the toolbar) and drag over the entirety of the robot(including any wires)

right-click and select **Edit>Copy** and then **Edit>Paste as>New Image**

Go to **File>Export as** and save the file in the maze-vision folder as **robot_template.jpg**.

Repeat this process for the end goal and name it **end_template.jpg**.


**Running the program**

Enter the following command in the maze vision folder:
        
        ./run

Now until you switch locations(at which point templates may need to be redefined) you can just take a picture and place it in the folder the same way as before and then use the same *run* command


**Troubleshooting**
Before starting, be sure that both that the pi and motor hat are both powered on.

If the program says that there is no path, check the extracted image. If the blue and red squares are not lining up with the car and finish respectively, then your template images need to be updated. If there is no path found but the car and finish are correctly found, then either part of the car or finish are not in the shot, or the obstacles are too close to start/finish. In many cases retaking the templates/maze picture will solve the conflict.

If shortest path file is not found in pi, be sure the directories are set up on robot as described above under "setup the pi"
