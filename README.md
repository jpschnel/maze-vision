# maze-vision
To find the fastest way around a set of obstacles by analyzing a bird's eye perspective.

Follow these steps for first time use and when entering a completely new environment.

**Getting Started**

Make sure you are running on a Linux distribution such as Ubuntu or mint.

A HDMI compatible monitor or television, and keyboard may be required to connect your raspberry pi to a network.
Note: Your raspberry pi may not be wifi compatible out of the box. If you are using a pi2.0 or older, you will need a USB wifi dongle.

Be sure the pi is connected to the same network as your PC, otherwise no data can be sent from your computer.
For more information on connecting your pi to your network, look here:
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

Once the pi is connected, download the latest maze-vision release to your PC.

Extract the downloaded file, and move the "Florence" folder to the Home directory of your raspberry pi.

**Setup the pi**
If you know the IP adress of your raspberry pi, you may skip this step;

Connect your pi car to a monitor.

Go to the terminal(**Ctrl-Alt-T**) and enter the following:

         hostname -I

Be sure to record what shows up afterwards. 

**Getting your computer ready**
         
On your computer navigate to the maze-vision folder.

Inside the config file inside the maze-vision folder write the number the pi returned. It should look somewhat like this:

         192.168.43.113
         
In the maze-vision folder right click>**open Terminal Here** enter the commands:

         sudo chmod +x install
         ./install
       
**Setting up the Maze**

Place the Robot on the surface (with the white wheel facing toward you when you take the picture) and pick a random object to represent the end goal-something with many varying colors and easily discernible usually works best. You can look at the files in the folder named Samples to get an idea. 

Place these in the maze.

Take a picture from overhead.

Upload the picture file inside the maze-vision directory as **mazeinput.jpg**.

**Creating Templates**

Open the file with GIMP. This can be done by right-clicking **mazeinput.jpg** and selecting "Open with.../GIMP".
   If GIMP has not been installed on your computer, it can be installed by:
         sudo apt-get install gimp

Use the rectangle tool (the box in the toolbar) and drag over the entirety of the robot(including any wires).

right-click and select **Edit>Copy**, right-click again and then **Edit>Paste as>New Image**.

Go to **File>Export as** and save the file in the maze-vision folder as **robot_template.jpg**.

Repeat this process for the end goal and name it **end_template.jpg**.


**Running the program**

**Right click>Open Terminal Here** and Enter the following command in the maze vision folder:
        
        ./run

Now until you switch locations(at which point templates may need to be redefined) you can just take a picture and place it in the folder the same way as before and then use the same *run* command.


**Troubleshooting**
Before starting, be sure that both that the pi and motor hat are both powered on.

If the program says that there is no path, check the extracted image. If the blue and red squares are not lining up with the car and finish respectively, then your template images need to be updated. If there is no path found but the car and finish are correctly found, then either part of the car or finish are not in the shot, or the obstacles are too close to start/finish. In many cases retaking the templates/maze picture will solve the conflict.

If shortest path file is not found in pi, be sure the directories are set up on robot as described above under "setup the pi".
