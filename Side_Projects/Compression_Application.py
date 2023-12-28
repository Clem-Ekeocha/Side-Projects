"""
The code below represents the simple gui development of a file compressor
using python and the PySimpleGUI module
"""
import PySimpleGUI as psg
from daily_journal.zip_creator import make_archive

label1 = psg.Text("Select file to compress")
input1 = psg.Input()
choose_button1 = psg.FilesBrowse("Choose", key = "files")  # Build a Choose Button to open local directory to select from.

label2 = psg.Text("Select destination folder")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key = "folder")  # Build a Choose Button to open local directory to store compress files.

compress_button = psg.Button("Compress")
success_label = psg.Text(key='output', text_color = "green")

window = psg.Window("Clement's File Compressor",
                    layout=[[label1, input1, choose_button1],  # Row one of the app layout
                            [label2, input2, choose_button2],  # Row 2 of the app layout
                            [compress_button, success_label]])                # Row 3 of the app layout showing the compress button

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Successful")

window.close()
