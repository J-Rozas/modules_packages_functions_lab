# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    list_of_uncompleted = []

    for task in list:
        if task["completed"] == False:
            list_of_uncompleted.append(task)

    return list_of_uncompleted

## Get a list of completed tasks
def get_completed_tasks(list):
    list_of_completed = []

    for task in list:
        if task["completed"] == True:
            list_of_completed.append(task)
    
    return list_of_completed

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    valid_time_tasks = []

    for task in list:
        if task["time_taken"] >= time:
            valid_time_tasks.append(task)
    
    return valid_time_tasks

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    if status == True:
        return get_completed_tasks(list)
    else:
        return get_uncompleted_tasks(list)

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

