# Digital-Circuit-Designer

Digital Circuit Designer is a Django Based Website designed for solving some of the fundamental Electronics Problems. The key Problems include :
1. Generating Boolean Expression using Min terms.
2. Designing User Defined Flip-Flop from Base Flip-flop.
3. Designing Counter for the required Counting Sequence using any Base Flip-Flop.

The end Result/View would look like the following:
1. Generating Boolean Expression using Min terms.


![bool-view](https://github.com/ashishjain0338/Digital-Circuit-Designer/blob/master/Images/phase1.PNG)



2. Designing User Defined Flip-Flop from Base Flip-flop.


![ff-view](https://github.com/ashishjain0338/Digital-Circuit-Designer/blob/master/Images/phase2.PNG)


3. Designing Counter for the required Counting Sequence using any Base Flip-Flop.


![Counter-view](https://github.com/ashishjain0338/Digital-Circuit-Designer/blob/master/Images/phase3.PNG)

## Requirements

	1. Python 3.7.3 or above
	2. Python Modules
			1. simplejson
			2. django
      3. Binpy
      
## Installation

### 1. Python 3.7.3 or above

1. Download the latest python version [Download](https://www.python.org/downloads/)
2. Install the downloaded file, Make sure to tick the dialogue box when installer provides an option to configure the **PATH** and **PATHEXT** variables 
3. To Check python has been successfully installed or not. Do the following:-
	1. Open Command Line and type the command. 
		``` bash
			python
		```
	2. The version of python would be shown along with opening of python Terminal starting with ">>>" , if the python is successfully installed.
	![python install](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/python%20install.PNG)
4. If Step 3 shows some Error then ,Copy the path of Installed folder (Example:->C:\Program Files\Python 3.8) and paste it in your System Environment Variables.

### 2. Python Modules
1. simplejson
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install simplejson
		```
	3. Download and installation would start automatically
	![Simple Json](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/Simplejson.PNG)
2. django
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install django
		```
	3. Download and installation would start automatically
	![Django](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/django.PNG)
3. binpy
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install binpy
		```
	3. Download and installation would start automatically


## How to use
1. Download this project from Github in a zip file by clicking at the Code(Green button) at https://github.com/ashishjain0338/Whatapp-Reloaded
2. Extract the Downloaded file.
3. Open Command Line and move to the Extracted directory by using cd command as
```
  cd PathOfTheExtractedFolder
```
4. Then enter the Command
	``` 
		python manage.py runserver
	```
	![Running Server](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/starting%20server.PNG)
5. Then open any browser and type
	```
		localhost:8080
	```
	**OR** Instead you can also type the link that would appear at Command line after typing the command at point 2(Example:-> http://127.0.0.1:8000/)
