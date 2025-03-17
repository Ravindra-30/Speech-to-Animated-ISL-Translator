from tkinter import *
import time, logging
import speech_recognition as sr
import os, os.path
from os import startfile
logging.basicConfig(level=20)
from ffpyplayer.player import MediaPlayer
import tkinter.messagebox
from tkinter.messagebox import Message 
from _tkinter import TclError
from moviepy.editor import *
import vlc
import time
from genericpath import exists
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"


def play_movie(path):
    
    startfile(path)
    
def PlayVideo(video_path):
    p = vlc.MediaPlayer(video_path)
    p.play()

    print('is_playing:', p.is_playing())  # 0 = False

    time.sleep(0.5)  # sleep because it needs time to start playing

    print('is_playing:', p.is_playing())  # 1 = True

    while p.is_playing():
        time.sleep(0.5)


def set_text_by_button():
    sample_text.delete(0,END)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening (close to exit)...")
        audio = r.listen(source)
        try:
            global a
            a=r.recognize_google(audio)
            sample_text.insert(0,a.lower())
            a=a.lower()
        except:
            sample_text.insert(0,"Could not listen")
            
def play():
    a=sample_text.get()
    a=a.lower()
    lst=a.split()
    print(lst)
    st=0
    i=0
    j=0
    list1=[]
    clips=[]
    #print(lst)
    while i<len(lst):
        #print(i)
        if (i+3<len(lst)) and lst[i]+lst[i+1]+lst[i+2]+lst[i+3] in isl_gif:
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/animations/"+str(lst[i])+str(lst[i+1])+str(lst[i+2])+str(lst[i+3])+".mp4")
            print(str(lst[i])+" "+str(lst[i+1])+" "+str(lst[i+2])+" "+str(lst[i+3]))
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/_.mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            i=i+4
            continue
        elif (i+2<len(lst)) and lst[i]+lst[i+1]+lst[i+2] in isl_gif:
            print(str(lst[i])+" "+str(lst[i+1])+" "+str(lst[i+2]))
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/"+str(lst[i])+str(lst[i+1])+str(lst[i+2])+".mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/_.mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            i=i+3
            continue
        elif (i+1<len(lst)) and lst[i]+lst[i+1] in isl_gif:
            print(str(lst[i])+" "+str(lst[i+1]))
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/"+str(lst[i])+str(lst[i+1])+".mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/_.mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            i=i+2
            #print(i)
            continue
        elif lst[i] in isl_gif :
            print(str(lst[i]))
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/"+str(lst[i])+".mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/_.mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            i=i+1
            continue
        else:
            for st in range(len(str(lst[i]))):
                list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/"+str(lst[i]).upper()[st]+".mp4")
                final = VideoFileClip(list1[j])
                final = final.subclip(0, 1)
                j=j+1
                clip_resized = final.resize(height=720)
                clips.append(clip_resized)
            list1.append("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/animations/_.mp4")
            final = VideoFileClip(list1[j])
            j=j+1
            clip_resized = final.resize(height=720)
            clips.append(clip_resized)
            i=i+1
            continue

    final = concatenate_videoclips(clips,method='compose')
    final.write_videofile("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/animations/created.mp4")
    PlayVideo("C:/Users/ravin/Downloads/Projects/Speech-to-Animated-ISL-Translator/animations/animations/created.mp4")

def main():
    window = Tk()
    window.title("INDIAN SIGN LANGUAGE TRANSLATOR(SignXlator)")
    window.configure(width=500, height=300)
    window.geometry("500x300")
    
    label1 = Label(window, text="", fg="red")
    label1.pack()
    label2 = Label(window, text="(A TRANSLATOR THAT CAN CONVERT SPEECH TO ISL VIDEOS)", fg="black")
    label2.pack()
    label3 = Label(window, text="Press mic button to turn ON mic", fg="blue")
    label3.pack()
    label8 = Label(window, text="or", fg="black")
    label8.pack()
    label7 = Label(window, text="Type the text and press play", fg="blue")
    label7.pack()
    label4 = Label(window, text="", fg="blue")
    label4.pack()
    frame1 = Frame(window)
    frame1.pack()
    la = Label(frame1, text="you said:")
    la.pack(side=LEFT)
    global isl_gif
    isl_gif=['accident','allthebest','allergies','arm','asthma','beard','belly','bones','breathe','bye','cancer','diabetes','doctor','ear','ecg','emergency','excuseme','eye','face','feet','fever','firstaidbag', 'goodmorning','goodnight','goodafternoon',
        'goodevening','good','night','hair','hand','head','headache','heartattack','hello','hospital','howareyou','iamfine','leg','lungs','medicine','morning','mouth','mynameis','nicetomeetyou','night','no','nose','ribs','skeleton','skin','skull','sorry','spine','stomachache',
        'symptoms','thankyou','thermometer','throat','teeth','virus','vomit','welcome','whatisyourname','yes',
        'one','two','three','four','five','six','seven','eight','nine','zero']    
    arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    global sample_text
    sample_text = Entry(frame1,width=50)
    sample_text.pack(side=LEFT)
    #sample_text.delete(0,"end")
    global r
    r = sr.Recognizer()
    label6 = Label(window, text="          ", fg="blue")
    label6.pack()
    frame2 = Frame(window)
    frame2.pack()
    Button(frame2,text='mic', padx=50,command = set_text_by_button).pack(side=LEFT)
    label5 = Label(frame2, text="          ", fg="blue")
    label5.pack(side=LEFT)
    Button(frame2,text='play',padx=50, command = play).pack(side=LEFT)
    #button = Button(, text='Stop', width=25, command=r.destroy)
    # move window center
    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))


    window.mainloop()
if __name__ == '__main__':
    main()
#./Scripts/python.exe window1.py -m deepspeech-0.9.3-models.pbmm  -s deepspeech-0.9.3-models.scorer