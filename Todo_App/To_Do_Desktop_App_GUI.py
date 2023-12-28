"""
Creating the GUI of the To-do App built
"""
import Function_file as ff  # This is from an external file
import PySimpleGUI as psg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
psg.theme("DarkPurple4")

title_clock = psg.Text("", key='clock')
label = psg.Text("Type in a Todo")  # Create a Title Instruction
input_box = psg.InputText(tooltip="Enter Todo", key='todo')  # Create an input box with tooltip
add_button = psg.Button("Add")  # Create the add button to add to the window
list_box = psg.Listbox(values=ff.get_todos(), key='todos',
                       enable_events=True, size=[20, 10])
edit_button = psg.Button("Edit")
delete_button = psg.Button("Delete")
exit_button = psg.Button("Exit") 

window = psg.Window('My To-do App',
                    layout=[[title_clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, delete_button],
                            [exit_button]],
                    font=('Helvetica', 20))   # Title and row-level arrangement  of the window app. Must Always be a list in a list --very important

while True:
    event, values = window.read(timeout=200)  # Displays window on the screen
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = ff.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            ff.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = ff.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                ff.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Select an item first",
                          font =('Helvetica', 20))
        case "Delete":
            try:
                todo_to_delete = values['todos'][0]
                todos = ff.get_todos()
                todos.remove(todo_to_delete)
                ff.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                psg.popup("Select an item first",
                          font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case psg.WIN_CLOSED:
            break


window.close()


