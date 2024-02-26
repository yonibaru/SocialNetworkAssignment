# Implemented with the singleton design pattern in mind, to insure only one instance of this class can exist at a time.
from User import User

class SocialNetwork:
    _name = ""
    _network = None
    _online = set() # Set is the ideal data structure, because we need to insure each online user is unique.
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
        if self._validNewUser(name,password):
            # Register the new user
            newUser = User(name,password)
            self._users.update({name:password})
            self._online.add(newUser)
            print("new user registered")
            return newUser
        # If _validNewUser returns False, it will raise an Error. Why?:
        # The sign_up method is ALWAYS expected to return the new registered user. We can't return None here since the next time someone will try to access
        # one of the methods a NULL user, we will be prompted an error anyway.
        # Returning the already-registered user seems like a security breach.
        # Therefore: if we can't create a user we must prompt an Error accordingly.

    def log_in(self,user):
        if user not in self._online and user._username in self._users: # If user is registered and offline
            self._online.add(user)
            user._online = True
            print(f"{user._username} connected")


    def log_out(self,user):
        if user in self._online and user._username in self._users: #If user is registered and online
            self._online.remove(user)
            user._online = False
            print(f"{user._username} disconnected")

    def _validNewUser(self,user,password):
        passLength = len(password)
        if user is None or password is None:
            raise TypeError("Invalid username/password: cannot be equal to None.")
        elif passLength < 4 or passLength > 8:
            raise TypeError("Invalid password length: password has to be between 4 and 8 characters.")
        elif user in self._users:
            raise TypeError("Invalid username: username already taken.")    
        else: 
            return True
    

        

