import os
import PySimpleGUI as sg
from pdf_creation import generate_PDF 

# Sets window color/theme
sg.theme('LightGreen3')

# Get paths of files
report_layout = [[sg.Text('Product List')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Final CSV')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Benefits CSV')],
            [sg.Input(), sg.FileBrowse()],
            [sg.Text('Download Location')],
            [sg.Input(), sg.FolderBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Arcadia Report Generator', report_layout)

event, values = window.read()
# window.maximize()
if event == 'OK':
     # Creates a folder caled Customer Reports to put the customer reports
     # in if the folder doesn't already exist
     if not os.path.exists(f"{values[3]}/Customer Reports"):
          os.mkdir(f"{values[3]}/Customer Reports")
     generate_PDF(values[0], values[1], values[2], values[3])

window.close()