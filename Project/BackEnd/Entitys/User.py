class User:
    def __init__(self, id_user, first_name, last_name, username, email, password, active, role, create_time, user_git, user_linkedin):
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.active = active
        self.role = role
        self.create_time = create_time
        self.user_git = user_git
        self.user_linkedin = user_linkedin

    def bookmark(self):
        pass

    def let_comment(self):
        pass

    def register(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass
