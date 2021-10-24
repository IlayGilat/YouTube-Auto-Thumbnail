import os 
import cv2
import tkinter as tk
from tkinter import messagebox,filedialog,Text,Entry
from random import *
from PIL import Image,ImageDraw,ImageFont,ImageFilter

#SD

root = tk.Tk()
root.resizable(False,False)
root.title("Thumbnail Generator")
root.geometry("400x400")



videoPath = ""
Text = ""
savePath = ""

def run():
    if videoPath != "" and savePath != "":
        Text = TextField.get()
        Generator(Text,videoPath,savePath)
    else:
        messagebox.showinfo("Error","You Need To Choose Video File And Destenation")

def buildLabels():
    for widgit in frame.winfo_children():
        widgit.destroy()

    videopathtext="Video Selected: "+videoPath
    savepathtext = "Save Directory Selected: "+savePath
    VideoPathlabel = tk.Label(frame,text=videopathtext)
    VideoPathlabel.pack()
    SavePathlabel = tk.Label(frame,text=savepathtext)
    SavePathlabel.pack()

def addVideo():
    global videoPath
    videoPath = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("videos","*.mp4"),("all files","*.*")))
    buildLabels()
    
   

def selectPath():
    global savePath
    savePath = filedialog.askdirectory(initialdir="/",title="Select Save Dir")
    buildLabels()

def Generator(myText,myVideo,saveDir):
    SaveFilePath = saveDir+"/thumbnail.png"
    size_YT=(1270,1080)
    #Pulling Image From Video Part
    video = cv2.VideoCapture(myVideo)
    success,image = video.read()
    frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    random = randint(1,frames)
    video.set(1,random)
    success,image= video.read()
    cv2.imwrite(SaveFilePath, image) 
    #End Pulling From Video Part

    #Putting Filter
    StartingImage = Image.open(SaveFilePath)
    StartingImage.filter(ImageFilter.GaussianBlur(7)).save(SaveFilePath)

    #Resizing
    ResizedImage=Image.open(SaveFilePath)
    ResizedImage.thumbnail(size_YT)
    ResizedImage.save(SaveFilePath)

    #PuttingText
    FinalImage=Image.open(SaveFilePath)
    font = ImageFont.truetype("arial.ttf",72)

    draw=ImageDraw.Draw(FinalImage)

    text=myText
    Centering = 475-(len(text) * 12)
    draw.text((Centering,300),text,(255,255,255),font=font,stroke_fill="black",stroke_width=2,spacing="7")
    FinalImage.save(SaveFilePath)
    messagebox.showinfo("Succsess","Generated Thumbnail Succsessfully")
    



HeaderFont = ('arial','16')
H2Font=('arial','12')


Header = tk.Label(root,text="THUMBNAIL GENERATOR",font=HeaderFont)
Header.pack()

EntryFrame = tk.Frame(root)
EntryFrame.place(relwidth=1,relheight=0.1,rely=0.1)

EntryText = tk.Label(EntryFrame,text="Text",font=H2Font)
EntryText.pack()
TextField = Entry(EntryFrame,width=40,bd=0,relief="groove")
TextField.pack(side = "top")


frame= tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.2,relx=0.1,rely=0.3)

ButtonFrame = tk.Frame(root)
ButtonFrame.place(relwidth=0.8,relheight=0.2,rely=0.85,relx=0.2 )


SelectVideo = tk.Button(ButtonFrame,text="Open File",padx=10,pady=5,fg="white",bg="#263D42" ,command=addVideo,anchor="w")
SelectVideo.pack(side="left")


SelectPath = tk.Button(ButtonFrame,text="Select Path",padx=10,pady=5,fg="white",bg="#263D42" ,command=selectPath,anchor="w")
SelectPath.pack(side="left")


Generate = tk.Button(ButtonFrame,text="Generate",padx=10,pady=5,fg="white",bg="#263D42" ,command=run,anchor="w")
Generate.pack(side="left")


root.mainloop()