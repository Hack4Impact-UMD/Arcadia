import os
import PySimpleGUI as sg
from pdf_creation import generate_PDF 

sg.theme('Green')

# Get paths of files
pl_layout = [[sg.Text('Product List')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Final CSV')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Benefits CSV')],
            [sg.Input(), sg.FileBrowse()],
            [sg.Text('Download Location')],
            [sg.Input(), sg.FolderBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Arcadia Report Generator', pl_layout)

event, values = window.read()
if event == 'OK':
     # Creates a folder caled Customer Reports to put the customer reports
     # in if the folder doesn't already exist
     if not os.path.exists(f"{values[3]}/Customer Reports"):
          os.mkdir(f"{values[3]}/Customer Reports")
     generate_PDF(values[0], values[1], values[2], values[3])

window.close()