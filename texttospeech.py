import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

layout = [ 
    [sg.InputText(key="-input-"),sg.Button("Speak")],
     [sg.Text('Select Voice Type:'),sg.Radio("Male", "RADIO", default=True, key="-male-"),sg.Radio("Female", "RADIO", key="-female-")], 
]

window = sg.Window("Text to Speech App", layout,background_color='pink')
voice_type=engine.getProperty('voices')
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Speak":
        text = values["-input-"]
        if values["-male-"]:
            engine.setProperty('voice', voice_type[0].id)  
        elif values["-female-"]:
            engine.setProperty('voice', voice_type[1].id)  
        engine.say(text)
        engine.runAndWait()
window.close()