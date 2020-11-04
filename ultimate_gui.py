import PySimpleGUI as sg

frame_layouts = [[[sg.Button('', size=(6, 3), key=(k, i, j), pad=(1, 1))
                   for j in range(3)]
                  for i in range(3)]
                 for k in range(9)]

layout = [[sg.Frame(str(j*3 + i), frame_layouts[j*3 + i], key=(j*3+i), pad=(6, 6), background_color="BLACK") for i in range(3)] for j in range(3)]

window = sg.Window('Frame with buttons', layout, background_color="BLACK")

while True:
    e, v = window.read()
    if e in (sg.WIN_CLOSED, 'Exit'):
        break
    print(e)
    window[e].update("", button_color=('black', 'white'))

window.close()
