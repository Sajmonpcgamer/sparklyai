import gtts
import requests
import speech_recognition as sr
import os
import webbrowser
from sys import argv as args
from sys import platform as SYSPLAT
from playsound import playsound

debug = False
if "--debug" in str(args): debug = True
r = sr.Recognizer()
l = "en"
if "--lang" in str(args):
  l = str(input("Language: ")).lower()
url = "http://" + str(input("Server: ")) + "/"
def speak(words:str, language:str="sk"):
  if words == "" or words == None:
    if debug: print("[gTTS]: No voice to speak, returning")
  if debug: print("[gTTS]: Text: " + words)
  if debug: print("[gTTS]: Converting words to Text")
  tts = gtts.gTTS(words, lang=language)
  if debug: print("[gTTS]: Saving Text")
  tts.save("speech.mp3")
  if debug: print("[gTTS]: Playing Text")
  if "win32" in SYSPLAT.lower():
    playsound(f"{os.getcwd()}\\speech.mp3")
  else:
    playsound(f"{os.getcwd()}/speech.mp3")
  if debug: print("[gTTS]: Finished!")
  if debug: print("[os]: Deleting speech")
  os.remove("speech.mp3")
  if debug: print("[os] File deleted!")

def get_voice(duration:float=1):
  try:
    if debug: print("[sr]: Opening Microphone()")
    with sr.Microphone() as src2:
      r.adjust_for_ambient_noise(src2, duration=duration)
      if debug: print("[sr]: Recording Voice")
      audio2 = r.listen(src2)
      if debug: print("[sr]: Sending Voice to Google")
      txt = r.recognize_google(audio2)
      txt = txt.lower()
      if debug: print("[sr]: Returning Text")
      return txt

  except sr.RequestError as e:
    print(f"Could not request results; {e}")
  except sr.UnknownValueError:
    print("Unknown error occured")

while True:
  if "--text" in str(args):
    t = str(input("> ")).replace("?", "").replace("&", "").replace(" ", "_")
    if not t == "" and not t == None and not t == " " and not t == " ":
      if debug: print("[requests]: Sending question to server")
      resp = requests.request(url=f"{url}?txt={t}&lang={l}", method="GET").text
      if "Internal Server Error" in resp:
        print("Error")
      elif "EXEC: " in resp:
        resp = resp.replace("EXEC: ", "")
        if "WEB: " in resp:
          resp = resp.replace("WEB: ", "")
          webbrowser.open(resp)
      else:
        if debug: print("[requests]: Got response")
        print(resp)
        speak(resp, language=l)
