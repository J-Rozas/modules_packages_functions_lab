def select_option():
    return input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")

def get_user_description():
    return input("Enter task description to search for: ")

def get_user_time():
    return int(input("Enter task duration: "))

def get_user_task():
    input("Enter task description to search for: ")

def get_past_tasks_preference():
    return True if input("Do you want to load the previous tasks (y/any other key)?: ") == "y" else False