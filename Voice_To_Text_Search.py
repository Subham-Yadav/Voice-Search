from tkinter import *
from playsound import playsound
import webbrowser
import speech_recognition as sr
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open_new(' ')

def recordVo():
    global e
    recording = sr.Recognizer()
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        playsound('speech.wav')
        audio = recording.listen(source)
        try:
            temp_text = recording.recognize_google(audio)
            Text.insert(e, END, temp_text + " ")
            SearchChrome(temp_text)
        except Exception as ep:
            Text.insert(e, END, ep)
            #print(ep)

def SearchChrome(temp_text):
    t = temp_text.split()
    if len(t)==1:
        new_text = t[0]
    else:
        new_text = t[0]
        for i in range(1, len(t)):
            new_text = new_text + '+' + t[i]
    final_text = "https://www.google.com/search?q=" + new_text + "&oq=" + new_text +"&aqs=chrome.1.69i57j0l5.9852j0j1&sourceid=chrome&ie=UTF-8"
    webbrowser.get(chrome_path).open_new_tab(final_text)

new_win = Tk()
new_win.title("Voice to Text")
new_win.geometry("375x200")

record = Button(new_win, text="Record", command=recordVo)
record.grid(row=1, column=1, padx=(25,0), pady=(30,0))

e = Text(new_win, height=5, width=40)
e.grid(row=2, column = 1, padx=(25,25), pady=(20,10))
e.focus_set()

new_win.resizable(0,0)
new_win.iconbitmap("voice_to_text.ico")
new_win.mainloop()
