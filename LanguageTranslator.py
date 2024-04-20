from tkinter import *
import speech_recognition as sr
from googletrans import Translator

translator = Translator()

Screen = Tk()
Screen.title("Language Translator")

text_to_translate = StringVar()
target_lang = StringVar()

def Translate():
    translation = translator.translate(text_to_translate.get(), dest=target_lang.get())
    OutputVar.set(translation.text)
    PronunciationVar.set(translation.pronunciation)

def SpeechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recognized_text = r.recognize_google(audio)
        text_to_translate.set(recognized_text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

Label(Screen,text="Enter Target Language").grid(row=0,column =0)
TextBox = Entry(Screen,textvariable=target_lang, width=50).grid(row=0,column = 1)

Label(Screen,text="Enter Text").grid(row=1,column=0)
TextBox = Entry(Screen,textvariable=text_to_translate, width=50).grid(row=1,column = 1)


Label(Screen,text="Output Text").grid(row=3,column =0)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar, width=50).grid(row=3,column = 1)

Label(Screen,text="Pronunciation").grid(row=4,column=0)
PronunciationVar = StringVar()
TextBox = Entry(Screen,textvariable=PronunciationVar, width=50).grid(row=4,column=1)

B1 = Button(Screen, text="Translate", command=Translate, relief=GROOVE).grid(row=5, column=1, columnspan=3)
B2 = Button(Screen, text="Speak", command=SpeechToText, relief=GROOVE).grid(row=2, column=1, columnspan=3)

mainloop()
