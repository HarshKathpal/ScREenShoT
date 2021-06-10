import pyautogui
import tkinter as tk
import os
dire = os.getcwd()
from pathlib import Path

myfile = Path(f'{dire}/ScreenShot/i.txt')
if "ScreenShot" in os.listdir():
    pass
else:
    os.mkdir("ScreenShot")
    myfile.touch()
    f = open("ScreenShot/i.txt","w")
    f.write("1")
    f.close()
    
root= tk.Tk()
root.overrideredirect(True)
root.call('wm', 'attributes', '.', '-topmost', '1')
root.geometry('80x30+1270+700')

canvas1 = tk.Canvas(root, width = 80, height = 30)
canvas1.pack()

def takeScreenshot ():
    ff = open("ScreenShot/i.txt","r")    #default read and text mode 
    i = ff.read()
    ff.close()
    ff = open("ScreenShot/i.txt","w")
    ff.write(f"{int(i)+1}")
    ff.close()    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'ScreenShot\\ScreenShot'+str(i)+'.png')

def exit():
    root.destroy()

myButton = tk.Button(text='ScS', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(60,15, window=myButton)
myButton = tk.Button(text='Exit', command=exit, bg='red',fg='white',font= 10)
canvas1.create_window(20,15, window=myButton)

root.mainloop()
