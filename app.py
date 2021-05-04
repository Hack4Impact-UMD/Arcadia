import PySimpleGUI as sg
from pdf_creation import generate_PDF 

# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

# # Create the Window
# window = sg.Window('PDF Report Generator', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

# window.close()

sg.theme('Dark Blue 3')  # please make your creations colorful

# get paths of files
pl_layout = [[sg.Text('Product List')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Final CSV')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Benefits CSV')],
            [sg.Input(), sg.FileBrowse()],
            [sg.Text('Download Location')],
            [sg.Input(), sg.FolderBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', pl_layout)
# window1 = sg.Window('Get filename example', pl_layout)

event, values = window.read()
if event == sg.OK():
    generate_PDF(values[0], values[1], values[2], values[3])
window.close()
# print(values)