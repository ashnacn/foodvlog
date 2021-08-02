from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def index(request):
    return render(request,'homepage.html')
def home(request,c_slug=None):
    c_page=None
    product=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product=Product.objects.filter(P_category=c_page,P_available=True)
    else:
        product=Product.objects.all().filter(P_available=True)
    cat=Category.objects.all()
    paginator=Paginator(product,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':product,'ct':cat,'pg':pro})



def prodDetails(request,c_slug,product_slug):
    try:
        prod = Product.objects.get(P_category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'item.html', {'pr': prod})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(P_name__contains=query) | Q(P_desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})
