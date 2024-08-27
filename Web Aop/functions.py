FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos( todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
