
class PostFactory:
    # Implemented with the "Factory" design pattern in mind.
    @staticmethod
    def createPost(original_poster,post_type,data,price=None,location=None):
        if post_type == "Text":
            return TextPost(original_poster,data)
        elif post_type == "Image":
            return ImagePost(original_poster,data)
        elif post_type == "Sale":
            return SalePost(original_poster,data,price,location)
        else:
            raise ValueError("Invalid post type")

class Post:

    def __init__(self,original_poster):
        self._original_poster = original_poster
        self._likes = set()
        self._comments = list() #Array of tuples, each tuples representing a comment: The poster of said comment and the text content of the comment. (user,text)
    
    def like(self,user):
        if user not in self._likes and user.isOnline():
            self._likes.add(user)
            if user is not self._original_poster:
                self._original_poster.notify_self(user,"Like")
       

    def comment(self,user,text):
        if user.isOnline():
            self._comments.append((user,text))
            if user is not self._original_poster:
                self._original_poster.notify_self(user,"Comment",text)



# The following are the subclasses that inherit from Post.
            
class TextPost(Post):
    def __init__(self,original_poster,text):
        super().__init__(original_poster)
        self._text = text
        print("TextPost Created")

class ImagePost(Post):
    def __init__(self,original_poster,image_url):
        super().__init__(original_poster)
        self._image_url = image_url
        print("ImagePost Created")



class SalePost(Post):
    def __init__(self,original_poster,product_name,price,location):
        super().__init__(original_poster)
        self._product_name = product_name
        self._price = price
        self._location = location
        self._isAvailable = True
        print("SalePost Created")
