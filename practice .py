

class Task:
    def __init__(self, id, title, priority, deadline):
        self.id = id
        self.title = title
        self.priority = priority
        self.deadline = deadline

    def __repr__(self):
        return f"Task({self.id}, {self.title}, {self.priority}, {self.deadline})"

tasks = []

def add_task(id, title, priority, deadline):
    global tasks
    task = Task(id, title, priority, deadline)
    tasks.append(task)
    # tasks.sort(key=lambda x: (-x.priority, -x.deadline))

def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task.id!= id]

def edit_task(id, title=None, priority=None, deadline=None):
    global tasks
    for task in tasks:
        if task.id == id:
            if title:
                task.title = title
            if priority:
                task.priority = priority
            if deadline:
                task.deadline = deadline
            break

def list_tasks():
    global tasks
    for task in tasks:
        print(task)

def main():
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Edit Task\n4. List Tasks\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            id = int(input("Enter task ID: "))
            title = input("Enter task title: ")
            priority = int(input("Enter task priority: "))
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            add_task(id, title, priority, deadline)
        elif choice == "2":
            id = int(input("Enter task ID to delete: "))
            delete_task(id)
        elif choice == "3":
            id = int(input("Enter task ID to edit: "))
            title = input("Enter new task title (leave blank to keep current): ")
            priority = int(input("Enter new task priority (leave blank to keep current): "))
            deadline = input("Enter new task deadline (leave blank to keep current): ")
            edit_task(id, title, priority, deadline)
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




        