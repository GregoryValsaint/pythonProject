class User:
    def __init__(self):
        self.username = "Greg"
        self.__password = "super-secret"

    def say_hello(self):
        print(r"Salut \à tous")

    def display_pass(self):
        print(self.__password)

class Editor:
    def write_article(self):
        print("article ecrit")

class Admin(User):
    def test_method(self):
        self.write_article()

my_user = User()
my_user.say_hello()
print(my_user.username)
my_user.display_pass()
