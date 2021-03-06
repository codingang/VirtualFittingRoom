from main.dataBaseModel import dataBaseModel
from django.http import HttpResponse
import json
from django.templatetags.static import static
from django.shortcuts import redirect
from main.views.mainViews import index
from django.views.decorators.csrf import csrf_exempt

def getWishlist(request):
    if request.user.is_authenticated() == False:
        return HttpResponse(json.dumps([]), content_type='application/json')
    db = dataBaseModel()
    result = db.getWishList(request.user.id)
    data = []
    if result[1] != dataBaseModel.SUCCESS:       
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    for wish in result[0]:
        map = {'item_name': wish.product.name.title(), 
               'image' : static('products/' + wish.product.photo), 
               'price' : wish.product.price, 
               'description' : wish.product.description,
               'category' : wish.product.category.name.title(),
               'product_id' : wish.product.pk}
        data.append(map)
    return HttpResponse(json.dumps(data), content_type='application/json')
        
@csrf_exempt
def addToWishlist(request, category, product, id):
    if not (request.method == 'POST' and 'application/json' in request.META['CONTENT_TYPE'] and request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    result = db.addToWishList(request.user.id, product.lower(), id)
    return HttpResponse(json.dumps({'errCode' : result}), content_type='application/json')
    
@csrf_exempt
def removeFromWishlist(request, category, product, id):
    if not (request.method == 'POST' and 'application/json' in request.META['CONTENT_TYPE'] and request.user.is_authenticated()):
        return HttpResponse(json.dumps({'errCode' : dataBaseModel.ERR_BAD_REQUEST}), content_type='application/json')
    db = dataBaseModel()
    result = db.removeFromWishList(request.user.id, product.lower(), id)
    return HttpResponse(json.dumps({'errCode' : result}), content_type='application/json')
