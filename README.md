**VDC User Manual**
For python version     3.6.13
**STEPS TO BE FOLLOWED FOR VDC**

Note: For creating a new environment, anaconda prompt should be installed in the system.
1.	Download and extract the zip containing the VDC Course to Documents folder present in C drive of your PC.
2.	Traverse to the VDC folder using “cd” command in anaconda prompt.
3.	Use this command to create a new environment in anaconda prompt:  conda create -n environment_name python=version [example: conda create -n vdc python=3.6.13] 
4.	 Conda activate environment_name [example: conda activate vdc]
5.	Install the dependencies using the command, pip install –r requirements.txt
Note: If any error arises regarding the versions of the dependencies, update the previous version of the particular dependency library from the versions listed in the terminal.
6.	Change environment name in python interpreter (traverse to the environment that is created using the required python version).
7.	Drive the self-driving car in training mode by clicking on the record button present in the training mode. That will show the path, where the data will be stored. Select the folder that is mentioned in the training program.
8.	After driving, click on pause button and close the window.
9.	The data of that will be recorded. In training program, change the path of the folder to the one the data are being recorded. If needed, change the epoch values. Now it.
10.	The training program will deliver a model based on the data acquired which are stored in the path with the extension (.h5).
11.	Then run the testing program as well as, run the autonomous mode in the simulator simultaneously.
Note: A popup window will appear after running the testing program (requesting permission for allowing public and private network to access python app) click on allow in that.
12.	While the testing program is running based on the trained data, the car will autonomously move.
****** End of document ******
