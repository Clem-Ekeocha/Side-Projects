import streamlit as st
import Function_file as ff

todos = ff.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    ff.write_todos(todos)

st.title("Clement's Todo App")
st.subheader("This is my Todo App")
st.write("This App is to increase your productivity")

todos_to_remove = []  # Create a list to store todos to be removed

for i, todo in enumerate(todos):
    # Use a combination of index and todo value as a unique identifier
    checkbox = st.checkbox(f"{i + 1}. {todo}", key=f"{i}_{todo}")
    if checkbox:
        todos_to_remove.append(todo)

# Remove todos outside the loop to avoid modifying the list while iterating
for todo in todos_to_remove:
    todos.remove(todo)

# Update the todos after removal
ff.write_todos(todos)

st.text_input(label="Enter a Todo Below", placeholder="Add new todo..",
              on_change=add_todo, key="new_todo")
