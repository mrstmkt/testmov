import speech_recognition as sr
fileName = "IosaWkNnRYw.wav"
r = sr.Recognizer()
 
with sr.AudioFile(fileName) as source:
    audio = r.record(source)
 
text = r.recognize_google(audio, language='ja-JP')
 
print(text)