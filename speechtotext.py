# This is the basic and quick efficient way to complete the speech to text requirement
import speech_recognition as sr
import sounddevice as sd
import wavio #this is used to convert mp3 file to wav
import os
# as we are using google speech recognizer so internet connection is required.
fps=44100  #flash per second
duration=3 #this is in sec.
print("Listing....")

recording=sd.rec(duration*fps,samplerate=fps,channels=2)
sd.wait()
print("processing..")
wavio.write('output.wav',recording,fps,sampwidth=2)
rec=sr.Recognizer()
audioF='output.wav'

with sr.AudioFile(audioF) as sourceF:
    audio=rec.record(sourceF)
    print("File Reading")

print("File test is: ")
try:
    text=rec.recognize_google(audio)
    print(text)

except Exception as e:
    print(e)
#removing the unwanted wav audio file.
os.remove('output.wav')
