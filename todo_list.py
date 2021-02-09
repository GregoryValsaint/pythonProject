from datetime import datetime

class Task:

    def __init__(self):
        self.id = ""
        self.content = input("")
        self.done = False
        self.created_date = datetime.now()


    def display_task(self):
        print(f"Tache {self.id} :  {self.content}   fait le:  % {self.created_date}")

class Manage(Task):
    def __init__(self):
        self.list = []
        self.content = input("")
        self.response = input('')

    def question(self):
        while self.response == "exit":
            if self.response == "list":
                self.display_list()
            if self.response == "delete":
                self.delete_task()
            if self.response == "add":
                self.add_task()
            if self.response == "end":
                self.validate_task()
            if self.response == "help":
                self.help_me()


    def display_list(self):
        print(self.list)

    def add_task(self):
        task = input('Entrez un tache:')
        new_task = Task()
        new_task.content = task
        list.append(new_task)



    def delete_task(self):
        self.list.append()

    def validate_task(self):
        self.list.append()
    def help_me(self):
        print('''- list -> liste les messages\n
                - delete -> demande l'id d'une tache pour la supprimer\n
                - add -> demande un texte et l'ajoute dans une nouvelle tâche\n
                - end -> demande l'id d'une tâche pour la valider\n
                - help -> message d'aide liste de commandes\n
                - exit -> sortir du programme\n
        ''')


my_task = Task()
my_task.display_task()

my_command = Manage()
my_command.question()