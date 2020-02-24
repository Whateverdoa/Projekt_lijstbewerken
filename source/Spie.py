import pandas as pd
import os
import PySimpleGUI as sg

# sg.change_look_and_feel('BluePurple')	# Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('vul pad en filenaam in')],
#             [sg.Text('hier:'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]
#
# # Create the Window
# window = sg.Window('csv file invoer ', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):	# if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
#
# window.close()

path = os.getcwd
# ordernummer = values[0]
# print(ordernummer)

myfile = "file_in\deel2.csv"
output_file = r"bestanden\test.csv"
output_begin_eind = r"bestanden\test_be.csv"

# pad="file_out"
# try:
#     os.mkdir(pad)
# except OSError as error:
#     print("check")


# pad = os.path.join('C:\\','Users','mike','PycharmProjects','Projekt_lijstbewerken','source', myfile)
pad = os.getcwd() + "\\" + myfile
pad_out = os.path.join('C:\\Users\\mike\\PycharmProjects\\Projekt_lijstbewerken\\' + output_file)
pad_begin_eind = os.path.join('C:\\Users\\mike\\PycharmProjects\\Projekt_lijstbewerken\\' + output_begin_eind)

print(pad)
# print(pad_out)
banen = 9
rolwikkel = 9

df = pd.read_csv(pad)
print(len(df)//1000)
baan = len(df)//1000
print(f'baan = {baan} || wikkel ={rolwikkel}')

# dit is file die ingelezen wordt
with open(pad, "r", encoding="utf-8") as target:
    readline = target.readlines()

# hier word een nieuwe file met wikkel gemaakt
with open(pad_out, "w", encoding="utf-8") as target, open(pad_begin_eind, "w", encoding="utf-8") as targetBE:

    vulling = ".;stans.pdf;" * banen + "\n"  ###

    target.writelines(readline[0:10])                              #------> inloop
    target.writelines(vulling * 140)    #------> inloop

    beginblok = 1
    eindblok = 1001

    for wikkel in range(baan):
        target.writelines(vulling * rolwikkel)
        target.writelines(readline[beginblok:eindblok])

        targetBE.writelines(readline[beginblok:beginblok+1])
        targetBE.writelines(readline[eindblok-1:eindblok])

        beginblok += 1000
        eindblok += 1000

    target.writelines(vulling * 140)   #---->  uitloop
    target.writelines(readline[-10:])                             #---->  uitloop


print(f"done file in  {pad_out}")
print(f"done BE {pad_begin_eind}")
