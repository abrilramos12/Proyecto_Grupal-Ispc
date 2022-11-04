from User import User


class Student(User):
    def __init__(self, id_user, first_name, last_name, username, email, password, active, user_git, user_linkedin, user_vip):
        super().__init__(id_user, first_name, last_name, username,
                         email, password, active, user_git, user_linkedin)
        self.user_vip = user_vip
