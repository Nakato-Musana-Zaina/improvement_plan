class Tasks:
    def __init__(self, id, title, priority, deadline):
        self.id =id
        self.priority = priority
        self.deadline = deadline
        self.title = title

    

    def adds_tasks(id, title, priority,deadline):
        tasks = []

        global tasks
        first_task = Tasks(id,title,priority,deadline)
        tasks.append(first_task)
        tasks.sort(key=lambda x: (-x.priority,-x>deadline))


    def deletes_tasks(id):
        global tasks
        tasks =[task for task in tasks if task.id!=id]



        