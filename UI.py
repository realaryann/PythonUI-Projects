import PySimpleGUI as sg

def add(num1, num2):
    sum=num1+num2
    return (str(sum))

sg.theme('Black')

layout=[
    [sg.Text("This is an Addition GUI")],
    [sg.Text("Enter the first number: "), sg.Input(size=(10,6), key="INPUT1",do_not_clear=False)],
    [sg.Text("Enter the first number: "), sg.Input(size=(10,6), key="INPUT2",do_not_clear=False)],
    [sg.Button("Compute",key="COMPUTE")],
    [sg.Text("OUTPUT",key="OUTPUT")]
    ]

window=sg.Window("Addition",layout,size=(250,150))

while True:
    event,values=window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'COMPUTE':
        result = add(int(values['INPUT1']),int(values['INPUT2']))
        window["OUTPUT"].update(str(result))
        

window.close()