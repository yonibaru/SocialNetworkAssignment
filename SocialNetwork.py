# Implemented with the singleton design pattern in mind, to insure only one instance of this class can exist at a time.
from User import User

class SocialNetwork:
    _name = ""
    _network = None

    # Set is the ideal data structure, because we need to insure each online user is unique.
    _online = set() #Set of username strings.

    # Dictionary is the ideal data structre because each user requires a unique name and we need a fast way to manipulate the user table.
    _users = dict() #username:<user_object_pointer>


    # def __init__(self):
    #     pass

    def __new__(cls,name):
        if cls._network is None:
            cls._network = super().__new__(cls) #the magical line, overriding .object's __new__ method
            cls._network._name = name
        return cls._network
    
    def __str__(self):
        pass
    
    def sign_up(self,username,password):
        if self._validNewUser(username,password):
            # Register the new user
            newUser = User(username,password)
            self._users.update({username:newUser}) # I think it's a good idea to have the value being a poiner to the actual object rather than just name:password. This way, we can access each user's unique methods.
            self._online.add(username)
            return newUser
        # If _validNewUser returns False, it will raise an Error. Why?:
        # The sign_up method is ALWAYS expected to return the new registered user. We can't return None here since the next time someone will try to access
        # one of the methods of a NULL user, we will be prompted an error anyway.
        # Returning the already-registered user seems like a security breach.
        # Therefore: if we can't create a user we must prompt an Error accordingly.

    def log_in(self,username,password):
        # If user is registered, offline and the password matches:
        if username not in self._users:
            return
        elif self.getUserObject(username).getPassword() != password:
            return
        if username not in self._online: 
            self._online.add(username)
            self.getUserObject.setOnline()
            print(f"{username} connected")


    def log_out(self,username):
        if username in self._online and username in self._users: #If user is registered and online
            self._online.remove(username)
            self.getUserObject(username).setOffline()
            print(f"{username} disconnected")

    def _validNewUser(self,username,password):
        passLength = len(password)
        if username is None or password is None:
            raise TypeError("Invalid username/password: cannot be equal to None.")
        elif passLength < 4 or passLength > 8:
            raise TypeError("Invalid password length: password has to be between 4 and 8 characters.")
        elif username in self._users:
            raise TypeError("Invalid username: username already taken.")    
        else: 
            return True
    
    def getUserObject(self,username):
        if username in self._users:
            return self._users.get(username)

        

