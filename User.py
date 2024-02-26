from Post import PostFactory

class User:
    def __init__(self,username,password):
        self._username = username
        self._password = password
        self._online = True
        self._followers = set() # Set is the ideal data strucutre here in order to insure each follower is unique. 

    def follow(self,user):
        if not self._online:
            return
        if user is not self and self not in user._followers:
            user._followers.add(self)
            print(f"{self._username} started following {user._username}")

    def unfollow(self,user):
        if not self._online:
            return
        if user is not self and self in user._followers:
            user._followers.remove(self)
            print(f"{self._username} unfollowed {user._username}")

    def publish_post(self,post_type,data,price=None,location=None):
        if not self._online:
            return;
        return PostFactory.createPost(self,post_type,data,price,location)

    def print_notifications(self):
        if not self._online:
            return

    def isOnline(self):
        return self._online

    def __str__(self):
        return f"{self._username}"