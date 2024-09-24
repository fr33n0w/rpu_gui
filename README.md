# rpu_gui
Reticulum Network Package Updater GUI 

### RETICULUM PACKAGE UPDATER GUI // RPU_GUI.PY V1.2 BY F ### 


Simple GUI to detect all the official reticulum packages update from github on start, 
check if installed, compare versions and tell if you need to update. 

All the info are displayed on the GUI.


Packages updates checked:

RNS
LXMF
NOMADNET
MESHCHAT
SIDEBAND
RNODE CE


RNS, LXMF and NOMADNET can be updated by pressing the Install/Update button if you need to update.

MESHCHAT, SIDEBAND AND RNODE CE are only checked for new versions, you have to manually install them.

The GihHub button takes your web browser to the official github release page of each packages.

####### REQUIREMENTS ########

Python & Pip of course, both on windows or linux.

To run this script you need these other pip modules installed:

tkinter , requests, json, subprocess, webbrowser, threading

If you encounter some error on the script launch, try to install such modules with command:

pip install tkinter requests json subprocess webbrowser threading


#################################################################
Tested on windows 10 with python & pip, all seems to work fine. 
Double click on rpu_gui.py to open or use: python rpu_gui.py under command prompt.

Untested on linux at the moment, you tell me if it works.
#################################################################

RPU_GUI.PY V1.2 BY F - 24/09/2024


######### CHANGELOG:
#### 23/09/2024 - FRU_GUI.PY V1.0 
- FIRST PUBLIC RELEASE

#### 24/09/2024 - FRU_GUI.PY V1.1 
- FIRST REVISION 
- IMPROVED GUI AND GRAPHIC

#### 24/09/2024 - FRU_GUI.PY V1.2
- SECOND REVISION 
- IMPROVED GUI 
- RESOLVED "STATUS" LABEL NOT UPDATING ON INSTALLING NEW PACKAGE
