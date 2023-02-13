import PySimpleGUI as sg

sum=0
multiplier = 1
sg.theme("Black")

layout=[
    [sg.Text("Basic Calculator")],
    [sg.Text("Enter number"), sg.Input(size=(10,6),key="INPUT",do_not_clear=False)],
    [sg.Button("+",key="ADD",size=(5,2)),sg.Button("-",key="SUB",size=(5,2)),sg.Button("÷",key="DIV",size=(5,2)),sg.Button("x",key="MULTI",size=(5,2))],
    [sg.Text("Result",key="RESULT")]
    ]

window = sg.Window("Demo Calculator",layout,size=(300,200),element_justification='c')

while True:
    event,values=window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'ADD':
        sum=sum+int(values['INPUT'])
        window["RESULT"].update(str(sum))
    if event == 'SUB':
        sum=sum-int(values['INPUT'])
        window["RESULT"].update(str(sum))
    if event == 'MULTI':
        multiplier = multiplier * sum * int(values['INPUT'])
        window['RESULT'].update(str(multiplier))
    if event == "DIV":
        sum=sum/int(values['INPUT'])
        window["RESULT"].update(str(sum))
        
window.close()