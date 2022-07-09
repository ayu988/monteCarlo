import pyttsx3
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
voiceID = "french"
engine.setProperty('voice',voiceID)
# for voice in voices:
#     # to get the info. about various voices in our PC 
#     print("Voice:")
#     print("ID: %s" %voice.id)
#     print("Name: %s" %voice.name)
#     print("Age: %s" %voice.age)
#     print("Gender: %s" %voice.gender)
#     print("Languages Known: %s" %voice.languages)
# # print(rate)
def bolo(msg):
    engine.say(msg)
    engine.runAndWait()
bolo("My one xylon")
# import random
# import numpy as np
# import pandas as pd
# def removeDuplicate(arr):
#     return list(dict.fromkeys(arr))
# def discardKrdo(arr):
#     temp = []
#     for i in range(len(arr)):
#         if (arr[i]>= 3.12) and (arr[i]<= 3.15):
#             temp.append(arr[i])
#     return temp
# master = []
# print()
# for i in range(10000):
#     pin = 0
#     ptot = 0
#     for j in range(1000):
#         x = random.random()
#         y = random.random()
#         z = random.random()
#         if (x*x+y*y+z*z)**0.5 <= 1 :
#             pin += 1
#         ptot += 1
#         pi = 6*(pin/ptot)
#         master.append(pi)
# master.sort()
# master = discardKrdo(master)
# print(len(master))
# frame = pd.DataFrame({'pi-val': master})
# freq=pd.crosstab(index=frame['pi-val'],columns='count')
# print(freq)
# name = str(input("Enter file name: "))
# freq.to_csv(name)