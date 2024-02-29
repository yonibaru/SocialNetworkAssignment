
class PostFactory:
    # Implemented with the "Factory" design pattern in mind.
    @staticmethod
    def createPost(original_poster_object,post_type,data,price=None,location=None):
        if post_type == "Text":
            return TextPost(original_poster_object,data)
        elif post_type == "Image":
            return ImagePost(original_poster_object,data)
        elif post_type == "Sale":
            return SalePost(original_poster_object,data,price,location)
        else:
            raise ValueError("Invalid post type")

class Post:


    def __init__(self,original_poster_object):
        self._original_poster_obj = original_poster_object
        self._likes = set() # A set of pointers to user objects.
        self._comments = list() #Array of tuples, each tuples representing a comment: The poster of said comment and the text content of the comment. (user,text)
    
    def like(self,userObject):
        if userObject not in self._likes and userObject.isOnline():
            self._likes.add(userObject)
            if userObject is not self._getOPObject():
                self._getOPObject().notify_self(userObject,"Like") #Notify OP that userObject liked his post
       

    def comment(self,userObject,text):
        if userObject.isOnline():
            self._comments.append((userObject,text))
            if userObject is not self._getOPObject():
                self._getOPObject().notify_self(userObject,"Comment",text) #Notify OP that userObject has commented on his post.

    def _getOPObject(self):
        return self._original_poster_obj



# The following are the subclasses that inherit from Post.
            
class TextPost(Post):
    def __init__(self,original_poster_object,text):
        super().__init__(original_poster_object)
        self._text = text

class ImagePost(Post):
    def __init__(self,original_poster_object,image_url):
        super().__init__(original_poster_object)
        self._image_url = image_url
    
    def display(self):
        if self._image_url:
            print("Shows picture")
    

 

class SalePost(Post):
    def __init__(self,original_poster_object,product_name,price,location):
        super().__init__(original_poster_object)
        self._product_name = product_name
        self._price = price
        self._location = location
        self._isAvailable = True

    def sold(self,op_password):
        if not self._isAvailable :
            return #already sold
        if self._getOPObject().getPassword() == op_password:
            self._isAvailable = False
            print(f"{self._getOPObject().getUsername()}'s product is sold")



    def discount(self,percentage,op_password):
        if not self._isAvailable:
            return #already sold
        if self._getOPObject().getPassword() == op_password:
            newPrice = self._price - (self._price * (percentage/100))
            self._price = newPrice
            print(f"Discount on {self._getOPObject().getUsername()} product! the new price is: {newPrice}")



            

    
