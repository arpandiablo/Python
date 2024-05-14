import win32com.client as wincl

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)

list_speak = []
while True:
    list_speak.append(input("Enter The Text You Want To Convert Into Speech : "))
    for i in list_speak:
        spk.Speak(i)
    if i == "exit":
        break