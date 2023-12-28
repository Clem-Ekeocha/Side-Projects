
import streamlit as st
import Function_file as ff

todos = ff.get_todos()

st.title("Clement's Todo App")
st. subheader("This is my Todo App")
st.write("This is App is to increase your productivity")


for i, todo in enumerate(todos):
    # Use the index as a unique identifier for each checkbox
    st.checkbox(f"{i + 1}. {todo}")

st.text_input(label="Enter a Todo Below", placeholder="Add new todo..")



