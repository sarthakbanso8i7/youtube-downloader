from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import urllib
import webbrowser
import shutil


#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file(): 
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')
def open():
    sartv=webbrowser.open("https://www.linkedin.com/in/sarthak-bansal-297741258/", new=0, autoraise=True)
screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, bg="red" ,width=500, height=500)
canvas_label= Label(screen,bg="white",text="youtube download", font=('Arial',34))
sart=Button(screen,bg="orange",text="follow on linkedin sarthak bansal",font=('Arial',23),command=open)
canvas.create_window(250,70,window=canvas_label)
canvas.create_window(250,450,window=sart)
canvas.pack()


#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='blue', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)


screen.mainloop()
