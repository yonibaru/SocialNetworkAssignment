# Implemented with the singleton design pattern in mind, to insure only one instance of this class can exist at a time.
from User import User

class SocialNetwork:
    _name = ""
    _network = None
    _online = set() # Set is the ideal data structure, because we need to ensure each online user is unique.
    _users = dict() # Dictionary is the ideal data structre because each user requires a unique name and we need a fast way to manipulate the user table.

    # def __init__(self):
    #     pass

    def __new__(cls,name):
        if cls._network is None:
            cls._network = super().__new__(cls) #the magical line, overriding .object's __new__ method
            cls._network._name = name
        return cls._network
    
    def __str__(self):
        pass
    
    def sign_up(self,name,password):

        #Register the new user
        newUser = User(name,password)
        self._users.update({name:password})
        self._online.add(newUser)
        return newUser

    def log_in(self,user):
        if user not in self._online and user._username in self._users: # If user is registered and offline
            self._online.add(user)
            user._online = True
            print(f"{user._username} connected")


    def log_out(self,user):
        if user in self._online and user._username in self._users: #If user registered and online
            self._online.remove(user)
            user._online = False
            print(f"{user._username} disconnected")

    def validateSignUp(self,user,password):
        pass
        # check if user exists
        # check valid password
    

        

