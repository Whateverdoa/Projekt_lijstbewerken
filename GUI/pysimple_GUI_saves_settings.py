import PySimpleGUI as sg

'''
    Example of GUI
'''


def main():
    sg.change_look_and_feel('DarkBlue12')

    layout = [
        [sg.Text('VDP invul formulier', size=(30, 1), font="arial", text_color="orange")],

        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()],

        [sg.InputText('202012345', key='ordernummer_1'), sg.Text('Ordernummer')],
        [sg.InputText('', key='totaal'),sg.Text('Totaal')],

        # [sg.InputText('', key='pre'), sg.Text('Pre')],
        [sg.InputText('', key='begin_1'),sg.Text('Begin nummer')],
        # [sg.InputText('', key='post'), sg.Text('Post')],

        [sg.InputText('', key='aantal'),sg.Text('Aantal')],
        [sg.InputText('', key='aantal_per_rol'),sg.Text('Aantal per rol')],

        [sg.InputText('', key='wikkel'),sg.Text('Wikkel')],
       # run button

        # this saves the input information
        [sg.Text('_' * 80)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]

    ]

    window = sg.Window('Nummer generator 2.0 form', layout, default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = window.read()

        if event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)

            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event in ('Exit', None):
            break


        print("test")

    window.close()


if __name__ == '__main__':
    main()

