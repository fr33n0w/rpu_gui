# rpu_gui
Reticulum Network Package Updater GUI 

# RETICULUM PACKAGE UPDATER GUI // RPU_GUI.PY V1.5 BY F. 


Simple GUI to detect all the official reticulum packages update from github on start, 
check if installed, compare versions and tell if you need to update. 

All the info are displayed on the GUI.

#RPU_GUI V1.5 - RELEASED: 06/10/2024
----------------------------------------------------------

#RETICULUM PACKAGES UPDATER V1.5 BY F. 

PYTHON SCRIPT WITH GUI TO CHECK FOR UPDATES ON THE OFFICIAL RETICULUM NETWORK DEVELOPERS GITHUB, COMPARE THE GITHUB VERSION WITH THE INSTALLED VERSION ON YOUR MACHINE, DISPLAY IF YOU ARE UP TO DATE OR NEED TO INSTALL NEW VERSION(S).

-----------------------------------------------------------
*** CHECKS FOR AND UPDATES THE FOLLOWING RETICULUM PACKAGES FROM THE OFFICIAL GITHUBS:

*    RNS
*    LXMF
*    NomadNet
*    Reticulum MeshChat
*    Sideband
*    RNode Stock
*    RNode CE
*    RNode TN

--------------------------------------------------------------

### CHANGELOG FOR RPU_GUI V1.5:

** ADDED RNODE TN FIRMWARE UPDATE CHECK
** MULTIPLE BUGS CORRECTED
** IMPROVED GUI STABILITY

-----------------------------------------------------------------

#INSTALLATION:

1) DOWNLOAD THE PYTHON SCRIPT FROM THE LAST RELEASES OF THIS GITHUB REPOSITORY

2) INSTALL FOLLOWING REQUIREMENTS WITH COMMAND:
    pip install tkinter requests json subprocess webbrowser threading
    (if you get errors, try pip install with each package separately, ex. pip install tkinter , then pip install json, etc. for all packages)

3) RUN THE SCRIPT WITH COMMAND:
    python rpu_gui.py
    (or python3 rpu_gui.py , based on your python installation.)
    ((If you have a windows machine you can double click on the py file, works also on some linux machines))

------------------------------------------------------------------------

NOTE:
YOU CAN RAPIDLY CHECK FOR UPDATES AND INSTALL THESE FOLLOWING PACKAGES:
RNS , LXMF AND NOMADNET WITH THE CLICK OF A BUTTON.

FOR MESHCHAT, SIDEBAND, RNODE AND RNODE TN & CE SOFTWARE PACKAGES,
YOU NEED TO INSTALL THEM MANUALLY. THE SCRIPT JUST CHECKS FOR THE ONLINE VERSION NUMBER.

DEVELOPER IS NOT AFFILIATED WITH THE DEVELOPMENT OF RETICULUM NETWORK, 
JUST MADE THIS  INDEPENDENT TOOL TO MAKE RETICULUM PACKAGE UPDATES EASY AND FAST.

---------------------------------------------------------------------------

THIS IS MY FIRST GITHUB RELEASE, BE KIND ON BUGS OR ANY OTHER ISSUE, FEEDBACK ARE WELCOME :)

ALL INSTALL REQUIREMENTS AND FULL INFO ON THE GITHUB README.
----------------------------------------------------------------------------

SCREENSHOT:
![rpu_gui_screenshot](https://github.com/user-attachments/assets/87058a65-eb99-4104-9d0b-f66cbb1abf88)


RNS, LXMF and NOMADNET can be updated by pressing the Install/Update button if you need to update.

MESHCHAT, SIDEBAND AND RNODE CE are only checked for new versions, you have to manually install them.

The GihHub button takes your web browser to the official github release page of each packages.



#################################################################
Tested on windows 10 with python & pip, all seems to work fine. 
Double click on rpu_gui.py to open or use: python rpu_gui.py under command prompt.

Untested on linux at the moment, you tell me if it works.
#################################################################

RPU_GUI.PY V1.5 BY F - 06/10/2024

