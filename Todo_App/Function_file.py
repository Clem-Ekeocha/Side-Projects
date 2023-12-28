"""
Functions File necessary for the GUI development
"""
FILEPATH = "todos.txt"


def get_todos():
    """ Read a text file and return the list of to-do items. """
    with open('todos.txt', 'r') as file_local:
        todos_in_def = file_local.readlines()
    return todos_in_def


def write_todos(todos_arg, filepath = FILEPATH):
    """ Write the to-do items in the text file. """
    with open(filepath, 'w') as file_local2:
        file_local2.writelines(todos_arg)


