# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list!")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{idx}. {task['name']} [{status}]")

# Function to add a task
def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")

# Function to mark a task as complete
def mark_task_complete():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['name']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
