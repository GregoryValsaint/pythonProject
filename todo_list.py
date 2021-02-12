from datetime import datetime

class Task:

    def __init__(self, content):
        self.content = content
        self.done = False
        self.created_date = datetime.now()

class Manage(Task):
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_text =input("Nom de la tâche: ")
        task = Task(task_text)
        self.tasks.append(task)

    def remove_task(self):
        try:
            task_id = int(input("Id de la tâche à supprimer: "))
            if 0 <= task_id < len(self.tasks):
                self.tasks.pop(task_id)
        except ValueError:
            print("Veuillez rentrer un nombre entre 0 et %i" % (len(self.tasks) - 1))

    def validate_task(self):
        task_id = int(input("Id de la tâche à valider: "))
        self.tasks[task_id].done = True

    def list_tasks(self):
        template = "{id} - {date} - {content}[{done}]"
        for task in self.tasks:
            print(template.format(
                id=0,
                date=task.created_date,
                content=task.content,
                done=task.done
            ))

class UserInterface:
    def __init__(self):
        self.manager = Manage()
        self.loop = True

    def run(self):
        functions = {
            "add": self.manager.add_task,
            "remove": self.manager.remove_task,
            "validate": self.manager.validate_task,
            "list": self.manager.list_tasks,
            "exit": self.manager.exit,
            "help": self.manager.display_help,
        }

        self.loop = True
        while self.loop:
            user_input = input("Que voulez-vous faire ?\n")
            # if user_input == "add":
            #     self.manager.add_task()
            # elif user_input == "remove":
            #     self.manager.remove_task()
            # elif user_input == "validate":
            #     self.manager.validate_task()
            # elif user_input == "list":
            #     self.manager.list_tasks()
            # elif user_input == "exit":
            #     self.exit()
            # else:
            #     self.display_help()
            if(user_input in functions):
                functions[user_input]()
            else:
                self.display_help()

    def display_help(self):
        print('''Aide:
        ''')

    def exit(self):
        self.loop = False

# manager = Manage()
# manager.add_task()
# manager.add_task()
# manager.add_task()
# # manager.list_tasks()
# manager.remove_task()
# manager.validate_task()
# manager.list_tasks()


interface = UserInterface()
interface.run()

