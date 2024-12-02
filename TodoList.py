#To-Do List project
from operator import index
import json


#Variables
Task = []
Tasks = []
operation = 0

#Functions
def createTask():
    follow = 1
#Create a bucle to repit while "do yo want add new task" its say "okey see you later" or similar thinks
    while follow == 1:
        newTask = input("Enter your new Task!: ")
        Task.append(newTask) #add newTask in a new task list

        state = input("\n|-- We recommend use 'Pendient' or 'completed' word. --|\nEstate of your task?: ")
        Task.append(state) #add state of newTask
        Tasks.append(Task[:])  # add new task list (no reference, its COPY of Task) with its state in Tasks (it contain all tasks)

        Task.clear() #clear task list for add new task list in Tasks (it contain all tasks)

        follow = int(input("\nDo You need add a new task?: \nPress [1] for YES\nPress [0] for NO: "))
        if follow != 1:
            break
    saveTasks()


def showTasks():
    y = 1
    for t in Tasks:
        print("\n    Task N",y,"   ")
        print("To do: ",t[0])
        print("Estate: ",t[1])
        y+=1
    if Tasks == []:
        print("\nYou dont have any task!\n")

def deleteTask():
    print("\n|-- We recommending look yours task first before delete something --|")
    showTasks()
    selector = int(input("\n|-- Which one you wan delete? --|\nEnter number of task you wan delete: "))
    Tasks.pop(index(selector-1))
    saveTasks()


def changeStatus():

    # add solution in case of dont have anyone list. e.g: 0 tasks
    print("\n|-- We recommending look yours task first before delete something --|")
    showTasks()
    selector = int(input("\n|-- Which task you wan change its Status? --|\nEnter number of task you wan change status: "))
    Tasks[selector-1][1] = input("What is the new status of this stask: ")
    saveTasks()


def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(Tasks, file, indent=4)


def loadTasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Damaged file or not JSON valid ")
        return[]


def showMenu():
    print("---What do you want?---")
    operation = int(input("[1] - Create a new task\n"
                          "[2] - Show your Tasks\n"
                          "[3] - Change status of some task\n"
                          "[4] - Delete Task\n"
                          "[5] - Exit: "))
    return operation

#MAIN
print("[WELCOME TO YOU TO DO LIST]")
Tasks = loadTasks()
operation = showMenu()

while operation != 5:
    #Tasks = loadTasks()
    if operation == 1:
        createTask()
    if operation == 2:
        showTasks()
    if operation == 3:
        changeStatus()
    if operation == 4:
        deleteTask()
    operation = showMenu()

print("See you later!")