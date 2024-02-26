class User:
    def __init__(self,username,password):
        self._username = username
        self._password = password
        self._online = True

    # User shouldn't be able to follow/unfollow himself
    def follow(self,user):
        pass

    def unfollow(self,user):
        pass

    def publish_post(self):
        pass

    def print_notifications(self):
        pass

    def __str__(self):
        return f"{self._username}"