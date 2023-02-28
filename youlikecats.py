# code sourced from https://realpython.com/pysimplegui-python/#creating-simple-applications

import PySimpleGUI as sg

# Define the layout

layout = [
    #Text command to ask a question
    [sg.Text('Do you want to see an image of a cat?')],
    #Checkbox command for yes, yes will make a image come up
    [sg.Checkbox('Yes', key='-SHOW-IMAGE-')],
    [sg.Image(key='-IMAGE-', visible=False)],
    [sg.Button('Exit')],
    [sg.Button('Continue...')]
]

# Create the window
window = sg.Window('Checkbox with image example', layout)

# Event loop
while True:
    # if exit button is clicked it will close the window
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if values['-SHOW-IMAGE-']:
        # Shows the image
        window['-IMAGE-'].update(filename='capycat.jfif', visible=True)
    else:
        # Hides the image
        window['-IMAGE-'].update(visible=False)

# Close the window
window.close()