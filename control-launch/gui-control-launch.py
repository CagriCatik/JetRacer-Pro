from tkinter import *
import subprocess
import webbrowser
 

def reboot():
    bashCommand = "dts duckiebot reboot myrobot"
    output = subprocess.check_output(['bash','-c', bashCommand])

def shutdown():
    bashCommand = "dts duckiebot shutdown myrobot"
    output = subprocess.check_output(['bash','-c', bashCommand])


def opendashboard():
    webbrowser.open('http://myrobot.local/dashboard/robot')  # Go to example.com



root = Tk(className=' Control Launch of JetRacerPro')
root.geometry("500x200")


canvas = Canvas(root, width = 130, height = 130)      
canvas.pack()      

Button(root, text="Turnoff   ", command=shutdown).pack()
Button(root, text="Reboot    ", command=reboot).pack()
Button(root, text="Dashboard ", command=opendashboard).pack()
root.mainloop()