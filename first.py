#Python program for creation of To-do-list 
import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []

def print_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            if description:
                tasks.append(Task(description))
                save_tasks(tasks)
            else:
                print("Task description cannot be empty.")

        elif choice == '2':
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == '3':
        
            task_id = int(input("Enter task number to update: ")) -1
            if 0 <= task_id < len(tasks):
                print("Current task:", tasks[task_id])
                update_choice = input("Would you like to update (d)escription or (c)ompletion status? (Enter 'd' or 'c'): ").strip().lower()
                
                if update_choice == 'd':
                    new_description = input("Enter new task description: ")
                    if new_description:
                        tasks[task_id].description = new_description
                        save_tasks(tasks)
                    else:
                        print("Task description cannot be empty.")
                
                elif update_choice == 'c':
                    tasks[task_id].completed = not tasks[task_id].completed
                    save_tasks(tasks)
                
                else:
                    print("Invalid choice.")
                
            else:
                print("Invalid task number.")

        elif choice == '4':
            if not tasks:
                print("No tasks available to delete.")
                continue
            
            task_id = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_id < len(tasks):
                tasks.pop(task_id)
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == '5':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
