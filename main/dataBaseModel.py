"""
1)
the validation case needs to be more informative..probably add more err code
eg. badUserID, badProductID

2)
also for a ForeignKey field, you need to actually add a reference model to it
eg. 
class Comment:
    owner = ForeignKey(User)
    ...

to add a new comment, you need
newComment = Comment()
newComment.owner = User.objects.get(id = uid)
newComment.save()

3) we just store a directory of the image in our user table, so when adding an image, we need a new "ImageWriter" class
to write the image to filesystem. Then here we just insert the URI to it

4) removeProduct
don't we just get a productID and remove it?
Product.objects.get(id = pid).delete()
"""

# This class encapsulates all communication with the DB
#from models import User
from django.contrib.auth.models import User
from models import Comment
from models import Product
from models import Category
from models import WishList

from django.db.models import Q

class dataBaseModel (object):
    
    SUCCESS = 1
    ERR_BAD_PRODUCT = -1
    ERR_BAD_USER = -2
    ERR_UNABLE_TO_REMOVE_FROM_WISHLIST = -3
    ERR_BAD_CATEGORY = -4

    
    
    def __init__(self):
        # do nothing
        pass
    """    
    Sth Idk how to do
    def addUserPhoto(self, userName, Photo):
        if userName is None:
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if Photo is None:
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num) 
        try{
            newOne = User.objects.get(Q(name = userName),)
    """                
    def addToWishList(self, userID, productID): # eddie: use ID instead of name

        if User.objects.filter(pk = userID).count() == 0:
            return dataBaseModel.ERR_BAD_USER
        
        if Product.objects.filter(pk = productID).count() == 0:
            return dataBaseModel.ERR_BAD_PRODUCT
        newOne = WishList(owner = User.objects.get(pk = userID), product = Product.objects.get(pk = productID))
        newOne.save()
        return dataBaseModel.SUCCESS


    def removeFromWishList(self, userID, productID): # use id as above
        try:
            newOne = WishList.objects.get(Q(owner = User.objects.get(pk = userID)), Q(product = Product.objects.get(pk = productID)))
        except:
            return dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST
        newOne.delete()
        return dataBaseModel.SUCCESS

    def getWishList(self, userID): # ID
        try:
            User.objects.get(pk = userID)
        except:
            return ([], dataBaseModel.ERR_BAD_USER)
        
        queryset = WishList.objects.filter(owner = User.objects.get(pk = userID))       
        items = []
        for item in queryset:
            items.append(item) # we now only obtain the product model..may be we want some specific field from the table

        return (items, dataBaseModel.SUCCESS)


    def addComment(self, userID, productID, content, time): # ID

        if User.objects.filter(pk = userID).count() == 0:
            return dataBaseModel.ERR_BAD_USER
        
        if Product.objects.filter(pk = productID).count() == 0:
            return dataBaseModel.ERR_BAD_PRODUCT
        
        newOne = Comment(owner = User.objects.get(pk = userID), product = Product.objects.get(pk = productID), content = content, time=time)
        newOne.save()
        return dataBaseModel.SUCCESS


    def getComments(self, productID): # here we just want to retreive a list of comments on that product
        if Product.objects.filter(pk = productID).count() == 0:
            return ([], dataBaseModel.ERR_BAD_PRODUCT)
        
        items = []
        for item in Comment.objects.filter(product = Product.objects.get(pk = productID)).order_by('time'):
            items.append(item)
        
        return (items, dataBaseModel.SUCCESS)


    def getProducts(self, category):
        queryset = Product.objects.filter(category = Category.objects.filter(name = category))
        if queryset.count() == 0:
            return ([], dataBaseModel.ERR_BAD_CATEGORY)
        # here you simply get the category, instead of products
        #newOne = Category.objects.get(Q(name = categoryName))
        items = []
        for item in queryset:
            items.append(item)
            
        return (items, dataBaseModel.SUCCESS)
    
    def getDetail(self, productID):
        if Product.objects.filter(pk=productID).count() != 1:
            return (None,dataBaseModel.ERR_BAD_PRODUCT)
        
        return (Product.objects.get(pk=productID), dataBaseModel.SUCCESS)
    
    
"""  sth idk how to do
    def removeProduct(userName, productName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None 
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        newOne = Product.objects.get(Q(owner = userName))     
"""   
