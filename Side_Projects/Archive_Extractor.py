
import PySimpleGUI as psg
from Archive_Extractor_Backend import extract_archive as ea

psg.theme("Black")

label1 = psg.Text("Select Archive: ")
input1 = psg.Input()
choose_button1 = psg.FileBrowse("Choose", key='archive')

label2 = psg.Text("Select Destination Dir: ")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key='folder')

extract_button = psg.Button("Extract")
output_label = psg.Text(key="output", text_color='green')

window = psg.Window("Archive Extractor",
                    layout=[[label1, input1, choose_button1],
                              [label2, input2, choose_button2],
                              [extract_button, output_label]])
while True:
    event, values = window.read()
    archivepath = values['archive']
    dest_dir = values["folder"]
    ea(archivepath,dest_dir )
    window["output"].update(value='Extraction Completed')

window.close()