
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
        self._comments = list() #Array of tuples, each tuple representing a comment: The (pointer) userObject of the comment poster and the text content of the comment. (<userObject pointer>,text)
    
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

    def stringify(self):
        # Each subclass implements their own 'stringify' method.
        pass

    def __str__(self):
        return self.stringify()
    
    def print(self):
        print(self.stringfy())

    def _getOPObject(self):
        return self._original_poster_obj

    def _getOPUsername(self):
        return self._getOPObject().getUsername()



# The following are the subclasses that inherit from Post.
            
class TextPost(Post):
    def __init__(self,original_poster_object,text):
        super().__init__(original_poster_object)
        self._text = text
        self._getOPObject().notify_followers("Post")
        print(self) #Print the post to console

    def stringify(self):
        return f"{self._getOPUsername()} published a post:\n\"{self._text}\"\n"

class ImagePost(Post):
    def __init__(self,original_poster_object,image_url):
        super().__init__(original_poster_object)
        self._image_url = image_url
        self._getOPObject().notify_followers("Post")
        print(self) #Print the post to console
    
    def display(self):
        if self._image_url:
            print("Shows picture")
    
    def stringify(self):
        return f"{self._getOPUsername()} posted a picture\n"

class SalePost(Post):
    def __init__(self,original_poster_object,product_name,price,location):
        super().__init__(original_poster_object)
        self._product_name = product_name
        self._price = price
        self._location = location
        self._isAvailable = True
        self._getOPObject().notify_followers("Post")
        print(self) #Print the post to console


    def sold(self,op_password):
        if not self._isAvailable :
            return #already sold
        if self._getOPObject().getPassword() == op_password:
            self._isAvailable = False
            print(f"{self._getOPUsername()}'s product is sold")

    def discount(self,percentage,op_password):
        if not self._isAvailable:
            return #already sold
        if self._getOPObject().getPassword() == op_password:
            newPrice = self._price - (self._price * (percentage/100))
            self._price = newPrice
            print(f"Discount on {self._getOPUsername()} product! the new price is: {newPrice}")

    def stringify(self):
        return f"{self._getOPUsername()} posted a product for sale:\n{'For sale!' if self._isAvailable else 'Sold!'} {self._product_name}, price: {self._price}, pickup from: {self._location}\n"



            

    
