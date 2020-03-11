
import pandas as pd
from pathlib import Path
import PySimpleGUI as sg

from SLI_csv_O.tool_defenities import one, two

one()
two()

#  todo gui needs to ask for variables:
#  todo where and what file needs to be processed
#  todo aantal_per_rol = 50
#   todo mes = 4
#   todo wikkel = 10
#   todo inloop_uitloop_Y_waarde = 8 (will be used *10) and used to produce real inloop_uitloop data
#    save these values cq state of gui in a file named

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [sg.OK(), sg.Cancel()] ]

window = sg.Window('Get filename example', layout)
event, values = window.read()
window.close()

sg.Popup(event, values[0])






