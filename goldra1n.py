import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import time
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import subprocess
import webbrowser

path = os.getcwd()

print(path)

root = tk.Tk()
root.title('Goldra1n LITE v1.9.2')
root.iconbitmap('goldrainicon.ico')

frame = tk.Frame(root, width="600", height="300")
frame.pack(fill=BOTH,expand=True)

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

def detectDevice():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    #step 1 technically
    print("Searching for connected device...")
    subprocess.run("idevicepair unpair", shell=True)
    subprocess.run("idevicepair pair", shell=True)
    subprocess.run("goldra1n\\euphoria_scripts\\ideviceinfo.exe > goldra1n\\euphoria_scripts\\lastdevice.txt", shell=True)
    
    time.sleep(2)

    f = open("goldra1n\\euphoria_scripts\\lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if("ERROR:" in fileData):
        #no device was detected, so retry user!
        print("ERROR: No device found!")
        messagebox.showinfo("No device detected! 0x404","Try disconnecting and reconnecting your device.")
    else:
        #we definitely have something connected...
        #find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start)+len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        #find the iOS
        #we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2)+len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if(len(UDID) > 38):
            #stop automatic detection
            timerStatus = 0
            print("Found UDID: "+LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!","Found iDevice on iOS "+LAST_CONNECTED_IOS_VER)

        else:
            print("Couldn't find your device")
            messagebox.showinfo("Somethings missing! 0x405","Try disconnecting and reconnecting your device.")

def startDFUCountdown():
    print("Get ready to put device into DFU mode...")

def enterRecMode():
    print("Kicking device into recovery mode...")
    os.system(".\\goldra1n\\euphoria_scripts\\enterrecovery.bat")

def exitRecMode():
    print("Kicking device out of recovery mode...")
    os.system(".\\goldra1n\\euphoria_scripts\\exitrecovery.bat")
    messagebox.showinfo("Sent command!", "Kicked device out of recovery mode!\n\nNow if your device is not exiting recovery mode still and keeps looping to it, either re-jailbreak with the same jailbreak you did or remove the jailbreak you installed.")


def showDFUMessage():
    messagebox.showinfo("Step 1", "Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")


def jailbreakIOS15SemiTethered():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    # iOSVER = str(LAST_CONNECTED_IOS_VER)
    iOSVer = Entry.get(entry)
    
    # check if theres a valid string to continue to reversing jb
    if(len(iOSVer) < 2):
        messagebox.showinfo('Bypass Failed', 'Give me a valid iOS version.')
    else:
        messagebox.showinfo('Ready to Jailbreak...', 'Hi, iOS '+str(iOSVer)+'. \n\nWe will now attempt to bypass iOS '+str(iOSVer)+' Semi-Tethered.')
        print("Starting bypass...")
        os.system("idevicepair unpair")
        os.system("idevicepair pair")
        os.system(f"cd .\\goldra1n\\ && .\\goldra1n.bat --tweaks {iOSVer} --semi-tethered")
        print("Device is bypassed!\n")
        messagebox.showinfo('Bypass Success!', 'Device is now bypassed!')


def callback(url):
    webbrowser.open_new_tab(url)


def quitProgram():
    print("Exiting...")
    os.system("exit")

root = tk.Tk()
root.title('Goldra1n LITE v1.9.2')
frame = Frame(root, width=500, height=300)
frame.pack()

label = Label(frame, text="Goldra1n LITE", font=('Helveticabold', 36))
label.place(x=190, y=50)

my_label2 = Label(frame, text="Designed for iOS 16.0 - 16.2")
my_label2.place(x=260, y=100)

my_label3 = Label(frame, fg="gold", text="ver 1.9.2 \n(dev + sync)")
my_label3.place(x=20, y=250)

cdetectDevice = tk.Button(frame, text="Pair iDevice", command=detectDevice)
cdetectDevice.place(x=50, y=150)

entry = Entry(frame)
entry.place(x=200, y=150)

cbeginExploit12 = tk.Button(frame, text="Semi-Tethered Bypass!", command=jailbreakIOS15SemiTethered, state="normal")
cbeginExploit12.place(x=212, y=180)

cexitRecovery = tk.Button(frame, text="Exit Recovery Mode", command=exitRecMode)
cexitRecovery.place(x=224, y=250)

# Create a Button to install dependencies
installdepen = tk.Button(root,
                  text="Install Dependencies",
                  command=installDependenciesSH)
installdepen.place(x=400, y=250)

# Create a Label to display the link
link = tk.Label(root, text="Thanks to @ios_euphoria", font=('Helvetica', 12), cursor="hand2")
link.place(x=20, y=290)
link.bind("<Button-1>", lambda e: callback("https://twitter.com/ios_euphoria"))

link2 = tk.Label(root, text="& @iAldazActivator", font=('Helvetica', 12), cursor="hand2")
link2.place(x=168, y=290)
link2.bind("<Button-1>", lambda e: callback("https://twitter.com/iAldazActivator"))

# Create a Label to display the link
link3 = tk.Label(root, text="Thanks to Jailbreak @palera1n team", font=('Helvetica', 12), cursor="hand2")
link3.place(x=300, y=290)
link3.bind("<Button-1>", lambda e: callback("https://twitter.com/palera1n"))

# KILL USB TO STOP CONNECT AND DISCONNECT ISSUE
os.system("powershell.exe -Command \"& {&'./t.ps1'}\"")

root.geometry("600x320")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

root.mainloop()
