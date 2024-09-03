import json

# Class to represent a Task
class Task:
    def __init__(self, description, completed=False):
        self.description = description  # Task description
        self.completed = completed      # Task completion status

    def __str__(self):
        # Return a string representation of the task, showing completion status
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

# Function to save tasks to a JSON file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        # Convert Task objects to dictionaries and save them to the file
        json.dump([task.__dict__ for task in tasks], file)

# Function to load tasks from a JSON file
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            # Load tasks data from the file and create Task objects
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        # Return an empty list if the file does not exist
        return []

# Function to print the menu options
def print_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Main function to run the To-Do List application
def main():
    tasks = load_tasks()  # Load existing tasks from the file

    while True:
        print_menu()  # Display the menu options
        choice = input("Choose an option: ")

        if choice == '1':
            # Add a new task
            description = input("Enter task description: ")
            if description:
                tasks.append(Task(description))  # Create a new Task and add it to the list
                save_tasks(tasks)  # Save the updated task list to the file
            else:
                print("Task description cannot be empty.")  # Handle empty description

        elif choice == '2':
            # View all tasks
            if not tasks:
                print("No tasks available.")  # Notify if no tasks are present
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")  # Print each task with its index

        elif choice == '3':
            # Update an existing task
            task_id = int(input("Enter task number to update: ")) - 1
            if 0 <= task_id < len(tasks):
                print("Current task:", tasks[task_id])  # Show the current task
                update_choice = input("Would you like to update (d)escription or (c)ompletion status? (Enter 'd' or 'c'): ").strip().lower()
                
                if update_choice == 'd':
                    # Update task description
                    new_description = input("Enter new task description: ")
                    if new_description:
                        tasks[task_id].description = new_description  # Set new description
                        save_tasks(tasks)  # Save the updated task list
                    else:
                        print("Task description cannot be empty.")  # Handle empty description
                
                elif update_choice == 'c':
                    # Toggle completion status
                    tasks[task_id].completed = not tasks[task_id].completed
                    save_tasks(tasks)  # Save the updated task list
                
                else:
                    print("Invalid choice.")  # Handle invalid update choice
                
            else:
                print("Invalid task number.")  # Handle invalid task number

        elif choice == '4':
            # Delete a task
            if not tasks:
                print("No tasks available to delete.")  # Notify if no tasks are present
                continue
            
            task_id = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_id < len(tasks):
                tasks.pop(task_id)  # Remove the task from the list
                save_tasks(tasks)  # Save the updated task list
            else:
                print("Invalid task number.")  # Handle invalid task number

        elif choice == '5':
            # Exit the program
            break

        else:
            print("Invalid choice, please try again.")  # Handle invalid menu choice

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
