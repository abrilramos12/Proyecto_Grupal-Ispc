
class User:
    def __init__(self,id_user, first_name, last_name, username, email, password, active, user_git, user_linkedin):
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.active = active
        self.user_git = user_git
        self.user_linkedin = user_linkedin

    def bookmark(self):

    def let_comment(self):

    def register(self):

    def login(self):

    def logout(self):

class Teacher(User):

    def upload_videos(self):


class Student(User):

