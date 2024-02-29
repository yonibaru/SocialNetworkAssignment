from Post import PostFactory

#Followers of said user are also designed with the 'Observer' design pattern, each follower acting as an Observer.
class User:
    def __init__(self,username,password):
        self._username = username
        self._password = password
        self._online = True
        # Set is the ideal data structure here in order to insure each follower is unique. 
        self._followers = set() #Set of pointers to user objects.
        self._notifications = list() #An ordered list of strings
        self._num_of_posts = 0

    def follow(self,userObject):
        if not self._online:
            return
        
        username = userObject.getUsername()
        if userObject is not self and self not in userObject._followers:
            userObject._followers.add(self)
            print(f"{self._username} started following {username}")

    def unfollow(self,userObject):

        if not self._online:
            return
        
        username = userObject.getUsername()
        if userObject is not self and self in userObject._followers:
            userObject._followers.remove(self)
            print(f"{self._username} unfollowed {username}")

    def publish_post(self,post_type,data,price=None,location=None):
        if not self._online:
            return;
        self._num_of_posts += 1
        return PostFactory.createPost(self,post_type,data,price,location)

    def print_notifications(self):
        if not self._online:
            return
        print(f"{self.getUsername()}'s notifications:")
        for notification in self._notifications:
            print(notification)


    def notify_self(self,notifierObject,type,comment=None):
        notifier_username = notifierObject.getUsername()
        if type == "Like":
            notification_text = f"{notifier_username} liked your post"
            print(f"notification to {self._username}: {notification_text}")
        elif type == "Comment":
            notification_text = f"{notifier_username} commented on your post"
            print(f"notification to {self._username}: {notification_text}: {comment}")
        elif type == "Post":
            notification_text = f"{notifier_username} has a new post"
        else:
            return
        self._notifications.append(notification_text)

    def notify_followers(self,type,comment=None):
        for follower in self._followers:
            follower.notify_self(self,type,comment) #Notifer is 'self'

    #Getters and setters
            
    def isOnline(self):
        return self._online
    
    def setOffline(self):
        self._online = False
    
    def setOnline(self):
        self._online = True
    
    def getPassword(self):
        #Terrible practice, but let's assume this is a hashed password.
        return self._password

    def getUsername(self):
        return self._username

    def stringify(self):
        return (f"User name: {self._username}, Number of posts: {self._num_of_posts}, "
                f"Number of followers: {len(self._followers)}")

    def __str__(self):
        return self.stringify()

        
