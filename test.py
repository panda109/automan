'''
Created on 2010/12/20

0 Mon Dec 20 15:36:16 2010

@author: panda.huang
'''
#pip install pipwin
#pipwin install pyaudio

import speech_recognition
import time
import os
import pyaudio
import wave              #

if __name__ == '__main__':

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source: 

        print("begin:")                        # print
        r.adjust_for_ambient_noise(source)     #
        audio = r.listen(source)

    try:
        Text = r.recognize_google(audio, language="zh-TW")     

    except r.UnknowValueError:
        Text = "can't trans"
    except r.RequestError as e:
        Text = "can't trans{0}".format(e)

    print( Text )
