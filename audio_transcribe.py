# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 00:58:13 2016

@author: prathmesh.savale
"""

import glob
import os
#import ctypes
import speech_recognition as sr


filenames = glob.glob('/home/cloudera/git/speechtotext/segmentedwavfiles/*.wav')

for i in range(0,len(filenames)):
    print(filenames[i])
    
    AUDIO_FILE = filenames[i]
    
    test = filenames[i].split('/', 6)[6]
    
    test2 = test.split('_',2)[2]
    test3 = test2.split('_',2)[1]
    speaker_name = test3.split('.',2)[0]
    #print(speaker_name)
    
    filename = filenames[i].split('/',6)[6]
    foldername = filename.split('_',2)[0]
    
    filename = foldername +speaker_name+ '.txt'
    #print(filename)
    
    
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file




    #try:
       # with open(filename) as file:
            #f=open(filename,"a")
        # do whatever
            
            
    #except IOError:
    if not os.path.exists("transcribed_files/"+foldername):
        os.makedirs("transcribed_files/"+foldername)        
            
            
    f = open("transcribed_files/"+foldername+"/"+filename,"a")
    f.write(speaker_name+" spoke:")
        #f.write(speaker_name + " said: ")
    try:
            
        f.write(r.recognize_google(audio))
        f.write("\n\n")
            #print(r.recognize_google(audio))
    except sr.UnknownValueError:
        f.write("Google Speech Recognition could not understand audio")
        f.write("\n\n")
    except sr.RequestError as e:
        f.write("Could not request results from Google Speech Recognition service; {0}".format(e))
        f.write("\n\n")
    f.close()
    

       


