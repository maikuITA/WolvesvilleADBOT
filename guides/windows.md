**#1: Download the script**
* Download ZIP of the project

![image1](https://i.imgur.com/DEwNATx.png)

* Download scrcpy [here](https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md)

**#2: Python**
* Unzip python-3.7.0-adm64.rar (python-3.7.0.rar is the 32bit VERSION, 64bit RECOMMENDED) and run the .exe
* Add python to PATH. This is REALLY important when installing the python package!

![image3](https://i.imgur.com/j2M7QqZ.png)

**#3: Requirements**
* Open folder in terminal (cmd or powershell)

![image4](https://i.imgur.com/NGXqvvR.png)

* To install the requirements run the following code ```pip install -r requirements.txt```
* (open requirements.txt to check which modules will be installed)

![image5](https://i.imgur.com/g78iPww.png)

**#4: Coordinates**
* Run the mouse position program (MousePosition32bit.exe)

![image6](https://i.imgur.com/EDzOFB9.png)

* You need to replace x and y values in the place of ```CHANGEME``` inside of wolvesville_YOURLANGUAGE.py :

* Put cursor on the pink spot and write down the X and Y coordinates:

![image7](https://i.imgur.com/GPhIRh8.png)

* Replace X and Y values:

![image8](https://i.imgur.com/sg6YeWT.png)

**#5: Select the preferred script mode**
* The script works in two modes, limitless (endless mode) and limited mode. Run it in your preferred mode and language.

**#6: Run the script**
* To run the script open the folder in terminal (STEP 3) and paste the following code: 
* ```python.exe wolvesville_YOURLANGUAGE.py```