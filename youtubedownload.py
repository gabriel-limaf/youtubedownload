import PySimpleGUI as sg
from pytube import YouTube


def menu():  # Janela 1
    sg.theme('Dark Blue 3')
    layout = [[sg.Text('URL do vídeo')],
              [sg.InputText(key='URL')],
              [[sg.Text('Onde deseja salvar seu vídeo?')],
               [sg.Input(), sg.FolderBrowse(key='path_save')]],
              [sg.Button('OK'), sg.Button('Cancelar')]]
    return sg.Window('Download de vídeos YouTube', layout=layout, finalize=True)


def sucesso():  # Janela 2
    sg.theme('DarkGreen')
    layout = [[sg.Text('Download realizado com sucesso !')],
              [sg.Button('Voltar'), sg.Button('Cancelar')]]
    return sg.Window('SUCESSO', layout=layout, size=(300, 100), finalize=True)


janela1, janela2 = menu(), None
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Cancelar':
        break
    if window == janela1 and event == 'OK' and values['URL'] != '' and values['path_save'] != '':
        yt = YouTube(values['URL'])
        video = yt.streams.get_highest_resolution()
        video.download(values['path_save'])
        janela1.close()
        janela2 = sucesso()
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1 = menu()
    if window == janela2 and event == 'Cancelar':
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
