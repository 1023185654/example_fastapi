class UserInfo:
    def __init__(self):
        self.user_info = {}

    def insert_user(self, user_id, **k):
        self.user_info[user_id] = {**k}

    def get_user(self, user_id):
        return self.user_info.get(user_id, {})

    def update_user(self, user_id, **k):
        self.user_info.update({user_id: {**k}})


user_info = UserInfo()
