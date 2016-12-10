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

Inside the config file write the number the pi returned. it should look somewhat like this:

         192.168.43.113
         
In the maze vision folder enter the command:

         ./install
       
**Setting up the Maze**
Place the Robot on the surface and pick a random object to represent the end goal-something with many varying colors and easily discernible usually works best. You can look at the files in the folder named Samples to get an idea. 

Place these in the maze

Take a picture from overhead

Upload the picture file inside the maze-vision directory as mazeinput.jpg

**Creating Templates**

Open the file with gimp.

Use the rectangle tool (the box in the toolbar) and drag over the entirety of the robot(including any wires)

right-click and select **Edit>Copy** and then **Edit>Paste as>New Image**

Go to **File>Export as** and save the file in the maze-vision folder as **robot_template.jpg**.

Repeat this process for the end goal. name it **end_template.jpg**.


**Running the program**

Enter the following command in the maze vision folder:
        
        ./run

Now until you switch locations(at which point templates may need to be redefined) you can just take a picture and place it in the folder the same way as before and then use the same *run* command
        
 
