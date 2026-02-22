import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    todo_key = f"Todo #{index}" #str(index)+todo
    checkbox = st.checkbox(todo, key=todo_key)
    if checkbox:
        # Remove the item from the todo list
        todos.pop(index)

        # Update the text file
        functions.write_todos(todos)

        # Remove the checked item from the session state dictionary
        del st.session_state[todo_key]
        st.rerun()

st.text_input(label="Enter a ToDo: ",placeholder="Add a new todo...", on_change=add_todo, key="new_todo")