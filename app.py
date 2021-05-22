import os
import PySimpleGUI as sg
import shutil
from datetime import date
from pdf_creation import generate_PDF 

# Sets window color/theme
sg.theme('LightGreen3')

# Get paths of files
report_layout = [[sg.Text('Product List', font = 'Arial 18')],
            [sg.Input(font = 'Arial 16'), sg.FileBrowse(font = 'Arial 18')], 
            [sg.Text('Customer Purchases', font = 'Arial 18')],
            [sg.Input(font = 'Arial 16'), sg.FileBrowse(font = 'Arial 18')], 
            [sg.Text('Benefits CSV', font = 'Arial 18')],
            [sg.Input(font = 'Arial 16'), sg.FileBrowse(font = 'Arial 18')],
            [sg.Text('Download Location', font = 'Arial 18')],
            [sg.Input(font = 'Arial 16'), sg.FolderBrowse(font = 'Arial 18')], 
            [sg.OK(font = 'Arial 18'), sg.Cancel(font = 'Arial 18')]] 

window = sg.Window('Arcadia Report Generator', report_layout)

event, values = window.read()
# window.maximize()
if event == 'OK':
     # Creates a folder caled Customer Reports to put the customer reports
     # in if the folder doesn't already exist
     today = date.today()
     date = today.strftime("%b-%d-%Y")

     if not os.path.exists(f"{values[3]}/Customer Reports {date}"):
          os.mkdir(f"{values[3]}/Customer Reports {date}")
     if not os.path.exists(f"{values[3]}/Pie-Charts"):
          os.mkdir(f"{values[3]}/Pie-Charts")
     generate_PDF(values[0], values[1], values[2], values[3], date)
     shutil.rmtree(f"{values[3]}/Pie-Charts")

window.close()