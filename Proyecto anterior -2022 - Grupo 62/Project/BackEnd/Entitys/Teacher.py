from User import User


class Teacher(User):
    def __init__(self, id_user, first_name, last_name, username, email, password, active, user_git, user_linkedin, dni):
        super().__init__(id_user, first_name, last_name, username,
                         email, password, active, user_git, user_linkedin)
        self.dni = dni

    def upload_videos(self):
        pass
