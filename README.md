# valentinka-joke
A joke program on tkinter, which can turn off the PC

## How to run

### *Step 1*
Clone this repo: `git clone https://github.com/DragonsCode/valentinka-joke`

### *Step 2*
Create a virtual environment with python: `python -m venv venv`

### *Step 3*
Activate the venv
Linux: `source venv/bin/activate`
Windows *PowerShell*: `venv\Scripts\Activate.ps1`
Windows *CMD*: `venv\Scripts\activate.bat`

### *Step 4*
Install the required libraries: `pip install -r requirements.txt`

### *Step 5*
Run the `valentinka.py` script: `python valentinka.py`


## How to build

### *Step 1*
Make sure you have installed the `pyinstaller` library: `pip install pyinstaller`

### *Step 2*
Build the program with `pyinstaller`: `pyinstaller --onefile --noconsole --icon=heart.ico valentinka.py`
**Note:** *if you have your own icon or script, just replace the `heart.ico` for the icon and `valentinka.py` for the script name*

### *Step 3*
You will find the `.exe` file in the `dist` folder


# Enjoy!
