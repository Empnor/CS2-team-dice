import PySimpleGUI as sg

sg.theme('DarkAmber')   


layout = [
            [sg.Button('Ok')] 
            ]

# Create the Window
window = sg.Window('testi', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'ok': # if user closes window or clicks cancel
        break
    sg.Text[('aafg')]

window.close()