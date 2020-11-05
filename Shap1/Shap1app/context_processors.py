from . models import *


def categories(request):
    b=product.objects.filter(prod_category='beer')
    w=product.objects.filter(prod_category='wine')
    l=product.objects.filter(prod_category='liquor')
    s=product.objects.filter(prod_category='snacks')

    return{
        'b':b,'w':w,'l':l,'s':s
    }
